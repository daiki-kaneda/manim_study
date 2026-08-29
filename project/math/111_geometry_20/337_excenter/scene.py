from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Excenter(PacedScene):
    """#337 傍心：外角二等分線の交点（約45秒）"""

    def construct(self):
        self.show_heading("傍心")
        self.draw_triangle()
        self.excenter()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 1.8
        self.B = LEFT * 2.4 + DOWN * 1.4
        self.C = RIGHT * 2.4 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def excenter(self):
        # excenter opposite A roughly below BC
        Ia = (self.B + self.C) / 2 + DOWN * 1.3
        # exterior bisector hints
        ext = Line(self.B + LEFT * 1.2, self.C + RIGHT * 1.2, color=GREY, stroke_width=2)
        lines = VGroup(
            Line(self.B, Ia, color=YELLOW, stroke_width=3),
            Line(self.C, Ia, color=YELLOW, stroke_width=3),
            Line(self.A, Ia, color=TEAL, stroke_width=3),
        )
        cap = self.ja_text("外角二等分", font_size=24).move_to(self.note)
        self.play(Create(ext), Transform(self.note, cap), run_time=1.1)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.1), run_time=1.3)
        self.read(0.2)
        circ = Circle(radius=0.55, color=ORANGE, stroke_width=3).move_to(Ia)
        cap2 = self.ja_text("円の中心", font_size=24).move_to(self.note)
        self.play(FadeIn(Dot(Ia, color=RED, radius=0.1)), Create(circ), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"I_a\sim(-a:b:c)").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
