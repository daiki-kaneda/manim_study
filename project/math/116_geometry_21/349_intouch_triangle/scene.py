from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class IntouchTriangle(PacedScene):
    """#349 接点三角形：内接円の接点を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("接点三角形")
        self.draw_base()
        self.intouch()
        self.show_formula()
        self.read(1.4)

    def draw_base(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.5 + DOWN * 1.5
        self.C = RIGHT * 2.5 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.I = (self.A + self.B + self.C) / 3 + DOWN * 0.15
        self.inc = Circle(radius=0.75, color=TEAL, stroke_width=3).move_to(self.I)
        self.play(Create(self.tri), Create(self.inc), run_time=1.4)
        note = self.ja_text("内接円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def intouch(self):
        def foot(P, Q):
            v = Q - P
            t = np.dot(self.I - P, v) / np.dot(v, v)
            return P + float(np.clip(t, 0.1, 0.9)) * v
        Ta = foot(self.B, self.C)
        Tb = foot(self.A, self.C)
        Tc = foot(self.A, self.B)
        contact = Polygon(Ta, Tb, Tc, color=ORANGE, stroke_width=3)
        cap = self.ja_text("接点", font_size=24).move_to(self.note)
        self.play(FadeIn(VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in (Ta, Tb, Tc)])), Transform(self.note, cap), run_time=1.1)
        self.play(Create(contact), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("接点三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("内接円の接点を結ぶ", font_size=30)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
