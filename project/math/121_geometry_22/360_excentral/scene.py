from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class ExcentralTriangle(PacedScene):
    """#360 傍心三角形：3 傍心を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("傍心三角形")
        self.draw_triangle()
        self.excenters()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 1.6
        self.B = LEFT * 2.2 + DOWN * 1.2
        self.C = RIGHT * 2.2 + DOWN * 1.2
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("元の三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def excenters(self):
        Ia = (self.B + self.C) / 2 + DOWN * 1.4
        Ib = (self.A + self.C) / 2 + RIGHT * 1.5
        Ic = (self.A + self.B) / 2 + LEFT * 1.5
        dots = VGroup(*[Dot(p, color=ORANGE, radius=0.1) for p in (Ia, Ib, Ic)])
        ex = Polygon(Ia, Ib, Ic, color=YELLOW, stroke_width=3)
        cap = self.ja_text("3 つの傍心", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.2)
        self.play(Create(ex), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("傍心三角形", font_size=24).move_to(self.note)
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
        formula = self.ja_text("傍心を頂点にする", font_size=30)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
