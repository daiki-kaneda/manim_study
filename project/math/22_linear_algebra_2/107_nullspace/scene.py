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


class NullSpace(JapaneseScene):
    """#107 核は 0 に潰れる向き（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 1.2
        self.unit = 1.5
        self.M = [[1.6, 0.0], [0.0, 0.0]]
        self.show_heading("核")
        self.draw_square()
        self.squash()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _poly(self, mat=None):
        corners = [(0, 0), (1.2, 0), (1.2, 1.2), (0, 1.2)]
        if mat is not None:
            corners = [apply_2d(mat, c)[:2] for c in corners]
        return Polygon(*[self._pt(c) for c in corners], color=BLUE, fill_opacity=0.4, stroke_width=2)

    def draw_square(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 4.2, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.2, color=GREY, stroke_width=2)
        self.sq = self._poly()
        v = Arrow(self._pt((0.3, 0.15)), self._pt((0.3, 1.05)), buff=0, color=YELLOW, stroke_width=4)
        self.play(Create(ax), Create(ay), FadeIn(self.sq), GrowArrow(v), run_time=0.8)
        self.v = v
        note = self.ja_text("この向き", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.45)
        self.note = note

    def squash(self):
        flat = self._poly(self.M)
        v2 = Arrow(self._pt((0.3, 0)), self._pt((0.3, 0.02)), buff=0, color=YELLOW, stroke_width=4)
        # 潰れたあとは点
        dot = Dot(self._pt((0.3, 0)), color=YELLOW, radius=0.08)
        self.play(Transform(self.sq, flat), Transform(self.v, dot), run_time=0.95)
        cap = self.ja_text("0 に潰れる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"\ker A=\{x:Ax=0\}").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
