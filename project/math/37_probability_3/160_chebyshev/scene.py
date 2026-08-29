from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class Chebyshev(PacedScene):
    """#160 チェビシェフの不等式（約50秒）"""

    def construct(self):
        self.show_heading("チェビシェフ")
        self.draw_blob()
        self.widen_band()
        self.show_formula()
        self.read(1.4)

    def draw_blob(self):
        self.axes = Axes(
            x_range=[-4.2, 4.2, 1],
            y_range=[0, 1.15, 1],
            x_length=9.0,
            y_length=2.7,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.05)
        self.curve = self.axes.plot(
            lambda x: 0.95 * math.exp(-0.5 * ((x + 0.35) ** 2) / 1.15) + 0.12 * math.exp(-0.5 * ((x - 1.6) ** 2) / 0.35),
            x_range=[-3.8, 3.8],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), run_time=2.0)
        mu = self.axes.c2p(0.15, 0)
        self.mean = DashedLine(mu + UP * 0.05, self.axes.c2p(0.15, 1.05), color=YELLOW, stroke_width=3)
        self.play(Create(self.mean), run_time=0.8)
        note = self.ja_text("平均", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.4)
        self.note = note

    def _band(self, k, color=ORANGE):
        left = self.axes.c2p(-k * 1.05, 0)
        right = self.axes.c2p(k * 1.05, 0)
        height = abs(self.axes.c2p(0, 1.05)[1] - self.axes.c2p(0, 0)[1])
        rect = Rectangle(
            width=abs(right[0] - left[0]),
            height=height,
            color=color,
            fill_opacity=0.18,
            stroke_width=2,
        )
        rect.move_to([(left[0] + right[0]) / 2, (self.axes.c2p(0, 0)[1] + self.axes.c2p(0, 1.05)[1]) / 2, 0])
        return rect

    def widen_band(self):
        band = self._band(1.0)
        cap = self.ja_text("幅 kσ", font_size=24).move_to(self.note)
        self.play(FadeIn(band), Transform(self.note, cap), run_time=1.3)
        self.read(0.4)
        band2 = self._band(2.0, color=TEAL)
        cap2 = self.ja_text("外は少ない", font_size=24).move_to(self.note)
        self.play(Transform(band, band2), Transform(self.note, cap2), run_time=1.6)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"P(|X-\mu|\ge k\sigma)\le\frac{1}{k^{2}}").scale(0.82)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
