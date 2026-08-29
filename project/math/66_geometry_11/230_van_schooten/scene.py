from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class VanSchooten(PacedScene):
    """#230 ファン・シューテン：回転で辺が移る（約45秒）"""

    def construct(self):
        self.show_heading("ファン・シューテン")
        self.draw_triangle()
        self.rotate_copy()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.2 + DOWN * 1.2
        self.B = RIGHT * 2.2 + DOWN * 1.2
        self.C = ORIGIN + UP * 1.8
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def rotate_copy(self):
        # outward equilateral on BC, then 60° rotation of A around B maps C toward new vertex
        def rot60(p, center, sign=1):
            v = p - center
            c, s = np.cos(sign * PI / 3), np.sin(sign * PI / 3)
            return center + np.array([c * v[0] - s * v[1], s * v[0] + c * v[1], 0])

        P = rot60(self.C, self.B, sign=-1)  # outward from ABC assuming CCW
        # check orientation
        if np.cross(self.B - self.A, self.C - self.A)[2] > 0:
            P = rot60(self.C, self.B, sign=1)
        eq = Polygon(self.B, self.C, P, color=BLUE, stroke_width=3)
        self.play(Create(eq), run_time=1.2)
        cap = self.ja_text("外に正三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.25)
        # arc showing rotation of A around B by 60° landing near something
        A2 = rot60(self.A, self.B, sign=1 if np.cross(self.B - self.A, self.C - self.A)[2] > 0 else -1)
        arc = ArcBetweenPoints(self.A, A2, angle=PI / 3, color=ORANGE, stroke_width=4)
        a2 = Dot(A2, color=ORANGE, radius=0.1)
        line = DashedLine(self.B, A2, color=ORANGE, stroke_width=3)
        cap2 = self.ja_text("60° 回転", font_size=24).move_to(self.note)
        self.play(Create(arc), FadeIn(a2), Create(line), Transform(self.note, cap2), run_time=1.6)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("回転で辺がうつる", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
