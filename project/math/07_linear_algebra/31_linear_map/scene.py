from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import apply_2d


class LinearMap(JapaneseScene):
    """#31 行列は線形変換（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 1.15
        self.unit = 1.55
        self.M = [[2.0, 1.0], [0.0, 1.0]]
        self.show_heading("線形変換")
        self.draw_square()
        self.apply_map()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _square(self, mat=None):
        corners = [(0, 0), (1, 0), (1, 1), (0, 1)]
        if mat is not None:
            corners = [apply_2d(mat, c)[:2] for c in corners]
        pts = [self._pt(c) for c in corners]
        return Polygon(*pts, color=BLUE, fill_opacity=0.35, stroke_width=2)

    def _basis(self, mat=None, colors=(YELLOW, GREEN)):
        e1, e2 = (1, 0), (0, 1)
        if mat is not None:
            e1, e2 = apply_2d(mat, e1)[:2], apply_2d(mat, e2)[:2]
        a1 = Arrow(self.origin, self._pt(e1), buff=0, color=colors[0], stroke_width=4)
        a2 = Arrow(self.origin, self._pt(e2), buff=0, color=colors[1], stroke_width=4)
        return a1, a2

    def draw_square(self):
        axes_x = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 4.4, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.3, self.origin + UP * 2.6, color=GREY, stroke_width=2)
        sq = self._square()
        a1, a2 = self._basis()
        l1 = MathTex(r"e_1", color=YELLOW, font_size=30).next_to(a1.get_end(), DOWN, buff=0.1)
        l2 = MathTex(r"e_2", color=GREEN, font_size=30).next_to(a2.get_end(), LEFT, buff=0.1)
        self.play(Create(axes_x), Create(axes_y), run_time=0.5)
        self.play(FadeIn(sq), GrowArrow(a1), GrowArrow(a2), FadeIn(l1), FadeIn(l2), run_time=0.8)
        note = self.ja_text("単位正方形", font_size=26).to_edge(RIGHT, buff=0.45).shift(UP * 1.6)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.6)
        self.sq, self.a1, self.a2, self.l1, self.l2, self.note = sq, a1, a2, l1, l2, note

    def apply_map(self):
        nxt = self._square(self.M)
        n1, n2 = self._basis(self.M)
        nl1 = MathTex(r"Ae_1", color=YELLOW, font_size=30).next_to(n1.get_end(), DOWN, buff=0.1)
        nl2 = MathTex(r"Ae_2", color=GREEN, font_size=30).next_to(n2.get_end(), LEFT, buff=0.08)
        self.play(
            Transform(self.sq, nxt),
            Transform(self.a1, n1),
            Transform(self.a2, n2),
            Transform(self.l1, nl1),
            Transform(self.l2, nl2),
            run_time=1.2,
        )
        mapped = self.ja_text("列ベクトルが基底の行き先", font_size=24).move_to(self.note)
        self.play(Transform(self.note, mapped), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"A=\begin{bmatrix}2&1\\0&1\end{bmatrix}").scale(1.05)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
