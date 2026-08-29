from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class FourierTransform(PacedScene):
    """#175 フーリエ変換は周波数の重み（約45秒）"""

    def construct(self):
        self.show_heading("フーリエ変換")
        self.draw_signal()
        self.show_spectrum()
        self.show_formula()
        self.read(1.4)

    def draw_signal(self):
        self.axes = Axes(
            x_range=[0, 6.5, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=7.6,
            y_length=2.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 1.05 + LEFT * 0.4)
        self.signal = self.axes.plot(
            lambda x: 0.7 * np.sin(2.2 * x) + 0.35 * np.sin(5.5 * x),
            x_range=[0.1, 6.2],
            color=BLUE,
            stroke_width=4,
        )
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.signal), run_time=2.0)
        note = self.ja_text("時間の波", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def show_spectrum(self):
        sax = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 1.2, 1],
            x_length=7.6,
            y_length=1.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 1.35 + LEFT * 0.4)
        self.play(Create(sax), run_time=0.7)
        bars = VGroup()
        for freq, h, col in ((2.2, 0.95, YELLOW), (5.5, 0.5, ORANGE)):
            x = sax.c2p(freq, 0)
            top = sax.c2p(freq, h)
            bars.add(Line(x, top, color=col, stroke_width=10))
            bars.add(Dot(top, color=col, radius=0.07))
        cap = self.ja_text("周波数", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(b) if isinstance(b, Line) else FadeIn(b) for b in bars], lag_ratio=0.15), Transform(self.note, cap), run_time=1.8)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"\hat f(\xi)=\int_{-\infty}^{\infty}f(x)e^{-2\pi i x\xi}\,dx").scale(0.68)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
