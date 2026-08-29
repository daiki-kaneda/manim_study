from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GeneratingFunction(PacedScene):
    """#136 幾何級数の母関数（約45秒）"""

    def construct(self):
        self.show_heading("母関数")
        self.stack_terms()
        self.show_formula()
        self.read(1.4)

    def stack_terms(self):
        terms = [
            MathTex("1", font_size=40),
            MathTex("+x", font_size=40),
            MathTex(r"+x^2", font_size=40),
            MathTex(r"+x^3", font_size=40),
            MathTex(r"+\cdots", font_size=40),
        ]
        row = VGroup()
        for i, t in enumerate(terms):
            if i == 0:
                t.shift(LEFT * 2.6 + UP * 0.35)
            else:
                t.next_to(row[-1], RIGHT, buff=0.18)
            row.add(t)
            self.play(FadeIn(t, shift=UP * 0.15), run_time=0.7)
            self.read(0.22)
        note = self.ja_text("無限に足す", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.5)
        self.row = row

    def show_formula(self):
        formula = MathTex(r"\sum_{n=0}^{\infty}x^n=\frac{1}{1-x}").scale(0.95)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
