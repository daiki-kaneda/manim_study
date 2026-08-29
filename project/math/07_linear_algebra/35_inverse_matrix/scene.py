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


class InverseMatrix(JapaneseScene):
    """#35 逆行列はもとに戻す写像（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 1.15
        self.unit = 1.5
        self.A = [[2.0, 1.0], [0.0, 1.0]]
        self.Ainv = [[0.5, -0.5], [0.0, 1.0]]
        self.show_heading("逆行列")
        self.draw_square()
        self.there_and_back()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _poly(self, mat, color, opacity=0.4):
        corners = [(0, 0), (1, 0), (1, 1), (0, 1)]
        if mat is not None:
            corners = [apply_2d(mat, c)[:2] for c in corners]
        return Polygon(*[self._pt(c) for c in corners], color=color, fill_opacity=opacity, stroke_width=2)

    def draw_square(self):
        axes_x = Line(self.origin + LEFT * 0.25, self.origin + RIGHT * 4.5, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.25, self.origin + UP * 2.5, color=GREY, stroke_width=2)
        self.sq = self._poly(None, BLUE)
        self.play(Create(axes_x), Create(axes_y), FadeIn(self.sq), run_time=0.7)
        cap = self.ja_text("A で送る", font_size=26).to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(cap), run_time=0.35)
        self.hold(0.45)
        self.cap = cap

    def there_and_back(self):
        para = self._poly(self.A, YELLOW)
        self.play(Transform(self.sq, para), run_time=1.0)
        self.hold(0.5)
        back = self.ja_text("A の逆で戻す", font_size=26).move_to(self.cap)
        self.play(Transform(self.cap, back), run_time=0.4)
        restored = self._poly(None, BLUE)
        self.play(Transform(self.sq, restored), run_time=1.0)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"A^{-1}A=I").scale(1.25)
        formula.to_edge(DOWN, buff=0.4)
        note = self.ja_text("もとの正方形に戻る", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(note), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
