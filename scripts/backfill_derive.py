#!/usr/bin/env python3
"""Backfill derive()/proof beats onto paced scenes #126–#1325."""
from __future__ import annotations

import ast
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DERIVE_METHOD = '''
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.75)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex({step1}).scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex({step2}).scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq
'''


def load_catalog():
    spec = importlib.util.spec_from_file_location("math_catalog", ROOT / "project/math/catalog.py")
    cat = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = cat
    assert spec.loader is not None
    spec.loader.exec_module(cat)
    rows = []
    for name, val in vars(cat).items():
        if name.startswith("VIDEOS_") and isinstance(val, tuple):
            rows.extend(val)
    return sorted(rows, key=lambda v: v.number)


def extract_mathtex_arg(show_body: str) -> str | None:
    """Return the argument expression inside MathTex(...), or None."""
    m = re.search(r"MathTex\((.+)\)\.scale\(", show_body, re.S)
    if not m:
        m = re.search(r"formula\s*=\s*MathTex\((.+)\)\.scale\(", show_body, re.S)
    if not m:
        return None
    return m.group(1).strip()


def step_args_from_mathtex_arg(arg: str) -> tuple[str, str]:
    """Build MathTex argument expressions for derive step1/step2."""
    # Simple string / raw string with '='
    m = re.fullmatch(r"[rR]?(['\"])(.*)\1", arg, re.S)
    if m:
        q, body = m.group(1), m.group(2)
        # unescape lightly for split only
        raw = body
        if "=" in raw:
            left = raw.split("=", 1)[0].rstrip()
            if left:
                return f"{'' if arg[0] not in 'rR' else arg[0]}{q}{left}{q}", arg
        return arg, arg

    # Concatenated form: look for "=' or '=' pattern in pieces
    if "=" in arg:
        # Prefer using a short implication then full formula
        return r'"\Rightarrow"', arg
    return r'"\cdots"', arg


def patch_construct(text: str) -> str:
    if re.search(r"self\.derive\(\)", text):
        return text

    def repl(m: re.Match) -> str:
        body = m.group(0)
        if "self.derive()" in body:
            return body
        if "self.show_formula()" not in body:
            return body
        return body.replace("self.show_formula()", "self.derive()\n        self.show_formula()", 1)

    return re.sub(
        r"def construct\(self\):(?:\n(?:    .*|\s*)*?)\n(?=\n    def |\Z)",
        repl,
        text,
        count=1,
        flags=re.M,
    )


def patch_show_formula(text: str) -> str:
    """Make show_formula transform from proof_eq when present."""

    def repl(m: re.Match) -> str:
        block = m.group(0)
        if "self.proof_eq" in block:
            return block
        # to_edge -> move_to proof_eq
        block2 = re.sub(
            r"formula\.to_edge\(DOWN,\s*buff=[^\)]+\)",
            "formula.move_to(self.proof_eq)",
            block,
            count=1,
        )
        # Write(formula) -> Transform(self.proof_eq, formula)
        block2 = re.sub(
            r"self\.play\(Write\(formula\)\s*,\s*run_time=([^\)]+)\)",
            r"self.play(Transform(self.proof_eq, formula), run_time=\1)",
            block2,
            count=1,
        )
        # Indicate(formula -> Indicate(self.proof_eq
        block2 = block2.replace("Indicate(formula,", "Indicate(self.proof_eq,")
        return block2

    return re.sub(
        r"def show_formula\(self\):(?:\n(?:    .*|\s*)*?)\n(?=\n    def |\Z)",
        repl,
        text,
        count=1,
        flags=re.M,
    )


def insert_derive_method(text: str, step1: str, step2: str) -> str:
    if "def derive(self)" in text:
        return text
    method = DERIVE_METHOD.format(step1=step1, step2=step2)
    # Insert before show_formula
    if "def show_formula(self):" not in text:
        # append before end
        return text.rstrip() + "\n" + method + "\n"
    return text.replace("def show_formula(self):", method + "\n    def show_formula(self):", 1)


def upgrade_storyboard(path: Path) -> None:
    if not path.is_file():
        return
    t = path.read_text(encoding="utf-8")
    if "導出" in t:
        return
    # Append a short note
    t = t.rstrip() + "\n\n- 導出: 途中式→整理→結論式（`derive()`）で尺を確保\n"
    path.write_text(t, encoding="utf-8")


def upgrade_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "def derive(self)" in text and "self.derive()" in text and "self.proof_eq" in text:
        return False
    if "PacedScene" not in text:
        return False
    if "def show_formula(self)" not in text:
        return False

    m = re.search(
        r"def show_formula\(self\):(?:\n(?:    .*|\s*)*?)\n(?=\n    def |\Z)",
        text,
        flags=re.M,
    )
    if not m:
        return False
    arg = extract_mathtex_arg(m.group(0))
    if not arg:
        # fallback generic steps
        step1, step2 = r'"\cdots"', r'"\Rightarrow"'
    else:
        step1, step2 = step_args_from_mathtex_arg(arg)
        # If step2 was meant to be full formula arg, use arg
        if step2 != arg and arg:
            step2 = arg

    text2 = patch_construct(text)
    text2 = insert_derive_method(text2, step1, step2)
    text2 = patch_show_formula(text2)

    # Validate syntax
    try:
        ast.parse(text2)
    except SyntaxError as e:
        raise RuntimeError(f"syntax error patching {path}: {e}") from e

    path.write_text(text2, encoding="utf-8")
    upgrade_storyboard(path.parent / "storyboard.md")
    return True


def main() -> None:
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 126
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 1325
    rows = [v for v in load_catalog() if start <= v.number <= end]
    changed = 0
    skipped = 0
    errors: list[tuple[int, str]] = []
    for v in rows:
        path = ROOT / v.path
        try:
            if upgrade_file(path):
                changed += 1
            else:
                skipped += 1
        except Exception as e:  # noqa: BLE001
            errors.append((v.number, str(e)))
    print(f"range {start}-{end}: changed={changed} skipped={skipped} errors={len(errors)}")
    for num, err in errors[:20]:
        print(" ERR", num, err)
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
