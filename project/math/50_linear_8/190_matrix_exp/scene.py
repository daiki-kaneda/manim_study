from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class MatrixExponential(PacedScene):
    """#190 行列指数は流れを時刻 t まで進める（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 1.2
        self.show_heading("行列の指数関数")
        self.draw_flow()
        self.advance()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_flow(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 5.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.5, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        # start vector
        self.v0 = np.array([2.2, 0.6])
        self.arr = Arrow(self.origin, self._pt(self.v0), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.arr), run_time=1.2)
        note = self.ja_text("出発", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def advance(self):
        # rotation-scaling: e^{tA} with A = [[0,-1],[1,0]] scaled + slight growth
        path_dots = VGroup()
        for t in (0.4, 0.8, 1.2, 1.6):
            c, s = np.cos(t), np.sin(t)
            scale = 1.0 + 0.18 * t
            v = scale * np.array([c * self.v0[0] - s * self.v0[1], s * self.v0[0] + c * self.v0[1]])
            path_dots.add(Dot(self._pt(v), radius=0.05, color=GREY_B))
        self.play(LaggedStart(*[FadeIn(d) for d in path_dots], lag_ratio=0.15), run_time=1.2)
        c, s = np.cos(1.6), np.sin(1.6)
        scale = 1.0 + 0.18 * 1.6
        v = scale * np.array([c * self.v0[0] - s * self.v0[1], s * self.v0[0] + c * self.v0[1]])
        new = Arrow(self.origin, self._pt(v), buff=0, color=BLUE, stroke_width=5)
        cap = self.ja_text("時刻 t", font_size=24).move_to(self.note)
        self.play(Transform(self.arr, new), Transform(self.note, cap), run_time=1.7)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"e^{tA}=\sum_{k=0}^{\infty}\frac{(tA)^k}{k!}").scale(0.82)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
