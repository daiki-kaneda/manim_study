from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Cramer(PacedScene):
    """#155 クラメルは面積の比（約50秒）"""

    def construct(self):
        self.origin = LEFT * 3.4 + DOWN * 1.55
        self.show_heading("クラメルの公式")
        self.draw_base()
        self.replace_col()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def _para(self, u, v, color, opacity=0.28):
        return Polygon(
            self.origin,
            self._pt(u),
            self._pt(u + v),
            self._pt(v),
            color=color,
            fill_opacity=opacity,
            stroke_width=3,
        )

    def draw_base(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 6.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.9, color=GREY, stroke_width=2)
        self.a1 = np.array([2.5, 0.45])
        self.a2 = np.array([0.7, 2.35])
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.para = self._para(self.a1, self.a2, BLUE)
        e1 = Arrow(self.origin, self._pt(self.a1), buff=0, color=BLUE, stroke_width=4)
        e2 = Arrow(self.origin, self._pt(self.a2), buff=0, color=GREEN, stroke_width=4)
        self.play(FadeIn(self.para), GrowArrow(e1), GrowArrow(e2), run_time=1.6)
        note = self.ja_text("det A", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note
        self.e1 = e1

    def replace_col(self):
        b = np.array([3.15, 1.55])
        nb = Arrow(self.origin, self._pt(b), buff=0, color=YELLOW, stroke_width=5)
        npara = self._para(b, self.a2, YELLOW, opacity=0.32)
        cap = self.ja_text("列を b に", font_size=24).move_to(self.note)
        self.play(Transform(self.e1, nb), Transform(self.para, npara), Transform(self.note, cap), run_time=1.9)
        self.read(0.4)
        cap2 = self.ja_text("面積の比", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"x").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x=\frac{\det A_x}{\det A}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x=\frac{\det A_x}{\det A}").scale(1.0)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
