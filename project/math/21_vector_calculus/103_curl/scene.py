from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class Curl(JapaneseScene):
    """#103 回転（約90秒）"""

    def construct(self):
        self.origin = LEFT * 1.8 + DOWN * 0.15
        self.show_heading("回転")
        self.draw_field()
        self.show_formula()
        self.hold(1.2)

    def draw_field(self):
        axes_x = Line(self.origin + LEFT * 2.3, self.origin + RIGHT * 2.5, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 2.0, self.origin + UP * 2.1, color=GREY, stroke_width=2)
        self.play(Create(axes_x), Create(axes_y), run_time=0.4)
        arrows = VGroup()
        for r in (0.85, 1.55):
            for t in np.linspace(0, TAU, 10, endpoint=False):
                p = self.origin + np.array([r * np.cos(t), r * np.sin(t), 0])
                tang = np.array([-np.sin(t), np.cos(t), 0])
                arrows.add(Arrow(p - 0.22 * tang, p + 0.22 * tang, buff=0, color=YELLOW, stroke_width=3, max_tip_length_to_length_ratio=0.35))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.02), run_time=1.3)
        note = self.ja_text("点のまわり", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\mathrm{curl}\,F=\partial_x Q-\partial_y P").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
