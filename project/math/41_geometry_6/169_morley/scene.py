from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Morley(PacedScene):
    """#169 モーリーの定理：三等分線の内側は正三角（約50秒）"""

    def construct(self):
        self.show_heading("モーリーの定理")
        self.draw_triangle()
        self.trisect()
        self.inner_triangle()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.2 + UP * 2.05
        self.B = LEFT * 3.3 + DOWN * 1.45
        self.C = RIGHT * 2.0 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.4)
        labs = VGroup(
            MathTex("A", font_size=26).next_to(self.A, UP, buff=0.08),
            MathTex("B", font_size=26).next_to(self.B, DL, buff=0.08),
            MathTex("C", font_size=26).next_to(self.C, DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.55)
        self.read(0.3)

    def _ang(self, v):
        return np.arctan2(v[1], v[0])

    def _ray(self, o, ang, length=4.5):
        d = np.array([np.cos(ang), np.sin(ang), 0.0])
        return o + length * d

    def _hit(self, p, q, a, b):
        d1 = q - p
        d2 = b - a
        mat = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
        t = np.linalg.solve(mat, (a - p)[:2])[0]
        return p + t * d1

    def trisect(self):
        # trisect angles at A, B, C and take adjacent intersections for Morley triangle
        ab = self._ang(self.B - self.A)
        ac = self._ang(self.C - self.A)
        # unwrap
        def unwrap(a0, a1):
            while a1 < a0:
                a1 += 2 * np.pi
            if a1 - a0 > np.pi:
                a0, a1 = a1, a0 + 2 * np.pi
            return a0, a1

        a0, a1 = unwrap(ab, ac)
        b0, b1 = unwrap(self._ang(self.C - self.B), self._ang(self.A - self.B))
        c0, c1 = unwrap(self._ang(self.A - self.C), self._ang(self.B - self.C))
        da, db, dc = a1 - a0, b1 - b0, c1 - c0
        # near-side trisectors (adjacent pairs form the Morley triangle)
        A_ab = self._ray(self.A, a0 + da / 3)
        A_ac = self._ray(self.A, a0 + 2 * da / 3)
        B_bc = self._ray(self.B, b0 + db / 3)
        B_ba = self._ray(self.B, b0 + 2 * db / 3)
        C_ca = self._ray(self.C, c0 + dc / 3)
        C_cb = self._ray(self.C, c0 + 2 * dc / 3)
        rays = VGroup(
            Line(self.A, A_ab, color=GREY_B, stroke_width=2),
            Line(self.A, A_ac, color=GREY_B, stroke_width=2),
            Line(self.B, B_bc, color=GREY_B, stroke_width=2),
            Line(self.B, B_ba, color=GREY_B, stroke_width=2),
            Line(self.C, C_ca, color=GREY_B, stroke_width=2),
            Line(self.C, C_cb, color=GREY_B, stroke_width=2),
        )
        note = self.ja_text("三等分", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(LaggedStart(*[Create(r) for r in rays], lag_ratio=0.08), FadeIn(note), run_time=2.2)
        self.read(0.35)
        self.note = note
        self.P = self._hit(self.A, A_ab, self.B, B_ba)
        self.Q = self._hit(self.B, B_bc, self.C, C_cb)
        self.R = self._hit(self.C, C_ca, self.A, A_ac)

    def inner_triangle(self):
        dots = VGroup(
            Dot(self.P, color=ORANGE, radius=0.08),
            Dot(self.Q, color=ORANGE, radius=0.08),
            Dot(self.R, color=ORANGE, radius=0.08),
        )
        inner = Polygon(self.P, self.Q, self.R, color=YELLOW, stroke_width=5)
        cap = self.ja_text("正三角", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), run_time=0.7)
        self.play(Create(inner), Transform(self.note, cap), run_time=1.5)
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
        eq = MathTex(r"|PQ|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|PQ|=|QR|=|RP|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|PQ|=|QR|=|RP|").scale(1.0)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
