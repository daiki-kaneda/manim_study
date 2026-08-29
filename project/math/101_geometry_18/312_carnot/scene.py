from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Carnot(PacedScene):
    """#312 カルノー：垂心と外心の距離公式の仲間（約45秒）"""

    def construct(self):
        self.show_heading("カルノーの定理")
        self.draw_triangle()
        self.signed_dists()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.0 + LEFT * 0.3
        self.B = LEFT * 2.5 + DOWN * 1.5
        self.C = RIGHT * 2.7 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.O = (self.A + self.B + self.C) / 3 + DOWN * 0.1
        circ = Circle(radius=2.35, color=GREY, stroke_width=2).move_to(self.O)
        self.play(Create(self.tri), Create(circ), run_time=1.4)
        note = self.ja_text("外接円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def signed_dists(self):
        # signed distances from O to sides as dashed
        feet = [(self.B + self.C) / 2, (self.A + self.C) / 2, (self.A + self.B) / 2]
        segs = VGroup(*[DashedLine(self.O, f, color=ORANGE, stroke_width=3) for f in feet])
        self.play(FadeIn(Dot(self.O, color=YELLOW, radius=0.1)), LaggedStart(*[Create(s) for s in segs], lag_ratio=0.1), run_time=1.5)
        cap = self.ja_text("辺への距離", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.7)
        self.read(0.25)
        cap2 = self.ja_text("和が R+r", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"d_a+d_b+d_c=R+r").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
