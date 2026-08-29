from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class VanAubel(PacedScene):
    """#168 ファン・オーベル：正方形の中心を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("ファン・オーベル")
        self.draw_quad()
        self.outward_squares()
        self.connect_centers()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        self.A = LEFT * 1.05 + UP * 0.75
        self.B = RIGHT * 0.95 + UP * 0.55
        self.C = RIGHT * 1.1 + DOWN * 0.95
        self.D = LEFT * 1.15 + DOWN * 0.8
        self.quad = Polygon(self.A, self.B, self.C, self.D, color=WHITE, stroke_width=3)
        self.play(Create(self.quad), run_time=1.4)
        self.read(0.3)

    def _out_square(self, p, q):
        v = q - p
        n = np.array([-v[1], v[0], 0.0])
        # choose outward: away from quad centroid
        mid = (p + q) / 2
        cen = (self.A + self.B + self.C + self.D) / 4
        if np.dot(n[:2], (mid - cen)[:2]) < 0:
            n = -n
        r = p + n
        s = q + n
        return Polygon(p, q, s, r, color=BLUE, fill_opacity=0.18, stroke_width=2), (r + s + p + q) / 4

    def outward_squares(self):
        sides = [(self.A, self.B), (self.B, self.C), (self.C, self.D), (self.D, self.A)]
        colors = [BLUE, TEAL, GREEN, YELLOW]
        self.centers = []
        sqs = VGroup()
        for (p, q), col in zip(sides, colors):
            poly, c = self._out_square(p, q)
            poly.set_color(col)
            sqs.add(poly)
            self.centers.append(c)
        note = self.ja_text("正方形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(LaggedStart(*[FadeIn(s, scale=0.9) for s in sqs], lag_ratio=0.18), FadeIn(note), run_time=2.2)
        self.read(0.35)
        self.note = note

    def connect_centers(self):
        dots = VGroup(*[Dot(c, color=ORANGE, radius=0.08) for c in self.centers])
        e1 = Line(self.centers[0], self.centers[2], color=ORANGE, stroke_width=5)
        e2 = Line(self.centers[1], self.centers[3], color=ORANGE, stroke_width=5)
        cap = self.ja_text("中心を結ぶ", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), run_time=0.7)
        self.play(Create(e1), Create(e2), Transform(self.note, cap), run_time=1.5)
        self.read(0.35)
        cap2 = self.ja_text("等長で直角", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"|P_1P_3|=|P_2P_4|,\quad P_1P_3\perp P_2P_4").scale(0.72)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
