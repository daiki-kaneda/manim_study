from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class EulerDistance(PacedScene):
    """#217 オイラー：外心と内心の距離（約45秒）"""

    def construct(self):
        self.show_heading("オイラーの距離公式")
        self.draw_triangle()
        self.mark_centers()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.6 + DOWN * 1.5
        self.B = RIGHT * 3.0 + DOWN * 1.4
        self.C = LEFT * 0.4 + UP * 2.0
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mark_centers(self):
        a = np.linalg.norm(self.B - self.C)
        b = np.linalg.norm(self.A - self.C)
        c = np.linalg.norm(self.A - self.B)
        # circumcenter
        A, B, C = self.A, self.B, self.C
        D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
        Ux = ((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1]) + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / D
        Uy = ((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0]) + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / D
        O = np.array([Ux, Uy, 0.0])
        R = np.linalg.norm(O - A)
        # incenter
        I = (a * A + b * B + c * C) / (a + b + c)
        s = (a + b + c) / 2
        area = 0.5 * abs(np.cross(B - A, C - A)[2])
        r = area / s
        oc = Circle(radius=R, color=GREY, stroke_width=2).move_to(O)
        ic = Circle(radius=r, color=TEAL, stroke_width=3).move_to(I)
        dO = Dot(O, color=YELLOW, radius=0.09)
        dI = Dot(I, color=ORANGE, radius=0.09)
        self.play(Create(oc), FadeIn(dO), run_time=1.2)
        cap = self.ja_text("外心 O", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.25)
        self.play(Create(ic), FadeIn(dI), run_time=1.1)
        seg = Line(O, I, color=RED, stroke_width=4)
        cap2 = self.ja_text("距離 d", font_size=24).move_to(self.note)
        self.play(Create(seg), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"d^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"d^{2}=R(R-2r)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"d^{2}=R(R-2r)").scale(1.1)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
