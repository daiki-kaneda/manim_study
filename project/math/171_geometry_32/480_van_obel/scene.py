from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class VanObel(PacedScene):
    """#480 ヴァン・オーベル：チェバ比の積（約45秒）"""

    def construct(self):
        self.show_heading("ヴァン・オーベル")
        self.draw_triangle()
        self.cevians()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.2
        self.B = LEFT * 2.8 + DOWN * 1.5
        self.C = RIGHT * 2.8 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("チェバ線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cevians(self):
        D = self.B * 0.45 + self.C * 0.55
        E = self.A * 0.4 + self.C * 0.6
        F = self.A * 0.55 + self.B * 0.45
        P = (self.A + self.B + self.C) / 3.2
        lines = VGroup(
            Line(self.A, D, color=ORANGE, stroke_width=3),
            Line(self.B, E, color=ORANGE, stroke_width=3),
            Line(self.C, F, color=ORANGE, stroke_width=3),
        )
        dot = Dot(P, color=YELLOW, radius=0.1)
        cap = self.ja_text("比の和", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.15), FadeIn(dot), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("チェバ上の関係", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\frac{AP}{PD}=\frac{AF}{FB}+\frac{AE}{EC}").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
