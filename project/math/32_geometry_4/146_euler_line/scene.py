from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


def _circum(p, q, r):
    A = np.array(
        [
            [2 * (q[0] - p[0]), 2 * (q[1] - p[1])],
            [2 * (r[0] - p[0]), 2 * (r[1] - p[1])],
        ]
    )
    b = np.array(
        [
            q[0] ** 2 + q[1] ** 2 - p[0] ** 2 - p[1] ** 2,
            r[0] ** 2 + r[1] ** 2 - p[0] ** 2 - p[1] ** 2,
        ]
    )
    c = np.linalg.solve(A, b)
    return np.array([c[0], c[1], 0.0])


class EulerLine(PacedScene):
    """#146 オイラー線（約50秒）"""

    def construct(self):
        self.show_heading("オイラー線")
        self.draw_triangle()
        self.three_centers()
        self.draw_line()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.45 + UP * 2.1
        self.B = LEFT * 3.45 + DOWN * 1.55
        self.C = RIGHT * 2.15 + DOWN * 1.25
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        self.read(0.3)

    def three_centers(self):
        self.O = _circum(self.A, self.B, self.C)
        self.G = (self.A + self.B + self.C) / 3
        self.H = 3 * self.G - 2 * self.O
        pts = [
            (self.O, "O", BLUE, "外心"),
            (self.G, "G", YELLOW, "重心"),
            (self.H, "H", ORANGE, "垂心"),
        ]
        self.note = self.ja_text(" ", font_size=24).to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.add(self.note)
        self.dots = VGroup()
        for p, name, color, jp in pts:
            d = Dot(p, color=color, radius=0.09)
            lab = MathTex(name, color=color, font_size=30).next_to(d, UR, buff=0.08)
            cap = self.ja_text(jp, font_size=24).move_to(self.note)
            self.play(FadeIn(d, scale=0.4), FadeIn(lab), Transform(self.note, cap), run_time=1.15)
            self.dots.add(d)
            self.read(0.28)

    def draw_line(self):
        ln = Line(self.H + 0.35 * (self.H - self.O), self.O + 0.25 * (self.O - self.H), color=TEAL, stroke_width=4)
        cap = self.ja_text("一直線", font_size=24).move_to(self.note)
        self.play(Create(ln), Transform(self.note, cap), run_time=1.6)
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
        eq = MathTex(r"HG").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"HG=2\,GO").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"HG=2\,GO").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
