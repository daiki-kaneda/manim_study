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


class Conformal(JapaneseScene):
    """#75 等角写像：直角が保たれる（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 0.4
        self.s = 1.15
        self.show_heading("等角写像")
        self.draw_grid()
        self.rotate()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.s, xy[1] * self.s, 0.0])

    def _square(self, mat=None):
        corners = [(0, 0), (1, 0), (1, 1), (0, 1)]
        if mat is not None:
            corners = [apply_2d(mat, c)[:2] for c in corners]
        return Polygon(*[self._pt(c) for c in corners], color=BLUE, fill_opacity=0.4, stroke_width=2)

    def draw_grid(self):
        axes_x = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 3.8, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.3, self.origin + UP * 2.8, color=GREY, stroke_width=2)
        sq = self._square()
        # 直角マーク
        mark = RightAngle(Line(self._pt((0, 0)), self._pt((1, 0))), Line(self._pt((0, 0)), self._pt((0, 1))), length=0.22, color=YELLOW)
        self.play(Create(axes_x), Create(axes_y), FadeIn(sq), Create(mark), run_time=0.85)
        note = self.ja_text("直角", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.55)
        self.sq, self.mark, self.note = sq, mark, note

    def rotate(self):
        # 乗法 i：90° 回転
        M = [[0.0, -1.0], [1.0, 0.0]]
        nxt = self._square(M)
        mark2 = RightAngle(
            Line(self._pt((0, 0)), self._pt(apply_2d(M, (1, 0))[:2])),
            Line(self._pt((0, 0)), self._pt(apply_2d(M, (0, 1))[:2])),
            length=0.22,
            color=YELLOW,
        )
        self.play(Transform(self.sq, nxt), Transform(self.mark, mark2), run_time=1.1)
        cap = self.ja_text("直角のまま", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"f(z)=iz").scale(1.15)
        formula.to_edge(DOWN, buff=0.4)
        note = self.ja_text("正則なら角度を保つ", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(note), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
