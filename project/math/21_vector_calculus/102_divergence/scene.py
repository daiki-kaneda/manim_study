from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class Divergence(JapaneseScene):
    """#102 発散はわき出し（約90秒）"""

    def construct(self):
        self.show_heading("発散")
        self.draw_source()
        self.draw_sink()
        self.show_formula()
        self.hold(1.2)

    def _burst(self, center, outward=True, color=YELLOW):
        arrows = VGroup()
        for ang in np.linspace(0, TAU, 8, endpoint=False):
            u = np.array([np.cos(ang), np.sin(ang), 0.0])
            if outward:
                a, b = center + 0.35 * u, center + 1.25 * u
            else:
                a, b = center + 1.25 * u, center + 0.35 * u
            arrows.add(Arrow(a, b, buff=0, color=color, stroke_width=3, max_tip_length_to_length_ratio=0.2))
        return arrows

    def draw_source(self):
        c = LEFT * 3.0 + DOWN * 0.1
        arrows = self._burst(c, True, YELLOW)
        lab = self.ja_text("わき出し", font_size=24).next_to(arrows, DOWN, buff=0.35)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.06), run_time=0.9)
        self.play(FadeIn(lab), run_time=0.3)
        self.hold(0.45)

    def draw_sink(self):
        c = RIGHT * 2.4 + DOWN * 0.1
        arrows = self._burst(c, False, BLUE)
        lab = self.ja_text("吸い込み", font_size=24).next_to(arrows, DOWN, buff=0.35)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.06), run_time=0.9)
        self.play(FadeIn(lab), run_time=0.3)
        self.hold(0.55)

    def show_formula(self):
        formula = MathTex(r"\mathrm{div}\,F=\partial_x P+\partial_y Q").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
