from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class LogisticGrowth(JapaneseScene):
    """#69 ロジスティック成長（約90秒）"""

    def construct(self):
        self.show_heading("ロジスティック")
        self.draw_curves()
        self.show_formula()
        self.hold(1.2)

    def draw_curves(self):
        self.axes = Axes(
            x_range=[0, 6.2, 1],
            y_range=[0, 2.4, 1],
            x_length=7.4,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 0.55 + DOWN * 0.2)
        self.play(Create(self.axes), run_time=0.5)
        expo = self.axes.plot(lambda x: 0.22 * math.exp(0.7 * x), x_range=[0, 3.4], color=GREY, stroke_width=3)
        k_line = DashedLine(self.axes.c2p(0, 1.8), self.axes.c2p(6.0, 1.8), color=YELLOW, stroke_width=2)
        k_lab = MathTex("K", color=YELLOW, font_size=30).next_to(k_line, RIGHT, buff=0.1)

        def logistic(x):
            return 1.8 / (1 + 7.5 * math.exp(-1.15 * x))

        logi = self.axes.plot(lambda x: logistic(x), x_range=[0, 6.0], color=BLUE, stroke_width=5)
        self.play(Create(expo), run_time=0.7)
        exp_lab = self.ja_text("指数のまま", font_size=22).to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(FadeIn(exp_lab), run_time=0.3)
        self.hold(0.45)
        self.play(Create(k_line), FadeIn(k_lab), run_time=0.45)
        self.play(Create(logi), Transform(exp_lab, self.ja_text("上限に頭打ち", font_size=22).move_to(exp_lab)), run_time=0.85)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"y'=ry\left(1-\frac{y}{K}\right)").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
