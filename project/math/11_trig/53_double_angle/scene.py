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


class DoubleAngle(JapaneseScene):
    """#53 二倍角（約90秒）"""

    def construct(self):
        self.R = 2.15
        self.origin = LEFT * 2.35 + DOWN * 0.2
        self.theta = 32 * DEGREES
        self.show_heading("二倍角")
        self.draw_circle()
        self.decompose()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_circle(self):
        circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        x_axis = Line(self.origin + LEFT * 0.3 * self.R, self.origin + RIGHT * 1.25 * self.R, color=GREY, stroke_width=1.5)
        self.play(Create(circle), Create(x_axis), run_time=0.7)
        p = self._pt(2 * self.theta)
        ray = Line(self.origin, p, color=YELLOW, stroke_width=3)
        arc = Arc(radius=0.5, start_angle=0, angle=2 * self.theta, color=ORANGE, arc_center=self.origin)
        lab = MathTex(r"2\theta", color=ORANGE, font_size=30).next_to(arc, RIGHT, buff=0.1)
        self.play(Create(ray), Create(arc), FadeIn(lab), run_time=0.7)
        self.hold(0.45)
        self.p = p

    def decompose(self):
        foot = np.array([self.p[0], self.origin[1], 0.0])
        drop = DashedLine(self.p, foot, color=YELLOW, stroke_width=2)
        sinlab = MathTex(r"\sin 2\theta", color=YELLOW, font_size=30)
        sinlab.to_edge(RIGHT, buff=0.45).shift(UP * 1.6)
        self.play(Create(drop), FadeIn(sinlab), run_time=0.6)
        # 中間の θ の点
        q = self._pt(self.theta)
        mid = Line(self.origin, q, color=BLUE, stroke_width=3)
        self.play(Create(mid), run_time=0.5)
        parts = MathTex(r"2\sin\theta\cos\theta", color=BLUE, font_size=30)
        parts.next_to(sinlab, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(parts), run_time=0.5)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"\sin 2\theta=2\sin\theta\cos\theta").scale(1.05)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
