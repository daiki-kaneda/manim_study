from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Pappus(PacedScene):
    """#228 パップス：交差の 3 点は共線（約45秒）"""

    def construct(self):
        self.show_heading("パップスの定理")
        self.draw_lines()
        self.mark_collinear()
        self.show_formula()
        self.read(1.4)

    def draw_lines(self):
        # two lines
        self.L1 = Line(LEFT * 4.2 + UP * 1.5, RIGHT * 4.2 + UP * 0.85, color=GREY, stroke_width=2)
        self.L2 = Line(LEFT * 4.2 + DOWN * 1.6, RIGHT * 4.2 + DOWN * 0.9, color=GREY, stroke_width=2)
        # points on L1: A,B,C and L2: A',B',C'
        def on(line, t):
            return line.point_from_proportion(t)

        self.A, self.B, self.C = on(self.L1, 0.15), on(self.L1, 0.45), on(self.L1, 0.78)
        self.Ap, self.Bp, self.Cp = on(self.L2, 0.2), on(self.L2, 0.5), on(self.L2, 0.82)
        self.play(Create(self.L1), Create(self.L2), run_time=1.1)
        dots = VGroup(*[Dot(p, radius=0.08, color=YELLOW) for p in (self.A, self.B, self.C, self.Ap, self.Bp, self.Cp)])
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.08), run_time=1.3)
        note = self.ja_text("2 直線上", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def _intersect(self, p1, p2, q1, q2):
        A = np.array(p1[:2], dtype=float)
        B = np.array(p2[:2], dtype=float)
        C = np.array(q1[:2], dtype=float)
        D = np.array(q2[:2], dtype=float)

        def cross2(u, v):
            return u[0] * v[1] - u[1] * v[0]

        den = cross2(B - A, D - C)
        t = cross2(C - A, D - C) / den
        xy = A + t * (B - A)
        return np.array([xy[0], xy[1], 0.0])

    def mark_collinear(self):
        # X = AB' ∩ A'B, Y = AC' ∩ A'C, Z = BC' ∩ B'C
        X = self._intersect(self.A, self.Bp, self.Ap, self.B)
        Y = self._intersect(self.A, self.Cp, self.Ap, self.C)
        Z = self._intersect(self.B, self.Cp, self.Bp, self.C)
        segs = VGroup(
            Line(self.A, self.Bp, color=BLUE, stroke_width=2),
            Line(self.Ap, self.B, color=BLUE, stroke_width=2),
            Line(self.A, self.Cp, color=TEAL, stroke_width=2),
            Line(self.Ap, self.C, color=TEAL, stroke_width=2),
            Line(self.B, self.Cp, color=GREEN, stroke_width=2),
            Line(self.Bp, self.C, color=GREEN, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.08), run_time=1.6)
        pts = VGroup(Dot(X, color=ORANGE, radius=0.1), Dot(Y, color=ORANGE, radius=0.1), Dot(Z, color=ORANGE, radius=0.1))
        line = Line(X, Z, color=ORANGE, stroke_width=4)
        # extend a bit through Y
        line = Line(X + 0.15 * (X - Z), Z + 0.15 * (Z - X), color=ORANGE, stroke_width=4)
        cap = self.ja_text("3 点が共線", font_size=24).move_to(self.note)
        self.play(FadeIn(pts), Create(line), Transform(self.note, cap), run_time=1.5)
        self.read(0.45)

    def show_formula(self):
        formula = self.ja_text("交差の 3 点は一直線", font_size=28)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
