from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class NumericalRange(PacedScene):
    """#275 数値域：レイリー商の値の集合（約45秒）"""

    def construct(self):
        self.show_heading("数値域")
        self.draw_region()
        self.mark_eigen()
        self.show_formula()
        self.read(1.4)

    def draw_region(self):
        self.O = LEFT * 0.6 + DOWN * 0.15
        ax = Line(self.O + LEFT * 2.6, self.O + RIGHT * 3.0, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 2.0, self.O + UP * 2.0, color=GREY, stroke_width=2)
        # elliptical numerical range
        self.region = Ellipse(width=3.6, height=2.4, color=BLUE, fill_opacity=0.25, stroke_width=3)
        self.region.move_to(self.O + RIGHT * 0.3 + UP * 0.2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.play(FadeIn(self.region), run_time=1.2)
        note = self.ja_text("値の集まり", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mark_eigen(self):
        eigs = [
            Dot(self.O + RIGHT * 1.4 + UP * 0.9, color=ORANGE, radius=0.1),
            Dot(self.O + LEFT * 0.5 + DOWN * 0.6, color=ORANGE, radius=0.1),
        ]
        cap = self.ja_text("固有値も", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in eigs], lag_ratio=0.15), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        # sample rayleigh points
        samples = VGroup(*[
            Dot(self.O + RIGHT * dx + UP * dy, color=YELLOW, radius=0.06)
            for dx, dy in [(0.2, 0.5), (1.0, -0.2), (0.6, 0.7), (-0.2, 0.1)]
        ])
        cap2 = self.ja_text("レイリー商", font_size=24).move_to(self.note)
        self.play(FadeIn(samples), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"W(A)=\{x^{*}Ax:\|x\|=1\}").scale(0.85)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
