from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class WeakConvergence(PacedScene):
    """#260 弱い収束は積分で測る（約45秒）"""

    def construct(self):
        self.show_heading("弱い収束")
        self.draw_densities()
        self.test_integral()
        self.show_formula()
        self.read(1.4)

    def draw_densities(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[0, 1.3, 1],
            x_length=7.8,
            y_length=2.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.45 + LEFT * 0.2)
        self.play(Create(self.axes), run_time=0.75)
        self.curve = None
        for mu, col, label in ((1.0, BLUE, "分布"), (1.8, TEAL, "動く"), (2.6, YELLOW, "近づく")):
            f = self.axes.plot(
                lambda x, m=mu: 0.9 * math.exp(-3.5 * (x - m) ** 2),
                x_range=[0.05, 4.0],
                color=col,
                stroke_width=4,
            )
            if self.curve is None:
                self.play(Create(f), run_time=1.1)
                self.curve = f
                note = self.ja_text(label, font_size=24)
                note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
                self.play(FadeIn(note), run_time=0.35)
                self.note = note
            else:
                cap = self.ja_text(label, font_size=24).move_to(self.note)
                self.play(Transform(self.curve, f), Transform(self.note, cap), run_time=1.15)
            self.read(0.2)

    def test_integral(self):
        # test function bump
        test = self.axes.plot(
            lambda x: 0.55 * math.exp(-2.0 * (x - 2.5) ** 2),
            x_range=[0.05, 4.0],
            color=ORANGE,
            stroke_width=3,
        )
        cap = self.ja_text("試験関数で積分", font_size=24).move_to(self.note)
        self.play(Create(test), Transform(self.note, cap), run_time=1.4)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\int f\,d\mu_n\to\int f\,d\mu").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
