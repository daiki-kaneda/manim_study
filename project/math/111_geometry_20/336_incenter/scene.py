from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Incenter(PacedScene):
    """#336 内心：角の二等分線の交点（約45秒）"""

    def construct(self):
        self.show_heading("内心")
        self.draw_triangle()
        self.bisectors()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.6 + DOWN * 1.5
        self.C = RIGHT * 2.6 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bisectors(self):
        I = (self.A + self.B + self.C) / 3 + DOWN * 0.15
        lines = VGroup(
            Line(self.A, I + (I - self.A) * 0.15, color=YELLOW, stroke_width=3),
            Line(self.B, I + (I - self.B) * 0.15, color=YELLOW, stroke_width=3),
            Line(self.C, I + (I - self.C) * 0.15, color=YELLOW, stroke_width=3),
        )
        # angle marks
        a1 = Angle(Line(self.A, self.B), Line(self.A, self.C), radius=0.4, color=TEAL)
        cap = self.ja_text("角の二等分", font_size=24).move_to(self.note)
        self.play(Create(a1), Transform(self.note, cap), run_time=1.0)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.12), run_time=1.3)
        self.read(0.2)
        inc = Circle(radius=0.7, color=ORANGE, stroke_width=3).move_to(I)
        cap2 = self.ja_text("円の中心", font_size=24).move_to(self.note)
        self.play(FadeIn(Dot(I, color=RED, radius=0.1)), Create(inc), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"I\sim(a:b:c)").scale(1.05)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
