from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class BrocardPoint(PacedScene):
    """#481 ブロシャール点：等角の回転点（約45秒）"""

    def construct(self):
        self.show_heading("ブロシャール点")
        self.draw_triangle()
        self.equal_angles()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.15
        self.B = LEFT * 2.7 + DOWN * 1.45
        self.C = RIGHT * 2.7 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形内の点", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def equal_angles(self):
        P = self.A * 0.35 + self.B * 0.35 + self.C * 0.3
        rays = VGroup(
            Line(P, self.A, color=ORANGE, stroke_width=3),
            Line(P, self.B, color=ORANGE, stroke_width=3),
            Line(P, self.C, color=ORANGE, stroke_width=3),
        )
        markers = VGroup(*[
            Dot(P + u * 0.35, color=YELLOW, radius=0.06)
            for u in [
                (self.A - P) / np.linalg.norm(self.A - P),
                (self.B - P) / np.linalg.norm(self.B - P),
                (self.C - P) / np.linalg.norm(self.C - P),
            ]
        ])
        dot = Dot(P, color=RED, radius=0.1)
        cap = self.ja_text("角が等しい", font_size=24).move_to(self.note)
        self.play(FadeIn(dot), Create(rays), Transform(self.note, cap), run_time=1.4)
        self.play(FadeIn(markers), run_time=0.7)
        self.read(0.25)
        cap2 = self.ja_text("ブロシャール角", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"\angle PAB").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\angle PAB=\angle PBC=\angle PCA=\omega").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\angle PAB=\angle PBC=\angle PCA=\omega").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
