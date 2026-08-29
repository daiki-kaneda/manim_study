from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class ChernoffBound(PacedScene):
    """#219 チェルノフ：尾は指数減衰（約45秒）"""

    def construct(self):
        self.show_heading("チェルノフ界")
        self.draw_mean()
        self.show_tail()
        self.show_formula()
        self.read(1.4)

    def draw_mean(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 1.05, 1],
            x_length=8.0,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.15)
        # binomial-like hump
        self.pdf = self.axes.plot(
            lambda x: math.exp(-0.55 * (x - 2.0) ** 2),
            x_range=[0.1, 5.0],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.pdf), run_time=1.5)
        mean = DashedLine(self.axes.c2p(2.0, 0), self.axes.c2p(2.0, 1.0), color=YELLOW, stroke_width=3)
        note = self.ja_text("平均", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(Create(mean), FadeIn(note), run_time=1.0)
        self.read(0.3)
        self.note = note

    def show_tail(self):
        a = 3.6
        line = DashedLine(self.axes.c2p(a, 0), self.axes.c2p(a, 0.9), color=ORANGE, stroke_width=3)
        tail = self.axes.get_area(self.pdf, x_range=[a, 5.0], color=RED, opacity=0.5)
        cap = self.ja_text("遠い尾", font_size=24).move_to(self.note)
        self.play(Create(line), FadeIn(tail), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        # decaying markers
        marks = VGroup()
        for x, h in ((3.8, 0.35), (4.2, 0.18), (4.6, 0.08)):
            marks.add(Line(self.axes.c2p(x, 0), self.axes.c2p(x, h), color=TEAL, stroke_width=4))
        cap2 = self.ja_text("指数で減少", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(m) for m in marks], lag_ratio=0.2), Transform(self.note, cap2), run_time=1.4)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"P(X\ge(1+\delta)\mu)\le e^{-\mu\delta^{2}/3}").scale(0.78)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
