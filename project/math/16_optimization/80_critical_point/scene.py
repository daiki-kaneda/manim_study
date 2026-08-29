from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class CriticalPoint(JapaneseScene):
    """#80 極値は接線が水平（約90秒）"""

    def construct(self):
        self.show_heading("極値")
        self.draw_curve()
        self.move_tangent()
        self.show_formula()
        self.hold(1.2)

    def _f(self, x):
        return 0.45 * (x - 0.8) ** 2 + 0.55

    def _fp(self, x):
        return 0.9 * (x - 0.8)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-1.6, 3.2, 1],
            y_range=[0, 4.0, 1],
            x_length=7.4,
            y_length=3.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.45)
        curve = self.axes.plot(lambda x: 0.45 * (x - 0.8) ** 2 + 0.55, x_range=[-1.4, 3.0], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.5)
        self.play(Create(curve), run_time=0.8)
        self.hold(0.35)

    def _tangent(self, x, color=ORANGE):
        y = self._f(x)
        m = self._fp(x)
        p = np.array(self.axes.c2p(x, y))
        q = np.array(self.axes.c2p(x + 1.0, y + m))
        direction = q - p
        nrm = np.linalg.norm(direction)
        direction = direction / nrm
        return Line(p - direction * 1.7, p + direction * 1.7, color=color, stroke_width=5), Dot(p, color=color, radius=0.07)

    def move_tangent(self):
        tan, dot = self._tangent(-0.6)
        note = self.ja_text("傾きあり", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(Create(tan), FadeIn(dot), FadeIn(note), run_time=0.7)
        self.hold(0.4)
        for x in (0.05, 0.8):
            nxt, nd = self._tangent(x, color=YELLOW if abs(x - 0.8) < 1e-6 else ORANGE)
            self.play(Transform(tan, nxt), Transform(dot, nd), run_time=0.7)
            self.hold(0.35)
        cap = self.ja_text("接線が水平", font_size=24).move_to(note)
        self.play(Transform(note, cap), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"f'(x)=0").scale(1.25)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=0.85)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
