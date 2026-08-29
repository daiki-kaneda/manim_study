from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class OrthogonalMatrix(PacedScene):
    """#144 直交行列は長さを保つ（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.2 + DOWN * 0.15
        self.show_heading("直交行列")
        self.draw_shape()
        self.turn()
        self.show_formula()
        self.read(1.4)

    def _rot(self, deg):
        t = deg * DEGREES
        c, s = np.cos(t), np.sin(t)
        return np.array([[c, -s], [s, c]])

    def _apply(self, mat, xy):
        v = mat @ np.array(xy)
        return self.origin + RIGHT * v[0] + UP * v[1]

    def _poly(self, mat):
        corners = [(1.2, 0.35), (2.15, 0.35), (2.15, 1.35), (1.2, 1.35)]
        return Polygon(
            *[self._apply(mat, c) for c in corners],
            color=BLUE,
            fill_opacity=0.4,
            stroke_width=3,
        )

    def _arrows(self, mat):
        a = Arrow(self.origin, self._apply(mat, (1.55, 0)), buff=0, color=YELLOW, stroke_width=4)
        b = Arrow(self.origin, self._apply(mat, (0, 1.55)), buff=0, color=GREEN, stroke_width=4)
        return VGroup(a, b)

    def draw_shape(self):
        ax = Line(self.origin + LEFT * 2.3, self.origin + RIGHT * 3.4, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.15, self.origin + UP * 2.25, color=GREY, stroke_width=2)
        ring = Circle(radius=1.55, color=GREY_B, stroke_width=2).move_to(self.origin)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.play(Create(ring), run_time=1.1)
        self.shape = self._poly(self._rot(0))
        self.arr = self._arrows(self._rot(0))
        self.play(FadeIn(self.shape), GrowArrow(self.arr[0]), GrowArrow(self.arr[1]), run_time=1.4)
        note = self.ja_text("長さ 1", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.4)
        self.note = note

    def turn(self):
        for deg, label in ((40, "回しても"), (90, "長さはそのまま")):
            nxt = self._poly(self._rot(deg))
            narr = self._arrows(self._rot(deg))
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            self.play(
                Transform(self.shape, nxt),
                Transform(self.arr, narr),
                Transform(self.note, cap),
                run_time=1.7,
            )
            self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"Q^{\mathsf T}Q=I").scale(1.15)
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
