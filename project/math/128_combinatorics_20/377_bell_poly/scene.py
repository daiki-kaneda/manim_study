from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BellPolynomials(PacedScene):
    """#377 ベル多項式：集合分割を重み付きで数える（約45秒）"""

    def construct(self):
        self.show_heading("ベル多項式")
        self.draw_blocks()
        self.weight()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        # partition of 4 elements into blocks
        els = VGroup(*[
            Dot(LEFT * 2.5 + RIGHT * i * 0.7 + UP * 1.0, color=BLUE, radius=0.12)
            for i in range(4)
        ])
        b1 = SurroundingRectangle(VGroup(els[0], els[1]), color=ORANGE, buff=0.2)
        b2 = SurroundingRectangle(els[2], color=TEAL, buff=0.25)
        b3 = SurroundingRectangle(els[3], color=YELLOW, buff=0.25)
        self.play(FadeIn(els), run_time=1.0)
        self.play(Create(b1), Create(b2), Create(b3), run_time=1.2)
        note = self.ja_text("ブロック分割", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def weight(self):
        weights = VGroup(
            MathTex(r"x_2", color=ORANGE, font_size=34).shift(LEFT * 2.1 + DOWN * 0.3),
            MathTex(r"x_1", color=TEAL, font_size=34).shift(LEFT * 0.4 + DOWN * 0.3),
            MathTex(r"x_1", color=YELLOW, font_size=34).shift(RIGHT * 0.9 + DOWN * 0.3),
        )
        cap = self.ja_text("サイズで重み", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(w) for w in weights], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("多項式へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"B_n(x_1,\ldots,x_n)=\sum_{\pi}\prod_{B\in\pi}x_{|B|}").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
