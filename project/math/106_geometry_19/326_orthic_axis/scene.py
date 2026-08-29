from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class OrthicAxis(PacedScene):
    """#326 垂足軸：垂足三角形の辺の交点が作る線（約45秒）"""

    def construct(self):
        self.show_heading("垂足軸")
        self.draw_orthic()
        self.axis()
        self.show_formula()
        self.read(1.4)

    def draw_orthic(self):
        self.A = UP * 2.1 + LEFT * 0.4
        self.B = LEFT * 2.4 + DOWN * 1.5
        self.C = RIGHT * 2.9 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        # feet approx
        self.Ha = (self.B + self.C) / 2 + UP * 0.15
        self.Hb = (self.A + self.C) / 2 + LEFT * 0.2
        self.Hc = (self.A + self.B) / 2 + RIGHT * 0.15
        orth = Polygon(self.Ha, self.Hb, self.Hc, color=TEAL, stroke_width=3)
        self.play(Create(self.tri), run_time=1.0)
        self.play(Create(orth), FadeIn(VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in (self.Ha, self.Hb, self.Hc)])), run_time=1.3)
        note = self.ja_text("垂足三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def axis(self):
        # side lines of orthic extended - show one axis line
        L = Line(LEFT * 3.2 + UP * 0.3, RIGHT * 3.2 + DOWN * 0.5, color=ORANGE, stroke_width=4)
        cap = self.ja_text("辺の延長", font_size=24).move_to(self.note)
        self.play(Create(L), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("軸になる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("辺が定める軸", font_size=28)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
