from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene
import numpy as np


class DerivativeTangent(JapaneseScene):
    """#16 微分＝接線の傾き（約90秒）"""

    def construct(self):
        self.show_heading("微分")
        self.draw_curve()
        self.secant_to_tangent()
        self.show_formula()
        self.hold(1.2)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 5.2, 1],
            x_length=6.2,
            y_length=4.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 1.5 + DOWN * 0.35)
        graph = self.axes.plot(lambda x: 0.28 * x * x + 0.2, x_range=[0.2, 3.8], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), run_time=0.6)
        self.play(Create(graph), run_time=0.9)
        self.hold(0.5)
        self.graph = graph

    def _extended_line(self, x1, x2, color=ORANGE, half_len=2.7):
        def f(x):
            return 0.28 * x * x + 0.2

        p1 = np.array(self.axes.c2p(x1, f(x1)))
        p2 = np.array(self.axes.c2p(x2, f(x2)))
        direction = p2 - p1
        norm = np.linalg.norm(direction)
        if norm < 1e-8:
            return Line(p1, p2, color=color, stroke_width=5)
        direction = direction / norm
        mid = (p1 + p2) / 2.0
        return Line(
            mid - direction * half_len,
            mid + direction * half_len,
            color=color,
            stroke_width=5,
        )

    def secant_to_tangent(self):
        x0 = 1.7
        sec = self._extended_line(x0, x0 + 1.4)
        note = self.ja_text("割線", font_size=26).to_edge(RIGHT, buff=0.6).shift(UP * 1.2)
        self.play(Create(sec), FadeIn(note), run_time=0.7)
        self.hold(0.6)
        for h in (0.8, 0.35):
            nxt = self._extended_line(x0, x0 + h)
            self.play(Transform(sec, nxt), run_time=0.7)
            self.hold(0.4)
        tan = self._extended_line(x0 - 0.05, x0 + 0.05, color=YELLOW)
        self.play(Transform(sec, tan), run_time=0.8)
        tan_note = self.ja_text("接線", font_size=26).move_to(note)
        self.play(Transform(note, tan_note), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(
            r"f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}"
        ).scale(0.8)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.1)
        meaning = self.ja_text("接線の傾き", font_size=26)
        meaning.to_edge(RIGHT, buff=0.55).shift(DOWN * 0.4)
        self.play(FadeIn(meaning), run_time=0.5)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
