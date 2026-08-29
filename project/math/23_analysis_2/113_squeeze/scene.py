from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class Squeeze(JapaneseScene):
    """#113 はさみうちの原理（約90秒）"""

    def construct(self):
        self.show_heading("はさみうち")
        self.draw_bounds()
        self.show_formula()
        self.hold(1.2)

    def draw_bounds(self):
        self.axes = Axes(
            x_range=[-2.4, 2.4, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=8.0,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        up = self.axes.plot(lambda x: x * x * 0.28, x_range=[-2.2, 2.2], color=ORANGE, stroke_width=4)
        lo = self.axes.plot(lambda x: -x * x * 0.28, x_range=[-2.2, 2.2], color=ORANGE, stroke_width=4)
        mid = self.axes.plot(
            lambda x: 0.28 * x * x * math.sin(8 * x),
            x_range=[-2.2, 2.2],
            color=YELLOW,
            stroke_width=4,
        )
        self.play(Create(self.axes), run_time=0.4)
        self.play(Create(up), Create(lo), run_time=0.7)
        note = self.ja_text("上下ではさむ", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.4)
        self.play(Create(mid), run_time=0.8)
        cap = self.ja_text("真ん中も 0 へ", font_size=24).move_to(note)
        self.play(Transform(note, cap), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"g\le f\le h\ \Rightarrow\ \lim f=L").scale(0.85)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
