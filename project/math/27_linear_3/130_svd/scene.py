from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class SVDStretch(PacedScene):
    """#130 行列は円を楕円にする（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.3 + DOWN * 0.15
        self.show_heading("特異値")
        self.draw_circle()
        self.stretch()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        ax = Line(self.origin + LEFT * 2.3, self.origin + RIGHT * 3.3, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.0, self.origin + UP * 2.15, color=GREY, stroke_width=2)
        self.circ = Circle(radius=1.15, color=BLUE, stroke_width=4).move_to(self.origin)
        self.play(Create(ax), Create(ay), run_time=0.9)
        self.play(Create(self.circ), run_time=1.4)
        note = self.ja_text("単位円", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.4)
        self.note = note

    def stretch(self):
        ell = Ellipse(width=3.6, height=1.5, color=YELLOW, stroke_width=5).move_to(self.origin)
        cap = self.ja_text("伸びる向き", font_size=24).move_to(self.note)
        self.play(Transform(self.circ, ell), Transform(self.note, cap), run_time=2.0)
        self.read(0.45)
        a = Arrow(self.origin, self.origin + RIGHT * 1.8, buff=0, color=ORANGE, stroke_width=4)
        b = Arrow(self.origin, self.origin + UP * 0.75, buff=0, color=GREEN, stroke_width=4)
        la = MathTex(r"\sigma_1", color=ORANGE, font_size=30).next_to(a.get_end(), DOWN, buff=0.1)
        lb = MathTex(r"\sigma_2", color=GREEN, font_size=30).next_to(b.get_end(), LEFT, buff=0.1)
        self.play(GrowArrow(a), GrowArrow(b), FadeIn(la), FadeIn(lb), run_time=1.4)
        self.read(0.5)

    def show_formula(self):
        formula = MathTex(r"A=U\Sigma V^{\mathsf T}").scale(1.1)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
