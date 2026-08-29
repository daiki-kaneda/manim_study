from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene
from manim_math.geometry import apply_2d


class MatrixTrace(PacedScene):
    """#128 トレースは対角の和（約40秒）"""

    def construct(self):
        self.origin = LEFT * 2.7 + DOWN * 1.2
        self.unit = 1.35
        self.show_heading("トレース")
        self.draw_matrix_and_square()
        self.rotate_shape()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _poly(self, mat):
        corners = [apply_2d(mat, c)[:2] for c in ((0, 0), (1, 0), (1, 1), (0, 1))]
        return Polygon(*[self._pt(c) for c in corners], color=BLUE, fill_opacity=0.4, stroke_width=2)

    def draw_matrix_and_square(self):
        mat = MathTex(r"A=\begin{bmatrix}2&1\\0&1\end{bmatrix}", font_size=40)
        mat.to_edge(RIGHT, buff=0.45).shift(UP * 1.15)
        self.play(Write(mat), run_time=1.6)
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 4.2, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.1, color=GREY, stroke_width=2)
        self.sq = self._poly([[2.0, 1.0], [0.0, 1.0]])
        self.play(Create(ax), Create(ay), FadeIn(self.sq), run_time=1.3)
        d1 = MathTex("2", color=YELLOW, font_size=32).next_to(mat, DOWN, buff=0.35)
        d2 = MathTex("1", color=YELLOW, font_size=32).next_to(d1, DOWN, buff=0.2)
        self.play(FadeIn(d1), FadeIn(d2), run_time=0.7)
        self.read(0.45)
        self.mat, self.d1, self.d2 = mat, d1, d2

    def rotate_shape(self):
        rot = [[0.0, -1.0], [1.0, 0.0]]
        A = [[2.0, 1.0], [0.0, 1.0]]
        RA = [
            [rot[0][0] * A[0][0] + rot[0][1] * A[1][0], rot[0][0] * A[0][1] + rot[0][1] * A[1][1]],
            [rot[1][0] * A[0][0] + rot[1][1] * A[1][0], rot[1][0] * A[0][1] + rot[1][1] * A[1][1]],
        ]
        spun = self._poly(RA)
        note = self.ja_text("回しても和は 3", font_size=24)
        note.next_to(self.d2, DOWN, buff=0.35)
        self.play(Transform(self.sq, spun), FadeIn(note), run_time=1.8)
        self.read(0.55)

    def show_formula(self):
        formula = MathTex(r"\mathrm{tr}\,A=a_{11}+a_{22}").scale(1.0)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
