from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class LaplaceTransform(PacedScene):
    """#223 ラプラスは減衰つきの積分変換（約45秒）"""

    def construct(self):
        self.show_heading("ラプラス変換")
        self.draw_time()
        self.dampen()
        self.show_formula()
        self.read(1.4)

    def draw_time(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[-0.2, 1.4, 1],
            x_length=7.8,
            y_length=2.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.35 + LEFT * 0.2)
        self.f = self.axes.plot(
            lambda t: math.exp(-0.15 * t) * math.cos(3.2 * t) ** 2 + 0.15,
            x_range=[0.05, 5.0],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.f), run_time=1.5)
        note = self.ja_text("時間側", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def dampen(self):
        damp = self.axes.plot(
            lambda t: math.exp(-0.85 * t) * (math.exp(-0.15 * t) * math.cos(3.2 * t) ** 2 + 0.15),
            x_range=[0.05, 5.0],
            color=ORANGE,
            stroke_width=4,
        )
        cap = self.ja_text("減衰して掛ける", font_size=24).move_to(self.note)
        self.play(Create(damp), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        area = self.axes.get_area(damp, x_range=[0.05, 5.0], color=YELLOW, opacity=0.35)
        cap2 = self.ja_text("積分", font_size=24).move_to(self.note)
        self.play(FadeIn(area), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"F(s)=\int_0^{\infty}e^{-st}f(t)\,dt").scale(0.85)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
