from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class QRFactorization(PacedScene):
    """#178 QR は直交と三角（約45秒）"""

    def construct(self):
        self.origin = LEFT * 3.2 + DOWN * 1.55
        self.show_heading("QR 分解")
        self.draw_columns()
        self.orthogonalize()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_columns(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 6.4, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.9, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.a1 = np.array([3.6, 0.7])
        self.a2 = np.array([1.6, 2.7])
        self.v1 = Arrow(self.origin, self._pt(self.a1), buff=0, color=BLUE, stroke_width=5)
        self.v2 = Arrow(self.origin, self._pt(self.a2), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.v1), GrowArrow(self.v2), run_time=1.4)
        note = self.ja_text("列ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def orthogonalize(self):
        # Gram-Schmidt visual: q1 along a1, q2 perpendicular
        q1 = self.a1 / np.linalg.norm(self.a1) * 3.2
        proj = (np.dot(self.a2, self.a1) / np.dot(self.a1, self.a1)) * self.a1
        q2_dir = self.a2 - proj
        q2 = q2_dir / np.linalg.norm(q2_dir) * 2.4
        n1 = Arrow(self.origin, self._pt(q1), buff=0, color=BLUE, stroke_width=5)
        n2 = Arrow(self.origin, self._pt(q2), buff=0, color=GREEN, stroke_width=5)
        drop = DashedLine(self._pt(self.a2), self._pt(proj), color=ORANGE, stroke_width=3)
        cap = self.ja_text("直交化", font_size=24).move_to(self.note)
        self.play(Create(drop), run_time=0.9)
        self.play(Transform(self.v1, n1), Transform(self.v2, n2), Transform(self.note, cap), run_time=1.7)
        self.read(0.4)
        labs = VGroup(
            MathTex("Q", color=BLUE, font_size=32).next_to(self._pt(q1), DOWN, buff=0.1),
            MathTex("R", color=ORANGE, font_size=32).move_to(self.origin + RIGHT * 5.2 + UP * 2.8),
        )
        cap2 = self.ja_text("直交と三角", font_size=24).move_to(self.note)
        self.play(FadeIn(labs), Transform(self.note, cap2), run_time=1.0)
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
        eq2 = MathTex(r"A=QR").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A=QR").scale(1.2)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.5)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
