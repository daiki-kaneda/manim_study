from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class EDefinition(JapaneseScene):
    """#20 e の定義 (1+1/n)^n（約90秒）"""

    def construct(self):
        self.show_heading("e の定義")
        self.show_sequence()
        self.draw_bars()
        self.show_limit()
        self.hold(1.2)

    def _value(self, n: int) -> float:
        return (1 + 1 / n) ** n

    def show_sequence(self):
        expr = MathTex(r"a_n=\left(1+\frac{1}{n}\right)^n").scale(1.15)
        expr.shift(UP * 2.15)
        self.play(Write(expr), run_time=0.9)
        self.hold(0.5)
        self.expr = expr

    def draw_bars(self):
        ns = [1, 2, 5, 10, 100]
        colors = [BLUE, GREEN, YELLOW, ORANGE, TEAL]
        bars = VGroup()
        labels = VGroup()
        max_h = 3.2
        e_approx = 2.718
        origin = LEFT * 3.6 + DOWN * 1.8
        for i, n in enumerate(ns):
            h = self._value(n) / e_approx * max_h
            bar = Rectangle(width=0.7, height=h, color=colors[i], fill_opacity=0.8, stroke_width=1)
            bar.move_to(origin + RIGHT * 1.35 * i + UP * (h / 2))
            lab = MathTex(rf"n={n}", font_size=22).next_to(bar, DOWN, buff=0.12)
            val = MathTex(f"{self._value(n):.3f}", font_size=22).next_to(bar, UP, buff=0.1)
            bars.add(bar)
            labels.add(VGroup(lab, val))
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in bars], lag_ratio=0.2), run_time=1.6)
        self.play(FadeIn(labels), run_time=0.5)
        self.hold(0.8)
        self.bars = bars
        self.origin = origin
        self.max_h = max_h

    def show_limit(self):
        e_line = DashedLine(
            self.origin + UP * self.max_h + LEFT * 0.4,
            self.origin + UP * self.max_h + RIGHT * 6.6,
            color=YELLOW,
            stroke_width=2,
        )
        e_lab = MathTex("e", color=YELLOW, font_size=36).next_to(e_line, RIGHT, buff=0.12)
        self.play(Create(e_line), FadeIn(e_lab), run_time=0.7)
        limit = MathTex(r"\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e").scale(1.05)
        limit.to_edge(DOWN, buff=0.4)
        self.play(Write(limit), run_time=1.0)
        self.play(Indicate(limit, color=YELLOW), run_time=0.8)
        self.hold(1.3)
