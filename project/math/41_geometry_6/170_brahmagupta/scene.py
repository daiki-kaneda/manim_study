from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Brahmagupta(PacedScene):
    """#170 ブラフマグプタ：円に内接する四角形の面積（約45秒）"""

    def construct(self):
        self.show_heading("ブラフマグプタ")
        self.draw_cyclic()
        self.mark_sides()
        self.show_formula()
        self.read(1.4)

    def draw_cyclic(self):
        self.O = LEFT * 0.6 + DOWN * 0.1
        self.R = 2.0
        circ = Circle(radius=self.R, color=GREY_B, stroke_width=2).move_to(self.O)
        angs = [0.35, 1.55, 3.35, 5.0]
        pts = [self.O + self.R * np.array([np.cos(a), np.sin(a), 0.0]) for a in angs]
        self.A, self.B, self.C, self.D = pts
        self.quad = Polygon(*pts, color=WHITE, stroke_width=3, fill_opacity=0.2, fill_color=BLUE)
        self.play(Create(circ), run_time=1.2)
        self.play(FadeIn(self.quad), run_time=1.3)
        labs = VGroup(
            MathTex("A", font_size=26).next_to(self.A, UR, buff=0.08),
            MathTex("B", font_size=26).next_to(self.B, UL, buff=0.08),
            MathTex("C", font_size=26).next_to(self.C, DL, buff=0.08),
            MathTex("D", font_size=26).next_to(self.D, DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.6)
        note = self.ja_text("円に内接", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def mark_sides(self):
        sides = VGroup(
            Line(self.A, self.B, color=YELLOW, stroke_width=6),
            Line(self.B, self.C, color=TEAL, stroke_width=6),
            Line(self.C, self.D, color=GREEN, stroke_width=6),
            Line(self.D, self.A, color=ORANGE, stroke_width=6),
        )
        names = VGroup(
            MathTex("a", color=YELLOW, font_size=28).next_to(sides[0], UP, buff=0.08),
            MathTex("b", color=TEAL, font_size=28).next_to(sides[1], LEFT, buff=0.08),
            MathTex("c", color=GREEN, font_size=28).next_to(sides[2], DOWN, buff=0.08),
            MathTex("d", color=ORANGE, font_size=28).next_to(sides[3], RIGHT, buff=0.08),
        )
        cap = self.ja_text("四辺", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(s) for s in sides], lag_ratio=0.15), Transform(self.note, cap), run_time=1.8)
        self.play(FadeIn(names), run_time=0.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"K=\sqrt{(s-a)(s-b)(s-c)(s-d)}").scale(0.85)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
