from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Spieker(PacedScene):
    """#301 スピーカー中心：周長の重心＝中点三角形の内心（約45秒）"""

    def construct(self):
        self.show_heading("スピーカー中心")
        self.draw_triangle()
        self.medial()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1 + LEFT * 0.2
        self.B = LEFT * 2.5 + DOWN * 1.5
        self.C = RIGHT * 2.8 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def medial(self):
        M_a = (self.B + self.C) / 2
        M_b = (self.A + self.C) / 2
        M_c = (self.A + self.B) / 2
        med = Polygon(M_a, M_b, M_c, color=TEAL, stroke_width=3)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in (M_a, M_b, M_c)])
        cap = self.ja_text("中点三角形", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Create(med), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        Sp = (M_a + M_b + M_c) / 3
        inc = Circle(radius=0.45, color=ORANGE, stroke_width=3).move_to(Sp)
        cap2 = self.ja_text("その内心", font_size=24).move_to(self.note)
        self.play(Create(inc), FadeIn(Dot(Sp, color=RED, radius=0.1)), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"S\sim(b+c:c+a:a+b)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S\sim(b+c:c+a:a+b)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S\sim(b+c:c+a:a+b)").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
