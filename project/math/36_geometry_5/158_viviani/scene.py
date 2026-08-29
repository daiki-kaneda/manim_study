from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Viviani(PacedScene):
    """#158 ヴィヴィアニの定理（約50秒）"""

    def construct(self):
        self.show_heading("ヴィヴィアニ")
        self.draw_triangle()
        self.drop_from(self.P0, first=True)
        self.move_point()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        side = 4.6
        h = side * np.sqrt(3) / 2
        c = DOWN * 0.28
        self.A = c + UP * (h * 2 / 3)
        self.B = c + DOWN * (h / 3) + LEFT * (side / 2)
        self.C = c + DOWN * (h / 3) + RIGHT * (side / 2)
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        self.alt = Line(self.A, (self.B + self.C) / 2, color=GREY, stroke_width=2)
        self.play(Create(self.alt), run_time=0.8)
        self.P0 = 0.45 * self.A + 0.30 * self.B + 0.25 * self.C
        self.P1 = 0.22 * self.A + 0.48 * self.B + 0.30 * self.C
        self.read(0.3)

    def _foot(self, p, a, b):
        ab = b - a
        t = np.dot((p - a)[:2], ab[:2]) / np.dot(ab[:2], ab[:2])
        return a + t * ab

    def _drops(self, p):
        feet = (
            self._foot(p, self.B, self.C),
            self._foot(p, self.C, self.A),
            self._foot(p, self.A, self.B),
        )
        colors = (YELLOW, BLUE, GREEN)
        segs = VGroup(*[Line(p, f, color=c, stroke_width=5) for f, c in zip(feet, colors)])
        return segs, Dot(p, color=ORANGE, radius=0.09)

    def drop_from(self, p, first=False):
        segs, dot = self._drops(p)
        if first:
            self.segs = segs
            self.dot = dot
            note = self.ja_text("三本の垂線", font_size=24)
            note.to_edge(RIGHT, buff=0.3).shift(UP * 1.65)
            self.play(FadeIn(self.dot), run_time=0.5)
            self.play(LaggedStart(*[Create(s) for s in self.segs], lag_ratio=0.2), FadeIn(note), run_time=1.8)
            self.note = note
            self.read(0.4)
        else:
            nsegs, ndot = segs, dot
            cap = self.ja_text("動かしても", font_size=24).move_to(self.note)
            self.play(Transform(self.dot, ndot), Transform(self.segs, nsegs), Transform(self.note, cap), run_time=1.7)
            self.read(0.4)

    def move_point(self):
        self.drop_from(self.P1, first=False)
        cap = self.ja_text("和は高さ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), Indicate(self.alt, color=YELLOW), run_time=1.1)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"d_a+d_b+d_c=h").scale(1.05)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
