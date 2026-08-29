from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


def _square_wave(x: float) -> float:
    s = math.sin(x)
    return 1.0 if s >= 0 else -1.0


def _fourier(x: float, n_odd: int) -> float:
    total = 0.0
    for k in range(n_odd):
        n = 2 * k + 1
        total += math.sin(n * x) / n
    return (4 / math.pi) * total


class FourierSquare(JapaneseScene):
    """#60 フーリエ：矩形波（約90秒）"""

    def construct(self):
        self.show_heading("フーリエ級数")
        self.draw_wave()
        self.add_harmonics()
        self.show_formula()
        self.hold(1.2)

    def draw_wave(self):
        self.axes = Axes(
            x_range=[-0.2, 2 * math.pi + 0.3, 1],
            y_range=[-1.6, 1.6, 1],
            x_length=8.6,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        sq = self.axes.plot(
            lambda x: _square_wave(x),
            x_range=[0.02, 2 * math.pi - 0.02],
            color=GREY,
            stroke_width=3,
            use_smoothing=False,
        )
        lab = self.ja_text("矩形波", font_size=24).to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(Create(self.axes), Create(sq), FadeIn(lab), run_time=0.9)
        self.hold(0.45)
        self.lab = lab

    def add_harmonics(self):
        current = None
        for n_odd, color, jp in (
            (1, BLUE, "1 項目"),
            (2, GREEN, "3 項目まで"),
            (4, YELLOW, "近づく"),
        ):
            graph = self.axes.plot(
                lambda x, n=n_odd: _fourier(x, n),
                x_range=[0.02, 2 * math.pi - 0.02],
                color=color,
                stroke_width=4,
            )
            cap = self.ja_text(jp, font_size=24).move_to(self.lab)
            if current is None:
                self.play(Create(graph), Transform(self.lab, cap), run_time=0.75)
                current = graph
            else:
                self.play(Transform(current, graph), Transform(self.lab, cap), run_time=0.8)
            self.hold(0.5)

    def show_formula(self):
        formula = MathTex(r"\frac{4}{\pi}\left(\sin x+\frac{\sin 3x}{3}+\frac{\sin 5x}{5}+\cdots\right)").scale(0.72)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
