from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class LyapunovEquation(PacedScene):
    """#321 リアプノフ方程式：安定性の二次形式（約45秒）"""

    def construct(self):
        self.show_heading("リアプノフ方程式")
        self.draw_flow()
        self.energy()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_flow(self):
        self.O = LEFT * 0.6 + DOWN * 0.1
        arrows = VGroup(*[
            Arrow(self.O + r * np.array([np.cos(a), np.sin(a), 0]), self.O + 0.55 * r * np.array([np.cos(a), np.sin(a), 0]),
                  buff=0, color=BLUE, stroke_width=3)
            for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)
            for r in [1.8]
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), run_time=1.5)
        note = self.ja_text("安定な流れ", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def energy(self):
        ell = Ellipse(width=3.6, height=2.2, color=ORANGE, stroke_width=4).move_to(self.O)
        cap = self.ja_text("エネルギー", font_size=24).move_to(self.note)
        self.play(Create(ell), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("減り続ける", font_size=24).move_to(self.note)
        self.play(ell.animate.scale(0.65), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"A^{\top}P+PA").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"A^{\top}P+PA=-Q").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A^{\top}P+PA=-Q").scale(1.0)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
