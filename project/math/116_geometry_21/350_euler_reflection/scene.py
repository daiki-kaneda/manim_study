from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class EulerReflection(PacedScene):
    """#350 オイラー反射点：垂線の足の反射が一点（約45秒）"""

    def construct(self):
        self.show_heading("オイラー反射点")
        self.draw_triangle()
        self.reflect()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.0 + LEFT * 0.3
        self.B = LEFT * 2.5 + DOWN * 1.5
        self.C = RIGHT * 2.7 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.H = (self.A + self.B + self.C) / 3 + DOWN * 0.2  # orthocenter approx
        self.play(Create(self.tri), FadeIn(Dot(self.H, color=ORANGE, radius=0.1)), run_time=1.3)
        note = self.ja_text("垂心", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def reflect(self):
        feet = [(self.B + self.C) / 2, (self.A + self.C) / 2, (self.A + self.B) / 2]
        refls = [2 * f - self.H for f in feet]
        lines = VGroup(*[DashedLine(self.H, r, color=GREY, stroke_width=2) for r in refls])
        dots = VGroup(*[Dot(r, color=YELLOW, radius=0.09) for r in refls])
        # concurrency point of reflections lines - use another point
        E = (refls[0] + refls[1] + refls[2]) / 3
        cap = self.ja_text("足を反射", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.1), FadeIn(dots), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("一点に集まる", font_size=24).move_to(self.note)
        self.play(FadeIn(Dot(E, color=RED, radius=0.11), scale=0.5), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("反射点が一致", font_size=30)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
