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


class MatrixComposition(JapaneseScene):
    """#34 行列の積＝写像の合成（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.2
        self.unit = 1.45
        self.B = [[1.0, 0.6], [0.0, 1.0]]
        self.A = [[2.0, 0.0], [0.0, 1.0]]
        self.show_heading("行列の積")
        self.draw_square()
        self.apply_then()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _poly(self, mat, color, opacity=0.4):
        corners = [(0, 0), (1, 0), (1, 1), (0, 1)]
        if mat is not None:
            corners = [apply_2d(mat, c)[:2] for c in corners]
        return Polygon(*[self._pt(c) for c in corners], color=color, fill_opacity=opacity, stroke_width=2)

    def _compose(self, a, b):
        # a @ b
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def draw_square(self):
        axes_x = Line(self.origin + LEFT * 0.25, self.origin + RIGHT * 4.6, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.25, self.origin + UP * 2.5, color=GREY, stroke_width=2)
        self.sq = self._poly(None, BLUE)
        self.play(Create(axes_x), Create(axes_y), FadeIn(self.sq), run_time=0.7)
        step = self.ja_text("まず B", font_size=26).to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(step), run_time=0.35)
        self.hold(0.45)
        self.step = step

    def apply_then(self):
        after_b = self._poly(self.B, ORANGE)
        self.play(Transform(self.sq, after_b), run_time=0.9)
        self.play(Transform(self.step, self.ja_text("つぎに A", font_size=26).move_to(self.step)), run_time=0.35)
        self.hold(0.45)
        ab = self._compose(self.A, self.B)
        after_ab = self._poly(ab, YELLOW)
        self.play(Transform(self.sq, after_ab), run_time=0.9)
        self.play(
            Transform(self.step, self.ja_text("B のあと A", font_size=26).move_to(self.step)),
            run_time=0.35,
        )
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"(AB)x=A(Bx)").scale(1.2)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
