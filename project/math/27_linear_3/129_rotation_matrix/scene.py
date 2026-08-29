from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene
from manim_math.geometry import apply_2d


class RotationMatrix(PacedScene):
    """#129 回転行列（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 1.15
        self.unit = 1.4
        self.show_heading("回転行列")
        self.draw_square()
        self.turn()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _rot(self, deg):
        t = deg * DEGREES
        c, s = np.cos(t), np.sin(t)
        return [[c, -s], [s, c]]

    def _poly(self, mat):
        corners = [apply_2d(mat, c)[:2] for c in ((0.2, 0.2), (1.2, 0.2), (1.2, 1.2), (0.2, 1.2))]
        return Polygon(*[self._pt(c) for c in corners], color=BLUE, fill_opacity=0.45, stroke_width=2)

    def draw_square(self):
        ax = Line(self.origin + LEFT * 0.4, self.origin + RIGHT * 3.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.4, self.origin + UP * 3.3, color=GREY, stroke_width=2)
        self.sq = self._poly(self._rot(0))
        self.play(Create(ax), Create(ay), run_time=0.9)
        self.play(FadeIn(self.sq), run_time=0.8)
        self.read(0.35)

    def turn(self):
        note = self.ja_text("0°", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        for deg in (90, 180, 270):
            nxt = self._poly(self._rot(deg))
            cap = self.ja_text(f"{deg}°", font_size=24).move_to(note)
            self.play(Transform(self.sq, nxt), Transform(note, cap), run_time=1.35)
            self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"R_\theta").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"R_\theta=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.8)
