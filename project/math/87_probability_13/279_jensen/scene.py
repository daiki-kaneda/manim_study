from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class JensenInequality(PacedScene):
    """#279 イェンセン：凸なら期待値の外 ≥ 内側（約45秒）"""

    def construct(self):
        self.show_heading("イェンセンの不等式")
        self.draw_convex()
        self.compare()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_convex(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[-0.2, 3.5, 1],
            x_length=6.5,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 0.4 + UP * 0.15)
        curve = self.axes.plot(lambda x: 0.25 * (x - 0.5) ** 2 + 0.4, x_range=[0.2, 3.8], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), run_time=0.7)
        self.play(Create(curve), run_time=1.3)
        note = self.ja_text("凸な関数", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.curve = curve

    def compare(self):
        x1, x2 = 0.8, 3.2
        p1 = self.axes.c2p(x1, 0.25 * (x1 - 0.5) ** 2 + 0.4)
        p2 = self.axes.c2p(x2, 0.25 * (x2 - 0.5) ** 2 + 0.4)
        chord = Line(p1, p2, color=ORANGE, stroke_width=4)
        mid_x = 0.5 * (x1 + x2)
        mid_curve = self.axes.c2p(mid_x, 0.25 * (mid_x - 0.5) ** 2 + 0.4)
        mid_chord = chord.point_from_proportion(0.5)
        d1 = Dot(mid_curve, color=YELLOW, radius=0.09)
        d2 = Dot(mid_chord, color=ORANGE, radius=0.09)
        cap = self.ja_text("弦と曲線", font_size=24).move_to(self.note)
        self.play(Create(chord), FadeIn(Dot(p1, color=TEAL)), FadeIn(Dot(p2, color=TEAL)), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("弦が上", font_size=24).move_to(self.note)
        self.play(FadeIn(d1), FadeIn(d2), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"f(\mathbb{E}X)\le\mathbb{E}f(X)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"f(\mathbb{E}X)\le\mathbb{E}f(X)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"f(\mathbb{E}X)\le\mathbb{E}f(X)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
