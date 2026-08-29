from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Menelaus(PacedScene):
    """#147 メネラウスの定理（約50秒）"""

    def construct(self):
        self.show_heading("メネラウスの定理")
        self.draw_triangle()
        self.draw_transversal()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.2 + UP * 2.05
        self.B = LEFT * 3.4 + DOWN * 1.45
        self.C = RIGHT * 1.7 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        labs = VGroup(
            MathTex("A", font_size=28).next_to(self.A, UP, buff=0.08),
            MathTex("B", font_size=28).next_to(self.B, DL, buff=0.08),
            MathTex("C", font_size=28).next_to(self.C, DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.65)
        self.read(0.35)

    def _hit(self, p, q, a, b):
        d1 = q - p
        d2 = b - a
        mat = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
        t = np.linalg.solve(mat, (a - p)[:2])[0]
        return p + t * d1

    def draw_transversal(self):
        F = 0.38 * self.A + 0.62 * self.B
        E = self.C + 0.42 * (self.C - self.A)
        D = self._hit(F, E, self.B, self.C)
        start = F + 0.18 * (F - E)
        end = E + 0.18 * (E - F)
        line = Line(start, end, color=YELLOW, stroke_width=5)
        self.play(Create(line), run_time=1.8)
        dots = VGroup(
            Dot(F, color=ORANGE, radius=0.08),
            Dot(D, color=ORANGE, radius=0.08),
            Dot(E, color=ORANGE, radius=0.08),
        )
        names = VGroup(
            MathTex("F", font_size=28).next_to(F, LEFT, buff=0.08),
            MathTex("D", font_size=28).next_to(D, DOWN, buff=0.08),
            MathTex("E", font_size=28).next_to(E, UR, buff=0.08),
        )
        self.play(FadeIn(dots), FadeIn(names), run_time=1.1)
        note = self.ja_text("横断線", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.5)
        self.read(0.45)
        cap = self.ja_text("比の積は 1", font_size=24).move_to(note)
        self.play(Transform(note, cap), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\frac{AF}{FB}\cdot\frac{BD}{DC}\cdot\frac{CE}{EA}=1").scale(0.82)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
