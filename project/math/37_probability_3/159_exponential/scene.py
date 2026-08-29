from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class ExponentialDist(PacedScene):
    """#159 指数分布は待ち時間（約50秒）"""

    def construct(self):
        self.show_heading("指数分布")
        self.draw_curve()
        self.mark_tail()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 1.15, 1],
            x_length=8.0,
            y_length=3.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.25)
        self.graph = self.axes.plot(
            lambda x: math.exp(-0.85 * x),
            x_range=[0.02, 4.9],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.9)
        self.play(Create(self.graph), run_time=2.0)
        note = self.ja_text("待ち時間", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note

    def mark_tail(self):
        area1 = self.axes.get_area(self.graph, x_range=[0.9, 4.7], color=YELLOW, opacity=0.4)
        cap = self.ja_text("まだ先", font_size=24).move_to(self.note)
        self.play(FadeIn(area1), Transform(self.note, cap), run_time=1.4)
        self.read(0.4)
        area2 = self.axes.get_area(self.graph, x_range=[2.2, 4.7], color=ORANGE, opacity=0.45)
        cap2 = self.ja_text("形は同じ", font_size=24).move_to(self.note)
        self.play(FadeIn(area2), Transform(self.note, cap2), run_time=1.5)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"f(x)=\lambda e^{-\lambda x}\quad(x\ge 0)").scale(0.88)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
