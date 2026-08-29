from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import polar


class CosineAddition(JapaneseScene):
    """#54 余弦の加法定理（約90秒）"""

    def construct(self):
        self.alpha = 38 * DEGREES
        self.beta = 28 * DEGREES
        self.R = 2.1
        self.origin = LEFT * 2.4 + DOWN * 0.15
        self.show_heading("余弦の加法")
        self.draw_circle()
        self.project()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_circle(self):
        circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        x_axis = Line(self.origin + LEFT * 0.25 * self.R, self.origin + RIGHT * 1.25 * self.R, color=GREY, stroke_width=1.5)
        self.play(Create(circle), Create(x_axis), run_time=0.7)
        p = self._pt(self.alpha + self.beta)
        ray = Line(self.origin, p, color=YELLOW, stroke_width=3)
        a = Arc(radius=0.5, start_angle=0, angle=self.alpha, color=BLUE, arc_center=self.origin)
        b = Arc(radius=0.75, start_angle=self.alpha, angle=self.beta, color=ORANGE, arc_center=self.origin)
        la = MathTex(r"\alpha", color=BLUE, font_size=28).next_to(a, RIGHT, buff=0.08)
        lb = MathTex(r"\beta", color=ORANGE, font_size=28).next_to(b, UR, buff=0.06)
        self.play(Create(ray), Create(a), Create(b), FadeIn(la), FadeIn(lb), run_time=0.85)
        self.hold(0.45)
        self.p = p

    def project(self):
        foot = np.array([self.p[0], self.origin[1], 0.0])
        drop = DashedLine(self.p, foot, color=YELLOW, stroke_width=2)
        lab = MathTex(r"\cos(\alpha+\beta)", font_size=30)
        lab.to_edge(RIGHT, buff=0.4).shift(UP * 1.55)
        self.play(Create(drop), FadeIn(lab), run_time=0.65)
        parts = MathTex(r"\cos\alpha\cos\beta-\sin\alpha\sin\beta", font_size=28)
        parts.next_to(lab, DOWN, aligned_edge=RIGHT, buff=0.28)
        self.play(FadeIn(parts), run_time=0.55)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta").scale(0.72)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
