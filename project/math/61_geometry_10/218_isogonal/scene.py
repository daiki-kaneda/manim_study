from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class IsogonalConjugate(PacedScene):
    """#218 等角共役は角の鏡映（約45秒）"""

    def construct(self):
        self.show_heading("等角共役")
        self.draw_triangle()
        self.show_conjugate()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.8 + DOWN * 1.5
        self.B = RIGHT * 2.9 + DOWN * 1.4
        self.C = ORIGIN + UP * 2.05
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        # point P inside
        self.P = 0.35 * self.A + 0.3 * self.B + 0.35 * self.C
        self.play(Create(self.tri), run_time=1.2)
        self.play(FadeIn(Dot(self.P, color=YELLOW, radius=0.1)), run_time=0.6)
        pl = MathTex("P", color=YELLOW, font_size=28).next_to(self.P, UR, buff=0.08)
        self.play(FadeIn(pl), run_time=0.35)
        note = self.ja_text("内点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def _reflect_ray(self, vertex, side1, side2, point):
        """Reflect the direction vertex->point across the angle bisector at vertex."""
        v1 = side1 - vertex
        v2 = side2 - vertex
        u1 = v1 / np.linalg.norm(v1)
        u2 = v2 / np.linalg.norm(v2)
        bis = u1 + u2
        bis = bis / np.linalg.norm(bis)
        d = point - vertex
        # reflect d across bis: 2 (d·bis) bis - d
        refl = 2 * np.dot(d, bis) * bis - d
        return refl

    def show_conjugate(self):
        # lines from vertices to P
        lines_p = VGroup(
            Line(self.A, self.P, color=BLUE, stroke_width=3),
            Line(self.B, self.P, color=BLUE, stroke_width=3),
            Line(self.C, self.P, color=BLUE, stroke_width=3),
        )
        self.play(LaggedStart(*[Create(l) for l in lines_p], lag_ratio=0.15), run_time=1.3)
        cap = self.ja_text("角を鏡る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.25)
        # isogonal: reflect each cevian; intersection is P*
        # Construct reflected directions and find intersection of two
        da = self._reflect_ray(self.A, self.B, self.C, self.P)
        db = self._reflect_ray(self.B, self.A, self.C, self.P)
        # line A + s da and B + t db
        # solve A + s da = B + t db
        M = np.column_stack([da[:2], -db[:2]])
        try:
            st = np.linalg.solve(M, (self.B - self.A)[:2])
            Pstar = self.A + st[0] * da
        except np.linalg.LinAlgError:
            Pstar = 0.25 * self.A + 0.4 * self.B + 0.35 * self.C
        lines_q = VGroup(
            Line(self.A, Pstar, color=ORANGE, stroke_width=3),
            Line(self.B, Pstar, color=ORANGE, stroke_width=3),
            Line(self.C, Pstar, color=ORANGE, stroke_width=3),
        )
        self.play(LaggedStart(*[Create(l) for l in lines_q], lag_ratio=0.12), run_time=1.4)
        q = Dot(Pstar, color=ORANGE, radius=0.1)
        ql = MathTex(r"P^{*}", color=ORANGE, font_size=28).next_to(Pstar, UL, buff=0.08)
        cap2 = self.ja_text("共役点", font_size=24).move_to(self.note)
        self.play(FadeIn(q), FadeIn(ql), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("等角なチェバの交点", font_size=28)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
