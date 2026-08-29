from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class MeanValue(JapaneseScene):
    """#111 平均値の定理（約90秒）"""

    def construct(self):
        self.show_heading("平均値の定理")
        self.draw_curve()
        self.secant_and_tangent()
        self.show_formula()
        self.hold(1.2)

    def _f(self, x):
        return 0.32 * x * x + 0.45

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 4.4, 1],
            y_range=[0, 4.2, 1],
            x_length=7.4,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.5)
        curve = self.axes.plot(lambda x: 0.32 * x * x + 0.45, x_range=[0.3, 3.6], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.45)
        self.play(Create(curve), run_time=0.75)
        self.hold(0.3)

    def _line_through(self, x1, x2, color=ORANGE, half=2.2):
        p1 = np.array(self.axes.c2p(x1, self._f(x1)))
        p2 = np.array(self.axes.c2p(x2, self._f(x2)))
        d = p2 - p1
        d = d / np.linalg.norm(d)
        mid = (p1 + p2) / 2
        return Line(mid - d * half, mid + d * half, color=color, stroke_width=5)

    def secant_and_tangent(self):
        a, b = 0.8, 3.2
        sec = self._line_through(a, b)
        da = Dot(self.axes.c2p(a, self._f(a)), color=ORANGE, radius=0.07)
        db = Dot(self.axes.c2p(b, self._f(b)), color=ORANGE, radius=0.07)
        note = self.ja_text("割線", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(Create(sec), FadeIn(da), FadeIn(db), FadeIn(note), run_time=0.7)
        self.hold(0.45)
        c = (a + b) / 2
        tan = self._line_through(c - 0.08, c + 0.08, color=YELLOW, half=2.2)
        dc = Dot(self.axes.c2p(c, self._f(c)), color=YELLOW, radius=0.08)
        self.play(Create(tan), FadeIn(dc), run_time=0.7)
        cap = self.ja_text("同じ傾き", font_size=24).move_to(note)
        self.play(Transform(note, cap), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"f'(c)=\dfrac{f(b)-f(a)}{b-a}").scale(0.95)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
