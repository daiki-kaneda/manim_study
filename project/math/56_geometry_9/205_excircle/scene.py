from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Excircle(PacedScene):
    """#205 傍接円は外で接する（約45秒）"""

    def construct(self):
        self.show_heading("傍接円")
        self.draw_triangle()
        self.draw_excircle()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.4 + UP * 1.7
        self.B = LEFT * 2.6 + DOWN * 1.6
        self.C = RIGHT * 2.8 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        # extend AB and AC a bit beyond B,C for excircle opposite A... actually A-excircle opposite A touches BC
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def draw_excircle(self):
        # A-excircle: center is intersection of external angle bisectors at B,C and internal at A
        # For triangle with sides a,b,c opposite A,B,C:
        # Ia = (-aA + bB + cC)/(-a+b+c)
        a = np.linalg.norm(self.B - self.C)
        b = np.linalg.norm(self.A - self.C)
        c = np.linalg.norm(self.A - self.B)
        Ia = (-a * self.A + b * self.B + c * self.C) / (-a + b + c)
        # radius ra = Area / (s-a)
        s = (a + b + c) / 2
        area = 0.5 * abs(np.cross(self.B - self.A, self.C - self.A)[2])
        ra = area / (s - a)
        circ = Circle(radius=ra, color=TEAL, stroke_width=4).move_to(Ia)
        # touch point on BC
        # from Ia drop perpendicular to BC
        bc = self.C - self.B
        bc_u = bc / np.linalg.norm(bc)
        # normal pointing toward Ia side
        n = np.array([-bc_u[1], bc_u[0], 0])
        if np.dot(n, Ia - self.B) < 0:
            n = -n
        touch = Ia - n * ra
        # extensions of AB, AC beyond B and C
        ext_b = Line(self.A, self.B + 1.8 * (self.B - self.A), color=GREY, stroke_width=2)
        ext_c = Line(self.A, self.C + 1.8 * (self.C - self.A), color=GREY, stroke_width=2)
        self.play(Create(ext_b), Create(ext_c), run_time=1.0)
        cap = self.ja_text("外で接する", font_size=24).move_to(self.note)
        self.play(Create(circ), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        tdot = Dot(touch, color=ORANGE, radius=0.09)
        cap2 = self.ja_text("対辺に接す", font_size=24).move_to(self.note)
        self.play(FadeIn(tdot), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"r_a").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"r_a=\frac{\Delta}{s-a}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"r_a=\frac{\Delta}{s-a}").scale(1.0)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
