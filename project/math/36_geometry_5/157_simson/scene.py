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
    center = np.array([c[0], c[1], 0.0])
    return center, np.linalg.norm(center - p)


def _foot(p, a, b):
    ab = b - a
    t = np.dot((p - a)[:2], ab[:2]) / np.dot(ab[:2], ab[:2])
    return a + t * ab


class Simson(PacedScene):
    """#157 シムソン線（約50秒）"""

    def construct(self):
        self.show_heading("シムソン線")
        self.draw_triangle()
        self.pick_point()
        self.drop_feet()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.4 + UP * 1.85
        self.B = LEFT * 3.2 + DOWN * 1.35
        self.C = RIGHT * 1.9 + DOWN * 1.2
        self.O, self.R = _circum(self.A, self.B, self.C)
        circ = Circle(radius=self.R, color=GREY_B, stroke_width=2).move_to(self.O)
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(circ), run_time=1.3)
        self.play(Create(self.tri), run_time=1.3)
        labs = VGroup(
            MathTex("A", font_size=26).next_to(self.A, UP, buff=0.08),
            MathTex("B", font_size=26).next_to(self.B, DL, buff=0.08),
            MathTex("C", font_size=26).next_to(self.C, DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.55)
        self.read(0.3)

    def pick_point(self):
        # a point on the circumcircle, away from vertices
        ang = np.arctan2((self.A - self.O)[1], (self.A - self.O)[0]) + 0.85
        self.P = self.O + self.R * np.array([np.cos(ang), np.sin(ang), 0.0])
        note = self.ja_text("円周上の点", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(Dot(self.P, color=ORANGE, radius=0.09)), FadeIn(note), run_time=0.9)
        plab = MathTex("P", color=ORANGE, font_size=28).next_to(self.P, UR, buff=0.08)
        self.play(FadeIn(plab), run_time=0.4)
        self.read(0.35)
        self.note = note

    def drop_feet(self):
        Fa = _foot(self.P, self.B, self.C)
        Fb = _foot(self.P, self.C, self.A)
        Fc = _foot(self.P, self.A, self.B)
        drops = VGroup(
            DashedLine(self.P, Fa, color=GREY, stroke_width=2),
            DashedLine(self.P, Fb, color=GREY, stroke_width=2),
            DashedLine(self.P, Fc, color=GREY, stroke_width=2),
        )
        feet = VGroup(*[Dot(f, color=YELLOW, radius=0.07) for f in (Fa, Fb, Fc)])
        self.play(LaggedStart(*[Create(d) for d in drops], lag_ratio=0.2), run_time=1.7)
        self.play(FadeIn(feet), run_time=0.6)
        pts = [Fa, Fb, Fc]
        v = Fb - Fa
        ts = [np.dot((p - Fa)[:2], v[:2]) for p in pts]
        pmin, pmax = pts[int(np.argmin(ts))], pts[int(np.argmax(ts))]
        ln = Line(pmin - 0.2 * (pmax - pmin), pmax + 0.2 * (pmax - pmin), color=YELLOW, stroke_width=5)
        cap = self.ja_text("足は一直線", font_size=24).move_to(self.note)
        self.play(Create(ln), Transform(self.note, cap), run_time=1.5)
        self.read(0.5)

    def show_formula(self):
        formula = self.ja_text("三点は一直線", font_size=36)
        formula.to_edge(DOWN, buff=0.28)
        self.play(FadeIn(formula), run_time=1.5)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
