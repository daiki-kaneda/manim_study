from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class CyclicQuad(PacedScene):
    """#265 内接四角形の対角の和は π（約45秒）"""

    def construct(self):
        self.show_heading("円に内接する四角形")
        self.draw_quad()
        self.opposite_angles()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        self.O = ORIGIN + DOWN * 0.1
        self.R = 2.2
        self.circ = Circle(radius=self.R, color=GREY, stroke_width=2).move_to(self.O)
        angs = [0.3, 1.5, 2.9, 5.0]
        self.pts = [self.O + self.R * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        self.quad = Polygon(*self.pts, color=BLUE, stroke_width=3)
        self.play(Create(self.circ), run_time=1.0)
        self.play(Create(self.quad), run_time=1.3)
        note = self.ja_text("内接四角形", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def opposite_angles(self):
        a0 = Angle(Line(self.pts[0], self.pts[3]), Line(self.pts[0], self.pts[1]), radius=0.4, color=ORANGE)
        a2 = Angle(Line(self.pts[2], self.pts[1]), Line(self.pts[2], self.pts[3]), radius=0.4, color=ORANGE)
        self.play(Create(a0), Create(a2), run_time=1.4)
        cap = self.ja_text("対角", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.3)
        cap2 = self.ja_text("和は 180°", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\angle A+\angle C=\pi").scale(1.05)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
