from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class Confocal(PacedScene):
    """#421 共焦点：楕円と双曲線が直交（約45秒）"""

    def construct(self):
        self.show_heading("共焦点")
        self.draw_curves()
        self.orthogonal()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_curves(self):
        self.O = ORIGIN + DOWN * 0.05
        ell = Ellipse(width=5.2, height=3.0, color=BLUE, stroke_width=3).move_to(self.O)
        hyp = ParametricFunction(
            lambda t: self.O + np.array([1.2 * np.cosh(t), 0.9 * np.sinh(t), 0]),
            t_range=[-1.1, 1.1], color=ORANGE, stroke_width=3,
        )
        hyp2 = ParametricFunction(
            lambda t: self.O + np.array([-1.2 * np.cosh(t), 0.9 * np.sinh(t), 0]),
            t_range=[-1.1, 1.1], color=ORANGE, stroke_width=3,
        )
        foci = VGroup(Dot(self.O + LEFT * 1.6, color=YELLOW, radius=0.1),
                      Dot(self.O + RIGHT * 1.6, color=YELLOW, radius=0.1))
        self.play(Create(ell), Create(hyp), Create(hyp2), FadeIn(foci), run_time=1.6)
        note = self.ja_text("同じ焦点", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.ell = ell

    def orthogonal(self):
        mark = Square(side_length=0.25, color=TEAL, stroke_width=3).move_to(self.O + RIGHT * 1.7 + UP * 0.85)
        cap = self.ja_text("交わる角", font_size=24).move_to(self.note)
        self.play(FadeIn(mark), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("直交する", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
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
        formula = self.ja_text("共焦点曲線は直交する", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
