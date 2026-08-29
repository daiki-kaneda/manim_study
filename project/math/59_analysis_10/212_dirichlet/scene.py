from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class DirichletPrinciple(PacedScene):
    """#212 ディリクレ：調和はエネルギーの最小（約45秒）"""

    def construct(self):
        self.show_heading("ディリクレ原理")
        self.draw_boundary()
        self.smooth_inside()
        self.show_formula()
        self.read(1.4)

    def draw_boundary(self):
        self.axes = Axes(
            x_range=[0, 3.4, 1],
            y_range=[0, 2.2, 1],
            x_length=7.6,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.25)
        # boundary values at ends
        left = Dot(self.axes.c2p(0.2, 1.6), color=YELLOW, radius=0.1)
        right = Dot(self.axes.c2p(3.2, 0.55), color=YELLOW, radius=0.1)
        self.play(Create(self.axes), run_time=0.8)
        self.play(FadeIn(left), FadeIn(right), run_time=0.8)
        note = self.ja_text("境界値", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def smooth_inside(self):
        rough = self.axes.plot(
            lambda x: 1.6 + (0.55 - 1.6) * (x - 0.2) / 3.0 + 0.35 * math.sin(6 * x),
            x_range=[0.2, 3.2],
            color=RED,
            stroke_width=4,
        )
        cap = self.ja_text("凸凹", font_size=24).move_to(self.note)
        self.play(Create(rough), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        smooth = self.axes.plot(
            lambda x: 1.6 + (0.55 - 1.6) * (x - 0.2) / 3.0,
            x_range=[0.2, 3.2],
            color=TEAL,
            stroke_width=5,
        )
        cap2 = self.ja_text("なだらか＝最小", font_size=24).move_to(self.note)
        self.play(Transform(rough, smooth), Transform(self.note, cap2), run_time=1.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"E[u]=\int|\nabla u|^2\to\min").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
