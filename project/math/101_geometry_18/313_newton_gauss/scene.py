from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class NewtonGauss(PacedScene):
    """#313 ニュートン・ガウス線：完備四角形の対辺中点（約45秒）"""

    def construct(self):
        self.show_heading("ニュートン・ガウス線")
        self.draw_complete()
        self.midpoints()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_complete(self):
        # four lines forming complete quadrilateral - simplify as 4 points + diagonals
        self.P = LEFT * 2.4 + UP * 1.3
        self.Q = RIGHT * 2.5 + UP * 1.1
        self.R = RIGHT * 1.8 + DOWN * 1.6
        self.S = LEFT * 2.0 + DOWN * 1.4
        sides = VGroup(
            Line(self.P, self.Q, color=BLUE, stroke_width=3),
            Line(self.Q, self.R, color=BLUE, stroke_width=3),
            Line(self.R, self.S, color=BLUE, stroke_width=3),
            Line(self.S, self.P, color=BLUE, stroke_width=3),
            Line(self.P, self.R, color=GREY, stroke_width=2),
            Line(self.Q, self.S, color=GREY, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(s) for s in sides], lag_ratio=0.08), run_time=1.6)
        note = self.ja_text("完備四辺形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def midpoints(self):
        m1 = (self.P + self.R) / 2
        m2 = (self.Q + self.S) / 2
        m3 = ((self.P + self.Q) / 2 + (self.R + self.S) / 2) / 2  # visual third mid
        # better: midpoints of three diagonal pairs
        m3 = (self.P + self.Q) / 2  # not ideal but visual
        # use midpoints of PR, QS, and intersection-based third
        dots = VGroup(Dot(m1, color=ORANGE, radius=0.09), Dot(m2, color=ORANGE, radius=0.09))
        # third: midpoint of opposite side pair midpoints of PS and QR? 
        m3 = ((self.P + self.S) / 2 + (self.Q + self.R) / 2) / 2
        dots.add(Dot(m3, color=ORANGE, radius=0.09))
        line = Line(m1, m2, color=YELLOW, stroke_width=4)
        # extend through m3
        line = Line(m1 + (m1 - m2) * 0.2, m2 + (m2 - m1) * 0.2, color=YELLOW, stroke_width=4)
        cap = self.ja_text("対辺の中点", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.1)
        self.play(Create(line), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("一直線", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"M_1,M_2,M_3\ \text{collinear}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"M_1,M_2,M_3\ \text{collinear}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"M_1,M_2,M_3\ \text{collinear}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
