from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


def _circle_through(p, q, r):
    """Return Circle through three points (as Manim Circle)."""
    A = np.array(p, dtype=float)
    B = np.array(q, dtype=float)
    C = np.array(r, dtype=float)
    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    ux = ((A[0] ** 2 + A[1] ** 2) * (B[1] - C[1]) + (B[0] ** 2 + B[1] ** 2) * (C[1] - A[1]) + (C[0] ** 2 + C[1] ** 2) * (A[1] - B[1])) / D
    uy = ((A[0] ** 2 + A[1] ** 2) * (C[0] - B[0]) + (B[0] ** 2 + B[1] ** 2) * (A[0] - C[0]) + (C[0] ** 2 + C[1] ** 2) * (B[0] - A[0])) / D
    center = np.array([ux, uy, 0.0])
    rad = np.linalg.norm(center - A)
    return Circle(radius=rad, color=WHITE, stroke_width=3).move_to(center)


class Miquel(PacedScene):
    """#193 ミケル：辺上の点から 3 円は共点（約45秒）"""

    def construct(self):
        self.show_heading("ミケルの定理")
        self.draw_triangle()
        self.draw_circles()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 3.0 + DOWN * 1.5
        self.B = RIGHT * 3.1 + DOWN * 1.5
        self.C = LEFT * 0.2 + UP * 2.0
        tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        # points on sides
        self.D = self.B * 0.45 + self.C * 0.55  # on BC
        self.E = self.C * 0.4 + self.A * 0.6   # on CA
        self.F = self.A * 0.35 + self.B * 0.65  # on AB
        pts = VGroup(*[Dot(p, radius=0.08, color=YELLOW) for p in (self.D, self.E, self.F)])
        self.play(Create(tri), run_time=1.3)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in pts], lag_ratio=0.15), run_time=1.2)
        note = self.ja_text("辺上の点", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def draw_circles(self):
        c1 = _circle_through(self.A, self.E, self.F)
        c1.set_color(BLUE)
        c2 = _circle_through(self.B, self.F, self.D)
        c2.set_color(TEAL)
        c3 = _circle_through(self.C, self.D, self.E)
        c3.set_color(ORANGE)
        # Miquel point: intersection of c1 and c2 other than F
        # compute numerically
        o1, r1 = c1.get_center(), c1.radius
        o2, r2 = c2.get_center(), c2.radius
        d = np.linalg.norm(o2 - o1)
        a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
        h = np.sqrt(max(r1 ** 2 - a ** 2, 0))
        mid = o1 + a * (o2 - o1) / d
        perp = np.array([-(o2 - o1)[1], (o2 - o1)[0], 0]) / d
        p_a = mid + h * perp
        p_b = mid - h * perp
        # pick the one farther from F
        M = p_a if np.linalg.norm(p_a - self.F) > np.linalg.norm(p_b - self.F) else p_b
        self.play(Create(c1), run_time=1.1)
        self.play(Create(c2), run_time=1.1)
        self.play(Create(c3), run_time=1.1)
        meet = Dot(M, color=RED, radius=0.11)
        cap = self.ja_text("一点で交わる", font_size=24).move_to(self.note)
        self.play(FadeIn(meet, scale=0.5), Transform(self.note, cap), run_time=1.2)
        self.read(0.45)

    def show_formula(self):
        formula = self.ja_text("3 円はミケル点で交わる", font_size=28)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
