from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class Gelfand(PacedScene):
    """#391 ゲルファント：可換 Banach 代数 → 関数への表現（約45秒）"""

    def construct(self):
        self.show_heading("ゲルファント表現")
        self.draw_algebra()
        self.characters()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_algebra(self):
        box = RoundedRectangle(width=2.8, height=2.0, corner_radius=0.15, color=BLUE, stroke_width=3).shift(LEFT * 2.6 + UP * 0.2)
        lab = MathTex(r"\mathcal{A}", font_size=40).move_to(box)
        self.play(Create(box), FadeIn(lab), run_time=1.2)
        note = self.ja_text("可換代数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.box = box

    def characters(self):
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.6, buff=0.05, color=YELLOW, stroke_width=4)
        # spectrum as dots on a curve
        curve = ParametricFunction(
            lambda t: np.array([1.6 + 1.1 * np.cos(t), 0.2 + 0.7 * np.sin(t), 0]),
            t_range=[0, TAU], color=ORANGE, stroke_width=3,
        )
        pts = VGroup(*[
            Dot(np.array([1.6 + 1.1 * np.cos(t), 0.2 + 0.7 * np.sin(t), 0]), color=TEAL, radius=0.07)
            for t in np.linspace(0.2, TAU, 7)[:-1]
        ])
        cap = self.ja_text("指標の空間", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Create(curve), Transform(self.note, cap), run_time=1.4)
        self.play(FadeIn(pts), run_time=0.8)
        self.read(0.25)
        cap2 = self.ja_text("関数へ写す", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\hat a(\varphi)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\hat a(\varphi)=\varphi(a)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\hat a(\varphi)=\varphi(a)").scale(1.05)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
