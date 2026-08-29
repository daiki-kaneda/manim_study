from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Isodynamic(PacedScene):
    """#325 等力点：角の二等分線の等角共役の交点（約45秒）"""

    def construct(self):
        self.show_heading("等力点")
        self.draw_triangle()
        self.points()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.0 + LEFT * 0.2
        self.B = LEFT * 2.5 + DOWN * 1.5
        self.C = RIGHT * 2.8 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def points(self):
        # two isodynamic points approx
        S = (self.A + self.B + self.C) / 3
        p1 = S + LEFT * 0.35 + UP * 0.2
        p2 = S + RIGHT * 0.45 + DOWN * 0.15
        # arcs suggesting equal angles
        arcs = VGroup(
            Arc(radius=0.45, start_angle=-0.2, angle=0.8, color=TEAL).move_arc_center_to(self.A),
            Arc(radius=0.45, start_angle=3.5, angle=0.8, color=TEAL).move_arc_center_to(self.B),
        )
        cap = self.ja_text("等角な配置", font_size=24).move_to(self.note)
        self.play(Create(arcs[0]), Create(arcs[1]), Transform(self.note, cap), run_time=1.3)
        self.play(FadeIn(Dot(p1, color=ORANGE, radius=0.1)), FadeIn(Dot(p2, color=ORANGE, radius=0.1)), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("2 点ある", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("等角共役の交点", font_size=30)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
