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


class ImageSpace(JapaneseScene):
    """#106 像は列が張る面（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.25
        self.unit = 1.45
        self.M = [[1.7, 0.7], [0.25, 1.35]]
        self.show_heading("像")
        self.draw_square()
        self.apply_map()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _poly(self, mat=None):
        corners = [(0, 0), (1, 0), (1, 1), (0, 1)]
        if mat is not None:
            corners = [apply_2d(mat, c)[:2] for c in corners]
        return Polygon(*[self._pt(c) for c in corners], color=BLUE, fill_opacity=0.4, stroke_width=2)

    def draw_square(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 4.4, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.3, color=GREY, stroke_width=2)
        self.sq = self._poly()
        self.play(Create(ax), Create(ay), FadeIn(self.sq), run_time=0.7)
        note = self.ja_text("定義域", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.4)
        self.note = note

    def apply_map(self):
        img = self._poly(self.M)
        self.play(Transform(self.sq, img), run_time=0.9)
        cap = self.ja_text("列が張る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"\mathrm{Im}\,A=\{Ax:x\in\mathbb{R}^n\}").scale(0.9)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
