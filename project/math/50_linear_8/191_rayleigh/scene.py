from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
import numpy as np
from manim import *
from manim_math import PacedScene


class RayleighQuotient(PacedScene):
    """#191 レイリー商は単位ベクトルでの二次形式（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.5 + DOWN * 1.15
        self.show_heading("レイリー商")
        self.draw_circle()
        self.sweep()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_circle(self):
        self.R = 2.0
        circ = Circle(radius=self.R, color=GREY, stroke_width=2).move_to(self.origin)
        self.play(Create(circ), run_time=1.1)
        self.arr = Arrow(self.origin, self._pt([self.R, 0]), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.arr), run_time=1.0)
        note = self.ja_text(r"単位ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        # A = diag(3, 1) eigenvalues — R(x)= 3 cos^2 + sin^2
        self.val_bar = Line(RIGHT * 3.2 + DOWN * 1.8, RIGHT * 3.2 + UP * 1.8, color=GREY, stroke_width=2)
        self.play(Create(self.val_bar), run_time=0.5)
        self.marker = Dot(RIGHT * 3.2 + UP * (-1.2), color=ORANGE, radius=0.1)
        self.play(FadeIn(self.marker), run_time=0.35)

    def _rayleigh(self, theta):
        return 3 * math.cos(theta) ** 2 + math.sin(theta) ** 2

    def sweep(self):
        trail = VGroup()
        for theta in (0.55, 1.1, 1.65):
            tip = self._pt([self.R * math.cos(theta), self.R * math.sin(theta)])
            new = Arrow(self.origin, tip, buff=0, color=YELLOW, stroke_width=5)
            r = self._rayleigh(theta)
            # map [1,3] -> [-1.2, 1.6] on bar
            y = -1.2 + (r - 1) / 2 * 2.8
            mpos = RIGHT * 3.2 + UP * y
            trail.add(Dot(tip, radius=0.04, color=GREY_B))
            self.play(
                Transform(self.arr, new),
                self.marker.animate.move_to(mpos),
                FadeIn(trail[-1]),
                run_time=0.95,
            )
        # go to max at theta=0
        tip = self._pt([self.R, 0])
        new = Arrow(self.origin, tip, buff=0, color=BLUE, stroke_width=5)
        mpos = RIGHT * 3.2 + UP * 1.6
        cap = self.ja_text("最大＝固有値", font_size=24).move_to(self.note)
        self.play(
            Transform(self.arr, new),
            self.marker.animate.move_to(mpos),
            Transform(self.note, cap),
            run_time=1.5,
        )
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
        eq = MathTex(r"R(x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"R(x)=\frac{x^{\mathsf T}Ax}{x^{\mathsf T}x}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"R(x)=\frac{x^{\mathsf T}Ax}{x^{\mathsf T}x}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
