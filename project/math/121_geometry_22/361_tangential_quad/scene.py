from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class TangentialQuad(PacedScene):
    """#361 接線四角形：対辺の和が等しい（ピトーと同型の強調）（約45秒）"""

    def construct(self):
        self.show_heading("接線四角形")
        self.draw_quad()
        self.sums()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        self.O = ORIGIN + DOWN * 0.1
        self.inc = Circle(radius=1.0, color=TEAL, stroke_width=3).move_to(self.O)
        self.pts = [
            self.O + np.array([2.3, 1.2, 0]),
            self.O + np.array([-1.9, 1.5, 0]),
            self.O + np.array([-2.1, -1.4, 0]),
            self.O + np.array([2.1, -1.3, 0]),
        ]
        self.quad = Polygon(*self.pts, color=BLUE, stroke_width=3)
        self.play(Create(self.inc), Create(self.quad), run_time=1.4)
        note = self.ja_text("内接円あり", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sums(self):
        s01 = Line(self.pts[0], self.pts[1], color=ORANGE, stroke_width=6)
        s23 = Line(self.pts[2], self.pts[3], color=ORANGE, stroke_width=6)
        s12 = Line(self.pts[1], self.pts[2], color=YELLOW, stroke_width=6)
        s30 = Line(self.pts[3], self.pts[0], color=YELLOW, stroke_width=6)
        cap = self.ja_text("対辺の組", font_size=24).move_to(self.note)
        self.play(Create(s01), Create(s23), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("和が等しい", font_size=24).move_to(self.note)
        self.play(Create(s12), Create(s30), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"a+c").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"a+c=b+d").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"a+c=b+d").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
