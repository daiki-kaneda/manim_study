from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Gergonne(PacedScene):
    """#288 ジェルゴンヌ点：接点と頂点を結ぶと一点（約45秒）"""

    def construct(self):
        self.show_heading("ジェルゴンヌ点")
        self.draw_triangle()
        self.cevians()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1 + LEFT * 0.2
        self.B = LEFT * 2.6 + DOWN * 1.5
        self.C = RIGHT * 2.8 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        # incenter approx
        self.I = (self.A + self.B + self.C) / 3 + DOWN * 0.15
        r = 0.75
        self.inc = Circle(radius=r, color=TEAL, stroke_width=3).move_to(self.I)
        self.play(Create(self.tri), run_time=1.1)
        self.play(Create(self.inc), run_time=0.9)
        note = self.ja_text("内接円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cevians(self):
        # touch points approx on sides
        def touch(P, Q):
            # point on PQ closest to I
            v = Q - P
            t = np.dot(self.I - P, v) / np.dot(v, v)
            t = float(np.clip(t, 0.15, 0.85))
            return P + t * v

        Ta = touch(self.B, self.C)
        Tb = touch(self.A, self.C)
        Tc = touch(self.A, self.B)
        dots = VGroup(*[Dot(p, color=ORANGE, radius=0.08) for p in (Ta, Tb, Tc)])
        lines = VGroup(
            Line(self.A, Ta, color=YELLOW, stroke_width=3),
            Line(self.B, Tb, color=YELLOW, stroke_width=3),
            Line(self.C, Tc, color=YELLOW, stroke_width=3),
        )
        cap = self.ja_text("接点と結ぶ", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.0)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.12), run_time=1.3)
        self.read(0.25)
        Ge = Dot(self.I + UP * 0.05, color=RED, radius=0.11)
        cap2 = self.ja_text("一点で交わる", font_size=24).move_to(self.note)
        self.play(FadeIn(Ge, scale=0.5), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
