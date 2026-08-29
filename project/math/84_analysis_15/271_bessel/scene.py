from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class BesselInequality(PacedScene):
    """#271 ベッセル：係数の二乗和 ≤ ノルム（約45秒）"""

    def construct(self):
        self.show_heading("ベッセルの不等式")
        self.draw_basis()
        self.project()
        self.show_formula()
        self.read(1.4)

    def draw_basis(self):
        self.O = LEFT * 0.5 + DOWN * 0.2
        e1 = Arrow(self.O, self.O + RIGHT * 2.2, buff=0, color=GREY, stroke_width=3)
        e2 = Arrow(self.O, self.O + UP * 2.0, buff=0, color=GREY, stroke_width=3)
        self.v = Arrow(self.O, self.O + RIGHT * 1.6 + UP * 1.3, buff=0, color=BLUE, stroke_width=5)
        self.play(GrowArrow(e1), GrowArrow(e2), run_time=1.1)
        self.play(GrowArrow(self.v), run_time=1.1)
        note = self.ja_text("正規直交", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.e1, self.e2 = e1, e2

    def project(self):
        p1_end = self.O + RIGHT * 1.6
        p2_end = self.O + UP * 1.3
        p1 = Arrow(self.O, p1_end, buff=0, color=ORANGE, stroke_width=4)
        p2 = Arrow(self.O, p2_end, buff=0, color=TEAL, stroke_width=4)
        cap = self.ja_text("係数の射影", font_size=24).move_to(self.note)
        self.play(GrowArrow(p1), GrowArrow(p2), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        squares = MathTex(r"a_1^{2}+a_2^{2}", color=YELLOW).scale(0.95).shift(RIGHT * 2.6 + DOWN * 0.3)
        cap2 = self.ja_text("二乗和 ≤", font_size=24).move_to(self.note)
        self.play(Write(squares), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\sum_k|\langle f,e_k\rangle|^{2}\le\|f\|^{2}").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
