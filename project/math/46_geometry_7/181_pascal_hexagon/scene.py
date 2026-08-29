from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class PascalHexagon(PacedScene):
    """#181 パスカル：円上の六角形の対辺は共線（約50秒）"""

    def construct(self):
        self.show_heading("パスカルの定理")
        self.draw_hexagon()
        self.opposite_sides()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_hexagon(self):
        self.O = LEFT * 0.3 + DOWN * 0.1
        self.R = 2.0
        circ = Circle(radius=self.R, color=GREY_B, stroke_width=2).move_to(self.O)
        # labeling order (not sorted around the circle) so opposite-side
        # intersections stay on screen
        angs = [3.10520166, 6.002434, 4.11898957, 2.18302689, 4.45354394, 0.26782563]
        self.pts = [self.O + self.R * np.array([np.cos(a), np.sin(a), 0.0]) for a in angs]
        self.play(Create(circ), run_time=1.2)
        dots = VGroup(*[Dot(p, color=WHITE, radius=0.07) for p in self.pts])
        self.play(FadeIn(dots), run_time=0.7)
        # draw hexagon edges in label order
        edges = VGroup(*[
            Line(self.pts[i], self.pts[(i + 1) % 6], color=BLUE, stroke_width=3)
            for i in range(6)
        ])
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.12), run_time=1.8)
        note = self.ja_text("円上の六点", font_size=24)
        note.to_edge(RIGHT, buff=0.3).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def _hit(self, p, q, a, b):
        d1 = q - p
        d2 = b - a
        mat = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
        t = np.linalg.solve(mat, (a - p)[:2])[0]
        return p + t * d1

    def opposite_sides(self):
        P = self._hit(self.pts[0], self.pts[1], self.pts[3], self.pts[4])
        Q = self._hit(self.pts[1], self.pts[2], self.pts[4], self.pts[5])
        R = self._hit(self.pts[2], self.pts[3], self.pts[5], self.pts[0])
        pairs = [
            (0, 1, 3, 4, YELLOW),
            (1, 2, 4, 5, TEAL),
            (2, 3, 5, 0, ORANGE),
        ]
        lines = VGroup()
        for i, j, k, l, col in pairs:
            lines.add(Line(self.pts[i], self.pts[j], color=col, stroke_width=5))
            lines.add(Line(self.pts[k], self.pts[l], color=col, stroke_width=5))
        cap = self.ja_text("対辺", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(ln) for ln in lines], lag_ratio=0.1), Transform(self.note, cap), run_time=1.8)
        self.read(0.3)
        dots = VGroup(*[Dot(p, color=RED, radius=0.08) for p in (P, Q, R)])
        v = Q - P
        ts = [np.dot((p - P)[:2], v[:2]) for p in (P, Q, R)]
        order = [P, Q, R]
        pmin, pmax = order[int(np.argmin(ts))], order[int(np.argmax(ts))]
        ln = Line(pmin - 0.25 * (pmax - pmin), pmax + 0.25 * (pmax - pmin), color=RED, stroke_width=5)
        cap2 = self.ja_text("交点は共線", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Create(ln), Transform(self.note, cap2), run_time=1.5)
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
        formula = self.ja_text("対辺の交点は共線", font_size=34)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.4)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
