from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Trilinear(PacedScene):
    """#300 三線座標：辺への符号付き距離比（約45秒）"""

    def construct(self):
        self.show_heading("三線座標")
        self.draw_triangle()
        self.distances()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.6 + DOWN * 1.5
        self.C = RIGHT * 2.6 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.P = (self.A + self.B + self.C) / 3 + LEFT * 0.3 + UP * 0.2
        self.play(Create(self.tri), run_time=1.1)
        self.play(FadeIn(Dot(self.P, color=ORANGE, radius=0.1)), run_time=0.6)
        note = self.ja_text("点 P", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def distances(self):
        # perpendicular feet approx toward side midpoints
        feet = [(self.B + self.C) / 2, (self.A + self.C) / 2, (self.A + self.B) / 2]
        cols = [YELLOW, TEAL, ORANGE]
        segs = VGroup(*[Line(self.P, f, color=c, stroke_width=3) for f, c in zip(feet, cols)])
        cap = self.ja_text("辺までの距離", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.12), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("比が座標", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"P").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P=(x:y:z)\propto(d_a:d_b:d_c)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P=(x:y:z)\propto(d_a:d_b:d_c)").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
