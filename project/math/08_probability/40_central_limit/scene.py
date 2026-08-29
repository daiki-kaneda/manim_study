from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class CentralLimit(JapaneseScene):
    """#40 中心極限定理（約90秒）"""

    def construct(self):
        self.show_heading("中心極限定理")
        self.draw_axes()
        self.evolve()
        self.show_formula()
        self.hold(1.2)

    def draw_axes(self):
        self.axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[0, 0.7, 0.2],
            x_length=8.6,
            y_length=3.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2)
        self.play(Create(self.axes), run_time=0.55)
        self.hold(0.3)

    def evolve(self):
        # 一様 → 三角（2つの和） → 正規に近い
        uniform = self.axes.plot(
            lambda x: 0.35 if abs(x) < 1.4 else 0.0,
            x_range=[-2.9, 2.9],
            color=BLUE,
            stroke_width=4,
            use_smoothing=False,
        )
        lab = self.ja_text("1回分（一様）", font_size=24).to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(Create(uniform), FadeIn(lab), run_time=0.8)
        self.hold(0.55)

        def tri(x):
            a = abs(x)
            if a >= 2.0:
                return 0.0
            return 0.45 * (1 - a / 2.0)

        triangular = self.axes.plot(lambda x: tri(x), x_range=[-2.9, 2.9], color=ORANGE, stroke_width=4)
        lab2 = self.ja_text("2回足す", font_size=24).move_to(lab)
        self.play(Transform(uniform, triangular), Transform(lab, lab2), run_time=0.9)
        self.hold(0.55)

        gauss = self.axes.plot(
            lambda x: 0.52 * math.exp(-0.5 * x * x),
            x_range=[-2.9, 2.9],
            color=YELLOW,
            stroke_width=5,
        )
        lab3 = self.ja_text("何度も足すと釣鐘", font_size=24).move_to(lab)
        self.play(Transform(uniform, gauss), Transform(lab, lab3), run_time=0.95)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"S_n \approx \mathrm{Normal}").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
