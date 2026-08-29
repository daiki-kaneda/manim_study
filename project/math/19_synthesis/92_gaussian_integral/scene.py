from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class GaussianIntegral(JapaneseScene):
    """#92 ガウス積分（約90秒）"""

    def construct(self):
        self.show_heading("ガウス積分")
        self.draw_curve()
        self.fill_area()
        self.show_formula()
        self.hold(1.2)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-2.8, 2.8, 1],
            y_range=[0, 1.25, 1],
            x_length=8.4,
            y_length=3.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2)
        self.curve = self.axes.plot(
            lambda x: math.exp(-x * x),
            x_range=[-2.6, 2.6],
            color=BLUE,
            stroke_width=5,
        )
        lab = MathTex(r"e^{-x^2}", color=BLUE, font_size=32)
        lab.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(Create(self.axes), run_time=0.45)
        self.play(Create(self.curve), FadeIn(lab), run_time=0.85)
        self.hold(0.4)
        self.lab = lab

    def fill_area(self):
        area = self.axes.get_area(self.curve, x_range=[-2.6, 2.6], color=YELLOW, opacity=0.4)
        self.play(FadeIn(area), run_time=0.8)
        cap = self.ja_text("面積は √π", font_size=24).move_to(self.lab)
        self.play(Transform(self.lab, cap), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt{\pi}").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
