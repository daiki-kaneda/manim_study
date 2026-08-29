from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class LinearSuperposition(JapaneseScene):
    """#70 線形なら解の和も解（約90秒）"""

    def construct(self):
        self.show_heading("重ね合わせ")
        self.draw_two()
        self.add_them()
        self.show_formula()
        self.hold(1.2)

    def draw_two(self):
        self.axes = Axes(
            x_range=[0, 6.4, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=8.4,
            y_length=3.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        self.play(Create(self.axes), run_time=0.5)
        y1 = self.axes.plot(lambda x: math.cos(x), x_range=[0, 6.2], color=BLUE, stroke_width=3)
        y2 = self.axes.plot(lambda x: 0.55 * math.sin(x), x_range=[0, 6.2], color=GREEN, stroke_width=3)
        l1 = MathTex(r"y_1", color=BLUE, font_size=28).to_edge(RIGHT, buff=0.45).shift(UP * 1.7)
        l2 = MathTex(r"y_2", color=GREEN, font_size=28).next_to(l1, DOWN, aligned_edge=RIGHT, buff=0.2)
        self.play(Create(y1), FadeIn(l1), run_time=0.65)
        self.hold(0.35)
        self.play(Create(y2), FadeIn(l2), run_time=0.65)
        self.hold(0.5)
        self.l2 = l2

    def add_them(self):
        ysum = self.axes.plot(
            lambda x: math.cos(x) + 0.55 * math.sin(x),
            x_range=[0, 6.2],
            color=YELLOW,
            stroke_width=5,
        )
        lab = MathTex(r"y_1+y_2", color=YELLOW, font_size=28).next_to(self.l2, DOWN, aligned_edge=RIGHT, buff=0.2)
        self.play(Create(ysum), FadeIn(lab), run_time=0.85)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"L[y_1]=0,\; L[y_2]=0 \;\Rightarrow\; L[y_1+y_2]=0").scale(0.8)
        formula.to_edge(DOWN, buff=0.32)
        note = self.ja_text("線形のとき", font_size=24)
        note.next_to(formula, UP, buff=0.16)
        self.play(Write(formula), FadeIn(note), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
