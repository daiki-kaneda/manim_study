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


class PythagoreanIdentity(JapaneseScene):
    """#23 sin²θ+cos²θ=1（約90秒）"""

    def construct(self):
        self.R = 2.25
        self.origin = LEFT * 2.2 + DOWN * 0.55
        self.theta = 48 * DEGREES
        self.show_heading("三角の恒等式")
        self.draw_triangle()
        self.label_sides()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_triangle(self):
        circle = Circle(radius=self.R, color=GREY, stroke_width=2).move_to(self.origin)
        p = self._pt(self.theta)
        foot = np.array([p[0], self.origin[1], 0.0])
        hyp = Line(self.origin, p, color=YELLOW, stroke_width=4)
        adj = Line(self.origin, foot, color=BLUE, stroke_width=4)
        opp = Line(foot, p, color=GREEN, stroke_width=4)
        self.play(Create(circle), run_time=0.7)
        self.play(Create(hyp), run_time=0.55)
        self.play(Create(adj), Create(opp), run_time=0.7)
        arc = Arc(radius=0.45, start_angle=0, angle=self.theta, color=ORANGE, arc_center=self.origin)
        lab = MathTex(r"\theta", color=ORANGE, font_size=32).next_to(arc, RIGHT, buff=0.08)
        self.play(Create(arc), FadeIn(lab), run_time=0.5)
        self.hold(0.5)
        self.p, self.foot = p, foot
        self.hyp, self.adj, self.opp = hyp, adj, opp

    def label_sides(self):
        cos_lab = MathTex(r"\cos\theta", color=BLUE, font_size=32)
        cos_lab.next_to(self.adj, DOWN, buff=0.15)
        sin_lab = MathTex(r"\sin\theta", color=GREEN, font_size=32)
        sin_lab.next_to(self.opp, RIGHT, buff=0.12)
        one_lab = MathTex("1", color=YELLOW, font_size=34)
        one_lab.next_to(self.hyp.get_center(), UL, buff=0.12)
        self.play(FadeIn(cos_lab), FadeIn(sin_lab), FadeIn(one_lab), run_time=0.7)
        note = self.ja_text("半径 1 の直角三角形", font_size=26)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)
        self.play(FadeIn(note), run_time=0.45)
        self.hold(0.8)
        pyth = MathTex(r"a^2+b^2=c^2", font_size=36)
        pyth.next_to(note, DOWN, buff=0.4)
        self.play(FadeIn(pyth), run_time=0.5)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\sin^2\theta+\cos^2\theta=1").scale(1.2)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
        self.hold(1.3)
