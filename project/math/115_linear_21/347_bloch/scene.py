from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class BlochSphere(PacedScene):
    """#347 ブロッホ球：2 準位の純粋状態（約45秒）"""

    def construct(self):
        self.show_heading("ブロッホ球")
        self.draw_sphere()
        self.state_vector()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_sphere(self):
        self.O = LEFT * 0.4 + DOWN * 0.15
        # 2d projection of sphere
        circ = Circle(radius=2.0, color=GREY, stroke_width=3).move_to(self.O)
        eq = Ellipse(width=4.0, height=1.2, color=GREY, stroke_width=2).move_to(self.O)
        ax = Line(self.O + DOWN * 2.2, self.O + UP * 2.2, color=GREY, stroke_width=2)
        self.play(Create(circ), Create(eq), Create(ax), run_time=1.4)
        note = self.ja_text("単位球", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def state_vector(self):
        tip = self.O + RIGHT * 1.1 + UP * 1.4
        v = Arrow(self.O, tip, buff=0, color=ORANGE, stroke_width=5)
        cap = self.ja_text("状態ベクトル", font_size=24).move_to(self.note)
        self.play(GrowArrow(v), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("純粋状態", font_size=24).move_to(self.note)
        self.play(FadeIn(Dot(tip, color=YELLOW, radius=0.1)), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"|\psi\rangle\leftrightarrow\vec r\in S^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|\psi\rangle\leftrightarrow\vec r\in S^{2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|\psi\rangle\leftrightarrow\vec r\in S^{2}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
