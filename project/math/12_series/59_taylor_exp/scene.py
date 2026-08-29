from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


def _taylor_exp(x: float, n_terms: int) -> float:
    total = 0.0
    term = 1.0
    for k in range(n_terms):
        total += term
        term *= x / (k + 1)
    return total


class TaylorExp(JapaneseScene):
    """#59 e^x のテイラー展開（約90秒）"""

    def construct(self):
        self.show_heading("e^x の展開")
        self.draw_exp()
        self.add_polynomials()
        self.show_formula()
        self.hold(1.2)

    def draw_exp(self):
        self.axes = Axes(
            x_range=[-1.2, 2.4, 1],
            y_range=[0, 7.5, 1],
            x_length=7.2,
            y_length=4.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.6)
        curve = self.axes.plot(lambda x: math.exp(x), x_range=[-1.1, 2.1], color=BLUE, stroke_width=5)
        lab = MathTex(r"e^x", color=BLUE, font_size=32).to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(Create(self.axes), run_time=0.5)
        self.play(Create(curve), FadeIn(lab), run_time=0.85)
        self.hold(0.4)
        self.lab = lab

    def add_polynomials(self):
        specs = [
            (2, ORANGE, r"1+x"),
            (3, GREEN, r"1+x+\dfrac{x^2}{2}"),
            (4, YELLOW, r"1+x+\dfrac{x^2}{2}+\dfrac{x^3}{6}"),
        ]
        current = None
        poly_lab = None
        for n, color, tex in specs:
            graph = self.axes.plot(
                lambda x, k=n: _taylor_exp(x, k),
                x_range=[-1.1, 2.05],
                color=color,
                stroke_width=4,
            )
            lab = MathTex(tex, color=color, font_size=28)
            lab.next_to(self.lab, DOWN, aligned_edge=RIGHT, buff=0.28)
            if current is None:
                self.play(Create(graph), FadeIn(lab), run_time=0.75)
                current, poly_lab = graph, lab
            else:
                self.play(Transform(current, graph), Transform(poly_lab, lab), run_time=0.8)
            self.hold(0.55)

    def show_formula(self):
        formula = MathTex(r"e^x=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots").scale(0.9)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
