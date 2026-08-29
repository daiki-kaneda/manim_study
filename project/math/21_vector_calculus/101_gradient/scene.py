from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class Gradient(JapaneseScene):
    """#101 勾配は最も急な向き（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 0.2
        self.show_heading("勾配")
        self.draw_contours()
        self.draw_arrows()
        self.show_formula()
        self.hold(1.2)

    def draw_contours(self):
        axes_x = Line(self.origin + LEFT * 2.2, self.origin + RIGHT * 2.4, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 2.0, self.origin + UP * 2.1, color=GREY, stroke_width=2)
        self.play(Create(axes_x), Create(axes_y), run_time=0.4)
        rings = VGroup()
        for r, op in ((0.7, 0.9), (1.25, 0.7), (1.8, 0.5)):
            rings.add(Circle(radius=r, color=BLUE, stroke_width=2, stroke_opacity=op).move_to(self.origin))
        self.play(LaggedStart(*[Create(c) for c in rings], lag_ratio=0.15), run_time=0.9)
        note = self.ja_text("等高線", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.4)
        self.note = note

    def draw_arrows(self):
        arrows = VGroup()
        for ang in np.linspace(0, TAU, 8, endpoint=False):
            start = self.origin + np.array([1.05 * np.cos(ang), 1.05 * np.sin(ang), 0])
            end = self.origin + np.array([1.85 * np.cos(ang), 1.85 * np.sin(ang), 0])
            arrows.add(Arrow(start, end, buff=0, color=YELLOW, stroke_width=3, max_tip_length_to_length_ratio=0.18))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), run_time=1.0)
        cap = self.ja_text("一番急な向き", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"\nabla f=\bigl(\partial_x f,\ \partial_y f\bigr)").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
