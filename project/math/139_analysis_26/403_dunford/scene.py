from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class DunfordCalculus(PacedScene):
    """#403 ダンフォード：コーシー積分で f(A) を定義（約45秒）"""

    def construct(self):
        self.show_heading("ダンフォード積分")
        self.draw_contour()
        self.integral()
        self.show_formula()
        self.read(1.4)

    def draw_contour(self):
        self.O = ORIGIN + DOWN * 0.1
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 2.8, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 1.8, self.O + UP * 1.8, color=GREY, stroke_width=2)
        eigs = VGroup(*[Dot(self.O + RIGHT * x, color=ORANGE, radius=0.1) for x in [-1.2, 0.4, 1.6]])
        cont = Ellipse(width=5.0, height=2.6, color=BLUE, stroke_width=3).move_to(self.O)
        self.play(Create(ax), Create(ay), FadeIn(eigs), Create(cont), run_time=1.5)
        note = self.ja_text("囲む路", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def integral(self):
        arrow = CurvedArrow(LEFT * 2.2 + UP * 1.1, RIGHT * 2.2 + UP * 1.1, color=YELLOW, stroke_width=3)
        cap = self.ja_text("コーシー積分", font_size=24).move_to(self.note)
        self.play(Create(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("f(A) を定義", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"f(A)=rac1{2\pi i}\oint f(z)(z-A)^{-1}dz").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
