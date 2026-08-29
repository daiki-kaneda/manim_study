from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class SlopeField(JapaneseScene):
    """#66 傾き場（約90秒）"""

    def construct(self):
        self.show_heading("傾き場")
        self.draw_field()
        self.overlay_solution()
        self.show_formula()
        self.hold(1.2)

    def draw_field(self):
        self.axes = Axes(
            x_range=[-2.4, 2.4, 1],
            y_range=[-1.6, 1.6, 1],
            x_length=7.4,
            y_length=3.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        self.play(Create(self.axes), run_time=0.5)
        dashes = VGroup()
        for x in np.linspace(-2.1, 2.1, 9):
            for y in np.linspace(-1.35, 1.35, 7):
                slope = 0.55 * y
                ang = np.arctan(slope)
                p = self.axes.c2p(x, y)
                half = 0.16
                d = Line(
                    p + np.array([-half * np.cos(ang), -half * np.sin(ang), 0]),
                    p + np.array([half * np.cos(ang), half * np.sin(ang), 0]),
                    color=BLUE,
                    stroke_width=2,
                )
                dashes.add(d)
        self.play(LaggedStart(*[Create(d) for d in dashes], lag_ratio=0.012), run_time=1.4)
        note = self.ja_text("その点での傾き", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.5)
        self.note = note

    def overlay_solution(self):
        curve = self.axes.plot(lambda x: 0.7 * np.exp(0.55 * x), x_range=[-2.1, 1.15], color=YELLOW, stroke_width=5)
        self.play(Create(curve), run_time=0.9)
        cap = self.ja_text("解の曲線", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"y'=ky").scale(1.2)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=0.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
