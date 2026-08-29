from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


def _taylor_sin(x: float, n_terms: int) -> float:
    total = 0.0
    sign = 1.0
    for k in range(n_terms):
        odd = 2 * k + 1
        total += sign * (x ** odd) / math.factorial(odd)
        sign *= -1.0
    return total


class TaylorSin(JapaneseScene):
    """#24 sin のテイラー展開（約90秒）"""

    def construct(self):
        self.show_heading("テイラー展開")
        self.draw_sine()
        self.add_polynomials()
        self.show_formula()
        self.hold(1.2)

    def draw_sine(self):
        self.axes = Axes(
            x_range=[-3.4, 3.4, 1],
            y_range=[-2.0, 2.0, 1],
            x_length=8.4,
            y_length=4.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.25)
        sine = self.axes.plot(lambda x: math.sin(x), x_range=[-3.3, 3.3], color=BLUE, stroke_width=5)
        sine_lab = MathTex(r"\sin x", color=BLUE, font_size=32)
        sine_lab.to_edge(RIGHT, buff=0.45).shift(UP * 1.7)
        self.play(Create(self.axes), run_time=0.6)
        self.play(Create(sine), FadeIn(sine_lab), run_time=0.9)
        self.hold(0.5)
        self.sine_lab = sine_lab

    def add_polynomials(self):
        specs = [
            (1, ORANGE, r"x"),
            (2, GREEN, r"x-\dfrac{x^3}{3!}"),
            (3, YELLOW, r"x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}"),
        ]
        current = None
        poly_lab = None
        for n_terms, color, tex in specs:
            graph = self.axes.plot(
                lambda x, n=n_terms: _taylor_sin(x, n),
                x_range=[-3.1, 3.1],
                color=color,
                stroke_width=4,
            )
            lab = MathTex(tex, color=color, font_size=30)
            lab.next_to(self.sine_lab, DOWN, aligned_edge=RIGHT, buff=0.3)
            if current is None:
                self.play(Create(graph), FadeIn(lab), run_time=0.8)
                current = graph
                poly_lab = lab
            else:
                self.play(Transform(current, graph), Transform(poly_lab, lab), run_time=0.85)
            self.hold(0.7)
        self.poly = current
        self.poly_lab = poly_lab

    def show_formula(self):
        formula = MathTex(r"\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.1)
        note = self.ja_text("項を足すほど sin に近づく", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(FadeIn(note), run_time=0.4)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
