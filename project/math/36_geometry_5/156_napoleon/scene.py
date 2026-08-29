from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


def _rot(p, o, deg):
    t = deg * DEGREES
    c, s = np.cos(t), np.sin(t)
    v = p - o
    return o + np.array([c * v[0] - s * v[1], s * v[0] + c * v[1], 0.0])


def _outward(p, q, other):
    r1 = _rot(q, p, 60)
    r2 = _rot(q, p, -60)
    if np.linalg.norm(r1 - other) >= np.linalg.norm(r2 - other):
        return r1
    return r2


class Napoleon(PacedScene):
    """#156 ナポレオンの定理（約50秒）"""

    def construct(self):
        self.show_heading("ナポレオンの定理")
        self.draw_triangle()
        self.outward_equilaterals()
        self.connect_centers()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.15 + UP * 2.0
        self.B = LEFT * 2.15 + UP * 0.2
        self.C = RIGHT * 1.7 + UP * 0.32
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.4)
        self.read(0.3)

    def outward_equilaterals(self):
        self.D = _outward(self.B, self.C, self.A)
        self.E = _outward(self.C, self.A, self.B)
        self.F = _outward(self.A, self.B, self.C)
        tris = VGroup(
            Polygon(self.B, self.C, self.D, color=BLUE, fill_opacity=0.22, stroke_width=2),
            Polygon(self.C, self.A, self.E, color=GREEN, fill_opacity=0.22, stroke_width=2),
            Polygon(self.A, self.B, self.F, color=YELLOW, fill_opacity=0.22, stroke_width=2),
        )
        note = self.ja_text("正三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(LaggedStart(*[FadeIn(t, scale=0.9) for t in tris], lag_ratio=0.22), FadeIn(note), run_time=2.2)
        self.read(0.4)
        self.note = note

    def connect_centers(self):
        g1 = (self.B + self.C + self.D) / 3
        g2 = (self.C + self.A + self.E) / 3
        g3 = (self.A + self.B + self.F) / 3
        dots = VGroup(*[Dot(g, color=ORANGE, radius=0.08) for g in (g1, g2, g3)])
        nap = Polygon(g1, g2, g3, color=ORANGE, stroke_width=5)
        cap = self.ja_text("同じ形", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), run_time=0.8)
        self.play(Create(nap), Transform(self.note, cap), run_time=1.6)
        self.read(0.5)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"|G_1G_2|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|G_1G_2|=|G_2G_3|=|G_3G_1|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|G_1G_2|=|G_2G_3|=|G_3G_1|").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
