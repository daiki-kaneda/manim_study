from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class BlockILU(PacedScene):
    """#599 ブロックILU：ブロック単位の不完全分解（約45秒）"""

    def construct(self):
        self.show_heading("ブロックILU")
        self.draw_blocks()
        self.factor()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        cells = VGroup()
        for i in range(3):
            for j in range(3):
                sq = Square(0.9, color=BLUE if i == j else GREY, fill_opacity=0.35 if i == j else 0.1, stroke_width=2)
                sq.shift(LEFT * 2.0 + RIGHT * j * 1.0 + UP * 1.0 + DOWN * i * 1.0)
                cells.add(sq)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.04), run_time=1.3)
        note = self.ja_text("ブロック構造", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def factor(self):
        cap = self.ja_text("ブロックで LU", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("疎性を保つ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A\approx \tilde L_B\tilde U_B").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
