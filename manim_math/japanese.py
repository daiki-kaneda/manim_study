"""Japanese TeX template and Text helpers.

Font selection (first match wins):

1. Environment variable ``MANIM_JAPANESE_FONT``
2. Hannari Mincho (the font used in existing scenes)
3. Other CJK fonts available via fontconfig (Noto, IPA, WenQuanYi, ...)
"""

from __future__ import annotations

import os
import subprocess
from functools import lru_cache
from typing import Any

try:
    from manim import Scene, Tex, TexTemplate, Text
except ImportError:  # pragma: no cover - allows importing helpers without manim
    Scene = object  # type: ignore[misc, assignment]
    Tex = None  # type: ignore[assignment]
    TexTemplate = None  # type: ignore[assignment]
    Text = None  # type: ignore[assignment]

PREFERRED_FONTS = (
    "HannariMincho-Regular",
    "Hannari Mincho",
    "HannariMincho",
    "Hiragino Mincho ProN",
    "YuMincho",
    "Yu Mincho",
    "Noto Serif CJK JP",
    "Noto Sans CJK JP",
    "IPAexMincho",
    "IPAMincho",
    "WenQuanYi Micro Hei",
    "Droid Sans Fallback",
)


def _fontconfig_families() -> set[str]:
    try:
        out = subprocess.check_output(
            ["fc-list", ":lang=ja", "family"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, OSError):
        try:
            out = subprocess.check_output(
                ["fc-list", "family"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except (FileNotFoundError, subprocess.CalledProcessError, OSError):
            return set()

    families: set[str] = set()
    for line in out.splitlines():
        for part in line.split(","):
            name = part.strip()
            if name:
                families.add(name)
    return families


@lru_cache(maxsize=1)
def get_japanese_font() -> str:
    env = os.environ.get("MANIM_JAPANESE_FONT")
    if env:
        return env

    families = _fontconfig_families()
    exact = {name.lower(): name for name in families}
    for preferred in PREFERRED_FONTS:
        if preferred in families:
            return preferred
        if preferred.lower() in exact:
            return exact[preferred.lower()]

    for preferred in PREFERRED_FONTS:
        needle = preferred.lower()
        for family in families:
            if needle in family.lower() or family.lower() in needle:
                return family

    if families:
        return sorted(families)[0]
    return "sans-serif"


@lru_cache(maxsize=1)
def get_japanese_tex_template():
    if TexTemplate is None:
        raise ImportError("manim is required to build the Japanese TeX template")

    font = get_japanese_font()
    return TexTemplate(
        tex_compiler="xelatex",
        output_format=".xdv",
        documentclass=r"\documentclass[preview]{standalone}",
        preamble=rf"""
\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{fontspec}}
\setmainfont{{{font}}}
""",
    )


def ja_tex(*args: Any, **kwargs: Any):
    """``Tex`` with the shared Japanese xelatex template."""
    if Tex is None:
        raise ImportError("manim is required to create Tex mobjects")
    kwargs.setdefault("tex_template", get_japanese_tex_template())
    return Tex(*args, **kwargs)


def ja_text(text: str, **kwargs: Any):
    """``Text`` using the detected Japanese font (no TeX required)."""
    if Text is None:
        raise ImportError("manim is required to create Text mobjects")
    kwargs.setdefault("font", get_japanese_font())
    return Text(text, **kwargs)


class JapaneseScene(Scene):
    """Scene base with ``ja_tex`` / ``ja_text`` for Japanese titles and mixed math.

    Target length is about 30–60 seconds. Fill that with motion (longer
    ``run_time``, extra visual beats). Do not pad with long idle waits.
    ``beat`` remains for older scenes that call ``hold``.
    """

    beat = 3.0
    motion_scale = 1.0

    def ja_tex(self, *args: Any, **kwargs: Any):
        return ja_tex(*args, **kwargs)

    def ja_text(self, text: str, **kwargs: Any):
        return ja_text(text, **kwargs)

    def play(self, *args, **kwargs):
        scale = self.motion_scale
        if scale != 1.0:
            kwargs["run_time"] = kwargs.get("run_time", 1.0) * scale
        return super().play(*args, **kwargs)

    def hold(self, beats: float = 1.0) -> None:
        self.wait(max(0.0, self.beat * beats))

    def read(self, seconds: float = 0.55) -> None:
        """Brief look at the current frame, in seconds (not beats)."""
        self.wait(max(0.0, seconds))

    def show_heading(self, text: str, font_size: int = 42):
        """Fade in a Japanese title, then park it at the top edge."""
        from manim import FadeIn, UP

        title = self.ja_text(text, font_size=font_size)
        self.play(FadeIn(title), run_time=1.0)
        self.wait(0.5)
        self.play(title.animate.scale(0.55).to_edge(UP), run_time=0.6)
        return title


class LessonScene(JapaneseScene):
    """5–10 minute curriculum lessons (math / algorithm 200).

    Motion is not stretched. ``beat`` is 1 second so ``hold`` is a short
    reading pause, not the 3-second wait used by short-form scenes.
    Do not use ``PacedScene`` (``motion_scale=2.5``) for these lessons.
    """

    motion_scale = 1.0
    beat = 1.0

    def linger(self, seconds: float = 3.0) -> None:
        """Keep a definition or key result on screen long enough to read.

        Use this for statements that later steps rely on. Wall-clock seconds,
        not scaled by a scene-level ``wait`` override. Do not use it to pad.
        """
        super().wait(max(0.0, seconds))

    def aligned_table(self, rows, **kwargs):
        """Numeric comparison table with per-column left alignment.

        ``rows`` is a list of rows, each a list of LaTeX strings (``MathTable``)
        or already-built mobjects (``MobjectTable``).
        """
        from manim import GREY_B, LEFT, MathTable, MobjectTable, VMobject

        n_cols = len(rows[0])
        kwargs.setdefault("h_buff", 0.55)
        kwargs.setdefault("v_buff", 0.32)
        kwargs.setdefault("include_outer_lines", True)
        kwargs.setdefault("include_inner_lines", True)
        kwargs.setdefault(
            "line_config",
            {"stroke_width": 1.2, "color": GREY_B},
        )
        kwargs.setdefault(
            "arrange_in_grid_config",
            {
                "col_alignments": "l" * n_cols,
                "cell_alignment": LEFT,
            },
        )
        first = rows[0][0]
        if isinstance(first, VMobject):
            return MobjectTable(rows, **kwargs)
        kwargs.setdefault("element_to_mobject_config", {"font_size": 28})
        return MathTable(rows, **kwargs)

    def reveal_table(self, table, row_wait: float = 0.7) -> None:
        """Fade table rows in from top to bottom. Hide entries first so columns stay aligned."""
        rows = list(table.get_rows())
        for row in rows:
            row.set_opacity(0)
        self.add(table)
        for i, row in enumerate(rows):
            self.play(row.animate.set_opacity(1), run_time=0.4)
            self.wait(row_wait if i > 0 else 0.35)


class PacedScene(JapaneseScene):
    """30–60 second shorts: animations are stretched, idle waits are not."""

    motion_scale = 2.5
