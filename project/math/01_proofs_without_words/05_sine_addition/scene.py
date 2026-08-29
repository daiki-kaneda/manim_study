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


class SineAddition(JapaneseScene):
    """#5 加法定理 sin(α+β)（約90秒）"""

    def construct(self):
        self.alpha = 40 * DEGREES
        self.beta = 32 * DEGREES
        self.R = 2.15
        self.origin = LEFT * 2.4 + DOWN * 0.35
        self.show_heading("加法定理")
        self.draw_circle_and_angles()
        self.decompose_sine()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_circle_and_angles(self):
        circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        x_axis = Line(
            self.origin + LEFT * 0.3 * self.R,
            self.origin + RIGHT * 1.15 * self.R,
            color=GREY,
            stroke_width=1.5,
        )
        self.play(Create(circle), Create(x_axis), run_time=1.0)

        p_a = self._pt(self.alpha)
        p_ab = self._pt(self.alpha + self.beta)
        ray_a = Line(self.origin, p_a, color=BLUE, stroke_width=3)
        ray_ab = Line(self.origin, p_ab, color=YELLOW, stroke_width=3)
        self.play(Create(ray_a), run_time=0.7)
        arc_a = Arc(
            radius=0.55,
            start_angle=0,
            angle=self.alpha,
            color=BLUE,
            arc_center=self.origin,
        )
        lab_a = MathTex(r"\alpha", color=BLUE, font_size=32).next_to(arc_a, RIGHT, buff=0.12)
        self.play(Create(arc_a), FadeIn(lab_a), run_time=0.6)
        self.hold(0.5)

        self.play(Create(ray_ab), run_time=0.7)
        arc_b = Arc(
            radius=0.8,
            start_angle=self.alpha,
            angle=self.beta,
            color=ORANGE,
            arc_center=self.origin,
        )
        lab_b = MathTex(r"\beta", color=ORANGE, font_size=32).next_to(arc_b, UR, buff=0.08)
        self.play(Create(arc_b), FadeIn(lab_b), run_time=0.6)
        self.hold(0.6)

        self.circle = circle
        self.p_ab = p_ab
        self.ray_a = ray_a
        self.ray_ab = ray_ab

    def decompose_sine(self):
        foot = np.array([self.p_ab[0], self.origin[1], 0.0])
        height = DashedLine(self.p_ab, foot, color=YELLOW, stroke_width=2)
        sin_label = MathTex(r"\sin(\alpha+\beta)", font_size=32)
        sin_label.to_edge(RIGHT, buff=0.55).shift(UP * 1.6)
        self.play(Create(height), FadeIn(sin_label), run_time=0.9)
        self.hold(0.8)

        f = self.origin + np.array(polar(self.R * np.cos(self.beta), self.alpha))
        f_dot = Dot(f, color=GREEN, radius=0.06)
        to_f = Line(self.origin, f, color=GREEN, stroke_width=4)
        fc = Line(f, self.p_ab, color=ORANGE, stroke_width=4)
        self.play(Create(to_f), FadeIn(f_dot), run_time=0.7)
        self.play(Create(fc), run_time=0.7)
        self.hold(0.9)

        part1 = MathTex(r"\sin\alpha\cos\beta", color=GREEN, font_size=30)
        part2 = MathTex(r"\cos\alpha\sin\beta", color=ORANGE, font_size=30)
        parts = VGroup(part1, MathTex("+", font_size=30), part2).arrange(RIGHT, buff=0.12)
        parts.next_to(sin_label, DOWN, aligned_edge=RIGHT, buff=0.35)
        self.play(FadeIn(parts), run_time=0.7)
        self.hold(1.0)
        self.parts = parts
        self.sin_label = sin_label

    def show_formula(self):
        formula = MathTex(
            r"\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta"
        ).scale(0.85)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.3)
        self.play(Indicate(formula, color=BLUE), run_time=0.8)
        self.hold(1.4)
