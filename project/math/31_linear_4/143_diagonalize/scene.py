from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Diagonalize(PacedScene):
    """#143 対角化は固有方向に伸ばす（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 0.2
        self.show_heading("対角化")
        self.draw_basis()
        self.stretch()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_basis(self):
        ax = Line(self.origin + LEFT * 2.4, self.origin + RIGHT * 3.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.1, self.origin + UP * 2.3, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.85)
        self.e1 = np.array([1.35, 0.55])
        self.e2 = np.array([-0.55, 1.25])
        self.a1 = Arrow(self.origin, self._pt(self.e1), buff=0, color=BLUE, stroke_width=5)
        self.a2 = Arrow(self.origin, self._pt(self.e2), buff=0, color=GREEN, stroke_width=5)
        l1 = MathTex(r"p_1", color=BLUE, font_size=30).next_to(self.a1.get_end(), DR, buff=0.08)
        l2 = MathTex(r"p_2", color=GREEN, font_size=30).next_to(self.a2.get_end(), UL, buff=0.08)
        self.play(GrowArrow(self.a1), GrowArrow(self.a2), FadeIn(l1), FadeIn(l2), run_time=1.5)
        para = Polygon(
            self.origin,
            self._pt(self.e1),
            self._pt(self.e1 + self.e2),
            self._pt(self.e2),
            color=WHITE,
            stroke_width=2,
            fill_opacity=0.12,
        )
        self.play(FadeIn(para), run_time=0.9)
        note = self.ja_text("固有の向き", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note
        self.para = para
        self.l1 = l1
        self.l2 = l2

    def stretch(self):
        s1, s2 = 1.85, 0.55
        n1 = self.e1 * s1
        n2 = self.e2 * s2
        na1 = Arrow(self.origin, self._pt(n1), buff=0, color=BLUE, stroke_width=5)
        na2 = Arrow(self.origin, self._pt(n2), buff=0, color=GREEN, stroke_width=5)
        npara = Polygon(
            self.origin,
            self._pt(n1),
            self._pt(n1 + n2),
            self._pt(n2),
            color=YELLOW,
            stroke_width=2,
            fill_opacity=0.18,
        )
        cap = self.ja_text("別々に伸縮", font_size=24).move_to(self.note)
        self.play(
            Transform(self.a1, na1),
            Transform(self.a2, na2),
            Transform(self.para, npara),
            self.l1.animate.next_to(self._pt(n1), DR, buff=0.08),
            self.l2.animate.next_to(self._pt(n2), UL, buff=0.08),
            Transform(self.note, cap),
            run_time=2.2,
        )
        self.read(0.45)
        lam = VGroup(
            MathTex(r"\lambda_1", color=BLUE, font_size=32).next_to(self._pt(n1), DOWN, buff=0.12),
            MathTex(r"\lambda_2", color=GREEN, font_size=32).next_to(self._pt(n2), LEFT, buff=0.12),
        )
        self.play(FadeIn(lam), run_time=0.7)
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
        eq2 = MathTex(r"A=PDP^{-1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A=PDP^{-1}").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
