from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class SpectralTheorem(PacedScene):
    """#153 対称行列は直交な固有方向（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.15 + DOWN * 0.1
        self.show_heading("スペクトル定理")
        self.draw_circle()
        self.stretch()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        ax = Line(self.origin + LEFT * 2.4, self.origin + RIGHT * 3.5, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.15, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        self.circ = Circle(radius=1.2, color=BLUE, stroke_width=4).move_to(self.origin)
        self.play(Create(ax), Create(ay), run_time=0.85)
        self.play(Create(self.circ), run_time=1.3)
        d = 1.2 / np.sqrt(2)
        self.q1 = Arrow(self.origin, self.origin + RIGHT * d + UP * d, buff=0, color=YELLOW, stroke_width=5)
        self.q2 = Arrow(self.origin, self.origin + RIGHT * d + DOWN * d, buff=0, color=GREEN, stroke_width=5)
        self.play(GrowArrow(self.q1), GrowArrow(self.q2), run_time=1.3)
        note = self.ja_text("直角の向き", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note

    def stretch(self):
        ell = Ellipse(width=3.4, height=1.35, color=YELLOW, stroke_width=5)
        ell.rotate(45 * DEGREES).move_to(self.origin)
        n1 = Arrow(self.origin, self.origin + RIGHT * 1.55 + UP * 1.55, buff=0, color=YELLOW, stroke_width=5)
        n2 = Arrow(self.origin, self.origin + RIGHT * 0.48 + DOWN * 0.48, buff=0, color=GREEN, stroke_width=5)
        cap = self.ja_text("向きに伸縮", font_size=24).move_to(self.note)
        self.play(
            Transform(self.circ, ell),
            Transform(self.q1, n1),
            Transform(self.q2, n2),
            Transform(self.note, cap),
            run_time=2.1,
        )
        self.read(0.45)
        labs = VGroup(
            MathTex(r"\lambda_1", color=YELLOW, font_size=30).next_to(n1.get_end(), UR, buff=0.08),
            MathTex(r"\lambda_2", color=GREEN, font_size=30).next_to(n2.get_end(), DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.7)
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
        eq = MathTex(r"A").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"A=Q\Lambda Q^{\mathsf T}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A=Q\Lambda Q^{\mathsf T}").scale(1.1)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
