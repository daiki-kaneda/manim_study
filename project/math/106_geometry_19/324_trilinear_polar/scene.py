from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class TrilinearPolar(PacedScene):
    """#324 三線極線：点に対する極線（約45秒）"""

    def construct(self):
        self.show_heading("三線極線")
        self.draw_triangle()
        self.polar()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.6 + DOWN * 1.5
        self.C = RIGHT * 2.6 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.P = (self.A + self.B + self.C) / 3 + UP * 0.35
        self.play(Create(self.tri), FadeIn(Dot(self.P, color=ORANGE, radius=0.1)), run_time=1.3)
        note = self.ja_text("点 P", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def polar(self):
        # polar line roughly across triangle
        L = Line(LEFT * 2.8 + DOWN * 0.4, RIGHT * 2.8 + DOWN * 0.1, color=YELLOW, stroke_width=4)
        # cevian intersections hint
        feet = VGroup(*[Dot(p, color=TEAL, radius=0.08) for p in [
            self.B * 0.4 + self.C * 0.6, self.A * 0.35 + self.C * 0.65, self.A * 0.4 + self.B * 0.6
        ]])
        cap = self.ja_text("接点を結ぶ", font_size=24).move_to(self.note)
        self.play(FadeIn(feet), Transform(self.note, cap), run_time=1.1)
        self.play(Create(L), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("極線", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"xX+yY+zZ=0").scale(1.05)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
