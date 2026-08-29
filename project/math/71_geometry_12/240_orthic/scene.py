from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class OrthicTriangle(PacedScene):
    """#240 垂足三角形は三垂線の足（約45秒）"""

    def construct(self):
        self.show_heading("垂足三角形")
        self.draw_triangle()
        self.drop_feet()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.8 + DOWN * 1.5
        self.B = RIGHT * 3.0 + DOWN * 1.4
        self.C = LEFT * 0.2 + UP * 2.05
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def _foot(self, p, a, b):
        ab = b - a
        t = np.dot(p - a, ab) / np.dot(ab, ab)
        return a + t * ab

    def drop_feet(self):
        D = self._foot(self.A, self.B, self.C)  # on BC
        E = self._foot(self.B, self.A, self.C)  # on CA
        F = self._foot(self.C, self.A, self.B)  # on AB
        alts = VGroup(
            DashedLine(self.A, D, color=GREY_B, stroke_width=2),
            DashedLine(self.B, E, color=GREY_B, stroke_width=2),
            DashedLine(self.C, F, color=GREY_B, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(l) for l in alts], lag_ratio=0.15), run_time=1.4)
        feet = VGroup(Dot(D, color=YELLOW, radius=0.09), Dot(E, color=YELLOW, radius=0.09), Dot(F, color=YELLOW, radius=0.09))
        self.play(FadeIn(feet), run_time=0.7)
        orth = Polygon(D, E, F, color=ORANGE, stroke_width=4)
        cap = self.ja_text("垂足を結ぶ", font_size=24).move_to(self.note)
        self.play(Create(orth), Transform(self.note, cap), run_time=1.4)
        self.read(0.45)

    def show_formula(self):
        formula = self.ja_text("三垂線の足が作る三角形", font_size=28)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
