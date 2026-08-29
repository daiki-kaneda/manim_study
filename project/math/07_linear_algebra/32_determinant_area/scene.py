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


class DeterminantArea(JapaneseScene):
    """#32 行列式＝面積の倍率（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.7 + DOWN * 1.2
        self.unit = 1.5
        self.M = [[2.0, 1.0], [0.0, 1.0]]
        self.show_heading("行列式")
        self.show_unit_area()
        self.show_image_area()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _poly(self, corners, color, opacity=0.4):
        pts = [self._pt(c) for c in corners]
        return Polygon(*pts, color=color, fill_opacity=opacity, stroke_width=2)

    def show_unit_area(self):
        axes_x = Line(self.origin + LEFT * 0.25, self.origin + RIGHT * 4.5, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.25, self.origin + UP * 2.5, color=GREY, stroke_width=2)
        sq = self._poly([(0, 0), (1, 0), (1, 1), (0, 1)], BLUE)
        self.play(Create(axes_x), Create(axes_y), FadeIn(sq), run_time=0.8)
        lab = MathTex("1", font_size=36).move_to(self._pt((0.5, 0.5)))
        cap = self.ja_text("面積 1", font_size=26).to_edge(RIGHT, buff=0.5).shift(UP * 1.6)
        self.play(FadeIn(lab), FadeIn(cap), run_time=0.5)
        self.hold(0.7)
        self.sq, self.lab, self.cap = sq, lab, cap

    def show_image_area(self):
        corners = [apply_2d(self.M, c)[:2] for c in [(0, 0), (1, 0), (1, 1), (0, 1)]]
        para = self._poly(corners, YELLOW, opacity=0.45)
        self.play(Transform(self.sq, para), run_time=1.1)
        new_lab = MathTex("2", font_size=40).move_to(self._pt((1.5, 0.5)))
        new_cap = self.ja_text("面積が 2 倍", font_size=26).move_to(self.cap)
        self.play(Transform(self.lab, new_lab), Transform(self.cap, new_cap), run_time=0.5)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"|\det A|=").scale(1.05)
        val = MathTex("2", font_size=44)
        row = VGroup(formula, val).arrange(RIGHT, buff=0.15)
        row.to_edge(DOWN, buff=0.38)
        note = self.ja_text("平行四辺形の面積", font_size=24)
        note.next_to(row, UP, buff=0.2)
        self.play(Write(row), FadeIn(note), run_time=1.0)
        self.play(Indicate(val, color=YELLOW), run_time=0.7)
        self.hold(1.2)
