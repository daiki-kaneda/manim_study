from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class PartialDerivative(PacedScene):
    """#140 偏微分は一方向だけ動かす（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.15 + DOWN * 0.2
        self.show_heading("偏微分")
        self.draw_levels()
        self.slice_x()
        self.slice_y()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, x, y):
        return self.origin + RIGHT * x + UP * y

    def draw_levels(self):
        ax = Line(self.origin + LEFT * 0.4, self.origin + RIGHT * 4.3, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.4, self.origin + UP * 2.85, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.85)
        circles = VGroup()
        for r, col in ((0.7, BLUE_E), (1.25, BLUE), (1.85, BLUE_A)):
            circles.add(Circle(radius=r, color=col, stroke_width=4).move_to(self.origin))
        self.play(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.22), run_time=2.2)
        note = self.ja_text("高さの線", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note
        self.circles = circles

    def slice_x(self):
        y0 = 0.95
        line = DashedLine(self._pt(-0.15, y0), self._pt(3.6, y0), color=YELLOW, stroke_width=3)
        cap = self.ja_text("y を止める", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.3)
        p = self._pt(1.1, y0)
        tangent = Line(p + LEFT * 0.85, p + RIGHT * 0.85, color=ORANGE, stroke_width=6)
        self.play(FadeIn(Dot(p, color=ORANGE, radius=0.08)), Create(tangent), run_time=1.1)
        self.read(0.4)

    def slice_y(self):
        x0 = 1.35
        line = DashedLine(self._pt(x0, -0.15), self._pt(x0, 2.55), color=GREEN, stroke_width=3)
        cap = self.ja_text("x を止める", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.3)
        p = self._pt(x0, 1.2)
        tangent = Line(p + DOWN * 0.7, p + UP * 0.7, color=TEAL, stroke_width=6)
        self.play(FadeIn(Dot(p, color=TEAL, radius=0.08)), Create(tangent), run_time=1.1)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"f_x").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"f_x=\frac{\partial f}{\partial x},\quad f_y=\frac{\partial f}{\partial y}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"f_x=\frac{\partial f}{\partial x},\quad f_y=\frac{\partial f}{\partial y}").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
