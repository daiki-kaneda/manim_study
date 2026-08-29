from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Desargues(PacedScene):
    """#180 デザルグ：透視があれば対応辺は共線（約50秒）"""

    def construct(self):
        self.show_heading("デザルグの定理")
        self.draw_perspective()
        self.extend_sides()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_perspective(self):
        self.O = LEFT * 3.0 + UP * 1.4
        dirs = [
            np.array([1.0, -0.1, 0.0]),
            np.array([0.55, -0.95, 0.0]),
            np.array([1.2, -0.55, 0.0]),
        ]
        dirs = [d / np.linalg.norm(d) for d in dirs]
        s1, s2 = (1.5, 3.0, 2.2), (4.5, 3.4, 3.8)
        self.A, self.B, self.C = [self.O + s * d for s, d in zip(s1, dirs)]
        self.A2, self.B2, self.C2 = [self.O + s * d for s, d in zip(s2, dirs)]
        rays = VGroup(*[
            Line(self.O, p + 0.2 * (p - self.O), color=GREY, stroke_width=2)
            for p in (self.A2, self.B2, self.C2)
        ])
        t1 = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        t2 = Polygon(self.A2, self.B2, self.C2, color=YELLOW, stroke_width=3)
        self.play(FadeIn(Dot(self.O, color=ORANGE, radius=0.09)), run_time=0.5)
        olab = MathTex("O", color=ORANGE, font_size=28).next_to(self.O, UL, buff=0.08)
        self.play(FadeIn(olab), Create(rays), run_time=1.3)
        self.play(Create(t1), run_time=1.1)
        self.play(Create(t2), run_time=1.1)
        note = self.ja_text("透視", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def _hit(self, p, q, a, b):
        d1 = q - p
        d2 = b - a
        mat = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
        t = np.linalg.solve(mat, (a - p)[:2])[0]
        return p + t * d1

    def extend_sides(self):
        P = self._hit(self.A, self.B, self.A2, self.B2)
        Q = self._hit(self.B, self.C, self.B2, self.C2)
        R = self._hit(self.C, self.A, self.C2, self.A2)
        extras = VGroup(
            DashedLine(self.A, P, color=GREY_B, stroke_width=2),
            DashedLine(self.A2, P, color=GREY_B, stroke_width=2),
            DashedLine(self.B, Q, color=GREY_B, stroke_width=2),
            DashedLine(self.B2, Q, color=GREY_B, stroke_width=2),
            DashedLine(self.C, R, color=GREY_B, stroke_width=2),
            DashedLine(self.C2, R, color=GREY_B, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(e) for e in extras], lag_ratio=0.08), run_time=1.6)
        dots = VGroup(*[Dot(p, color=TEAL, radius=0.08) for p in (P, Q, R)])
        v = Q - P
        ts = [np.dot((p - P)[:2], v[:2]) for p in (P, Q, R)]
        order = [P, Q, R]
        pmin, pmax = order[int(np.argmin(ts))], order[int(np.argmax(ts))]
        line = Line(pmin - 0.2 * (pmax - pmin), pmax + 0.2 * (pmax - pmin), color=TEAL, stroke_width=5)
        cap = self.ja_text("対応辺", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.0)
        cap2 = self.ja_text("一直線", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap2), run_time=1.3)
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
        formula = self.ja_text("交点は一直線", font_size=36)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.4)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
