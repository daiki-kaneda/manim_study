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


class NinePoint(PacedScene):
    """#145 九点円（約55秒）"""

    def construct(self):
        self.show_heading("九点円")
        self.draw_triangle()
        self.midpoints()
        self.circle_and_feet()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.35 + UP * 2.05
        self.B = LEFT * 3.55 + DOWN * 1.5
        self.C = RIGHT * 2.05 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        labs = VGroup(
            MathTex("A", font_size=28).next_to(self.A, UP, buff=0.08),
            MathTex("B", font_size=28).next_to(self.B, DL, buff=0.08),
            MathTex("C", font_size=28).next_to(self.C, DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.65)
        self.read(0.35)

    def midpoints(self):
        self.Ma = (self.B + self.C) / 2
        self.Mb = (self.C + self.A) / 2
        self.Mc = (self.A + self.B) / 2
        dots = VGroup(
            Dot(self.Ma, color=YELLOW, radius=0.07),
            Dot(self.Mb, color=YELLOW, radius=0.07),
            Dot(self.Mc, color=YELLOW, radius=0.07),
        )
        note = self.ja_text("中点", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(LaggedStart(*[FadeIn(d, scale=0.3) for d in dots], lag_ratio=0.2), FadeIn(note), run_time=1.5)
        self.read(0.4)
        self.note = note

    def circle_and_feet(self):
        center, radius = _circum(self.Ma, self.Mb, self.Mc)
        circ = Circle(radius=radius, color=BLUE, stroke_width=4).move_to(center)
        cap = self.ja_text("三点を通る", font_size=24).move_to(self.note)
        self.play(Create(circ), Transform(self.note, cap), run_time=1.8)
        self.read(0.4)
        feet = VGroup(
            *[
                Dot(_foot(p, a, b), color=ORANGE, radius=0.07)
                for p, a, b in (
                    (self.A, self.B, self.C),
                    (self.B, self.C, self.A),
                    (self.C, self.A, self.B),
                )
            ]
        )
        alts = VGroup(
            DashedLine(self.A, _foot(self.A, self.B, self.C), color=GREY, stroke_width=2),
            DashedLine(self.B, _foot(self.B, self.C, self.A), color=GREY, stroke_width=2),
            DashedLine(self.C, _foot(self.C, self.A, self.B), color=GREY, stroke_width=2),
        )
        cap2 = self.ja_text("垂線の足も", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(ln) for ln in alts], lag_ratio=0.18), run_time=1.6)
        self.play(FadeIn(feet), Transform(self.note, cap2), run_time=1.1)
        self.read(0.5)

    def show_formula(self):
        formula = MathTex(r"N=\frac{O+H}{2}").scale(1.05)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
