from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Incircle(PacedScene):
    """#132 内接円と面積（約45秒）"""

    def construct(self):
        self.show_heading("内接円")
        self.draw_triangle()
        self.draw_circle()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.2 + UP * 1.95
        self.B = LEFT * 3.4 + DOWN * 1.5
        self.C = RIGHT * 1.4 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        self.read(0.35)

    def draw_circle(self):
        a = np.linalg.norm(self.B - self.C)
        b = np.linalg.norm(self.A - self.C)
        c = np.linalg.norm(self.A - self.B)
        P = (a * self.A + b * self.B + c * self.C) / (a + b + c)
        bc = self.C - self.B
        n = np.array([-bc[1], bc[0], 0.0])
        n = n / np.linalg.norm(n)
        mid = (self.B + self.C) / 2
        if np.dot(n, self.A - mid) < 0:
            n = -n
        r = abs(np.dot(P - self.B, n))
        inc = Circle(radius=r, color=YELLOW, stroke_width=4).move_to(P)
        self.play(Create(inc), FadeIn(Dot(P, color=YELLOW, radius=0.07)), run_time=1.6)
        foot = P - n * r
        rad = Line(P, foot, color=ORANGE, stroke_width=4)
        self.play(Create(rad), run_time=0.9)
        rlab = MathTex("r", color=ORANGE, font_size=30).next_to(rad, LEFT, buff=0.08)
        self.play(FadeIn(rlab), run_time=0.4)
        note = self.ja_text("内側に接する", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.5)

    def show_formula(self):
        formula = MathTex(r"A=r s").scale(1.25)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.3)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
