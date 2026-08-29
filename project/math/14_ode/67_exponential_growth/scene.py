from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class ExponentialGrowth(JapaneseScene):
    """#67 指数成長 y'=ky（約90秒）"""

    def construct(self):
        self.show_heading("指数成長")
        self.draw_family()
        self.show_formula()
        self.hold(1.2)

    def draw_family(self):
        self.axes = Axes(
            x_range=[0, 3.2, 1],
            y_range=[0, 5.2, 1],
            x_length=7.0,
            y_length=3.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 0.7 + DOWN * 0.2)
        self.play(Create(self.axes), run_time=0.5)
        k = 0.7
        colors = [BLUE, GREEN, ORANGE]
        y0s = [0.35, 0.55, 0.85]
        for y0, color in zip(y0s, colors):
            curve = self.axes.plot(
                lambda x, a=y0: a * math.exp(k * x),
                x_range=[0, 2.15],
                color=color,
                stroke_width=4,
            )
            self.play(Create(curve), run_time=0.55)
            self.hold(0.25)
        note = self.ja_text("初期値だけ違う", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.6)

    def show_formula(self):
        formula = MathTex(r"y=y_0 e^{kt}").scale(1.2)
        formula.to_edge(DOWN, buff=0.38)
        note = MathTex(r"y'=ky", font_size=32).next_to(formula, UP, buff=0.2)
        self.play(Write(formula), FadeIn(note), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
