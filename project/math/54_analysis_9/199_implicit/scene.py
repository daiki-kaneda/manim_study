from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class ImplicitCurve(PacedScene):
    """#199 陰関数は F(x,y)=0 の曲線（約45秒）"""

    def construct(self):
        self.show_heading("陰関数")
        self.draw_curve()
        self.draw_tangent()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-1.6, 1.6, 1],
            x_length=7.4,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.1)
        # ellipse x^2/4 + y^2 = 1
        self.ell = Ellipse(width=4.0, height=2.4, color=BLUE, stroke_width=5).move_to(self.axes.c2p(0, 0))
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.ell), run_time=1.6)
        note = self.ja_text("F=0", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def draw_tangent(self):
        # point on ellipse at angle
        a, b = 2.0, 1.2
        t = 0.7
        p = np.array([a * np.cos(t), b * np.sin(t), 0.0])
        # gradient of x^2/a^2 + y^2/b^2 - 1: (2x/a^2, 2y/b^2)
        g = np.array([2 * p[0] / (a * a), 2 * p[1] / (b * b), 0.0])
        # tangent direction perpendicular to g
        d = np.array([-g[1], g[0], 0.0])
        d = d / np.linalg.norm(d) * 1.4
        center = self.axes.c2p(0, 0)
        # map ellipse local coords: ell already sized width=4 height=2.4 so matches a=2,b=1.2 in axes units roughly
        # Use geometric positions on the drawn ellipse
        pt = self.ell.point_at_angle(t)
        tang = Line(pt - d, pt + d, color=ORANGE, stroke_width=4)
        dot = Dot(pt, color=ORANGE, radius=0.1)
        cap = self.ja_text("接線", font_size=24).move_to(self.note)
        self.play(FadeIn(dot), Create(tang), Transform(self.note, cap), run_time=1.5)
        self.read(0.35)
        cap2 = self.ja_text("陰微分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\frac{dy}{dx}=-\frac{F_x}{F_y}").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
