from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class LeibnizPi(JapaneseScene):
    """#57 ライプニッツの公式（約90秒）"""

    def construct(self):
        self.show_heading("π の級数")
        self.show_partials()
        self.show_formula()
        self.hold(1.2)

    def _s(self, n):
        total = 0.0
        for k in range(n):
            total += ((-1) ** k) / (2 * k + 1)
        return 4 * total

    def show_partials(self):
        ns = [1, 2, 3, 6, 20]
        colors = [BLUE, GREEN, ORANGE, TEAL, YELLOW]
        origin = LEFT * 3.8 + DOWN * 1.6
        max_h = 3.15
        pi_h = math.pi / 4.1 * max_h  # 4*s_n の上限を 4 と見てスケール
        # 値は 4 前後なので高さ = value / 4 * max_h
        bars = VGroup()
        for i, n in enumerate(ns):
            val = self._s(n)
            h = val / 4.2 * max_h
            bar = Rectangle(width=0.75, height=h, color=colors[i], fill_opacity=0.85, stroke_width=1)
            bar.move_to(origin + RIGHT * 1.35 * i + UP * (h / 2))
            lab = MathTex(rf"n={n}", font_size=22).next_to(bar, DOWN, buff=0.1)
            num = MathTex(f"{val:.2f}", font_size=22).next_to(bar, UP, buff=0.08)
            bars.add(VGroup(bar, lab, num))
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in bars], lag_ratio=0.18), run_time=1.6)
        pi_line = DashedLine(
            origin + UP * (math.pi / 4.2 * max_h) + LEFT * 0.35,
            origin + UP * (math.pi / 4.2 * max_h) + RIGHT * 6.5,
            color=YELLOW,
            stroke_width=2,
        )
        pi_lab = MathTex(r"\pi", color=YELLOW, font_size=34).next_to(pi_line, RIGHT, buff=0.1)
        self.play(Create(pi_line), FadeIn(pi_lab), run_time=0.6)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"4\left(1-\frac13+\frac15-\frac17+\cdots\right)=\pi").scale(0.9)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
