from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Feuerbach(PacedScene):
    """#254 フォイエルバッハ：九点円は内接円に接する（約45秒）"""

    def construct(self):
        self.show_heading("フォイエルバッハの定理")
        self.draw_triangle()
        self.draw_circles()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.5 + UP * 1.7
        self.B = LEFT * 2.7 + DOWN * 1.6
        self.C = RIGHT * 2.9 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def draw_circles(self):
        a = np.linalg.norm(self.B - self.C)
        b = np.linalg.norm(self.A - self.C)
        c = np.linalg.norm(self.A - self.B)
        s = (a + b + c) / 2
        area = 0.5 * abs(np.cross(self.B - self.A, self.C - self.A)[2])
        r = area / s
        I = (a * self.A + b * self.B + c * self.C) / (a + b + c)
        # nine-point center approx midpoint of OH; for simplicity use midpoint of orthocenter and circumcenter
        # Approximate NPC as circle through midpoints
        M_ab = 0.5 * (self.A + self.B)
        M_bc = 0.5 * (self.B + self.C)
        M_ca = 0.5 * (self.C + self.A)
        # circumcenter of midpoints
        def circ_center(P, Q, R):
            A, B, C = P, Q, R
            D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
            Ux = ((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1]) + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / D
            Uy = ((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0]) + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / D
            O = np.array([Ux, Uy, 0.0])
            return O, np.linalg.norm(O - A)

        N, R9 = circ_center(M_ab, M_bc, M_ca)
        inc = Circle(radius=r, color=TEAL, stroke_width=3).move_to(I)
        npc = Circle(radius=R9, color=YELLOW, stroke_width=3).move_to(N)
        self.play(Create(inc), run_time=1.1)
        cap = self.ja_text("内接円", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.read(0.2)
        self.play(Create(npc), run_time=1.2)
        # touch point approx along NI
        v = I - N
        nrm = np.linalg.norm(v)
        if nrm > 1e-6:
            # Feuerbach: internal touch, distance |R9 - r|
            touch = N + (R9 - r) * (v / nrm) if R9 > r else N + R9 * (v / nrm)
        else:
            touch = I
        cap2 = self.ja_text("九点円と接する", font_size=24).move_to(self.note)
        self.play(FadeIn(Dot(touch, color=ORANGE, radius=0.1)), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("九点円は内接円に接する", font_size=28)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
