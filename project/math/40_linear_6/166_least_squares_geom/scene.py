from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class NormalEquations(PacedScene):
    """#166 正規方程式は射影で一番近い（約45秒）"""

    def construct(self):
        self.origin = LEFT * 3.1 + DOWN * 1.55
        self.show_heading("正規方程式")
        self.draw_plane()
        self.project()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_plane(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 6.4, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.9, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        # column space as a line (1D plane in 2D)
        self.col = Line(self.origin + LEFT * 0.2 + DOWN * 0.1, self.origin + RIGHT * 5.6 + UP * 2.5, color=BLUE, stroke_width=5)
        self.play(Create(self.col), run_time=1.2)
        note = self.ja_text("列空間", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def project(self):
        b = self._pt((2.4, 3.15))
        p = self._pt((3.4, 1.55))
        ab = Arrow(self.origin, b, buff=0, color=YELLOW, stroke_width=5)
        ap = Arrow(self.origin, p, buff=0, color=GREEN, stroke_width=5)
        drop = DashedLine(b, p, color=ORANGE, stroke_width=3)
        self.play(GrowArrow(ab), run_time=1.0)
        blab = MathTex(r"b", color=YELLOW, font_size=32).next_to(b, UP, buff=0.08)
        self.play(FadeIn(blab), run_time=0.35)
        self.read(0.3)
        cap = self.ja_text("最短", font_size=24).move_to(self.note)
        self.play(GrowArrow(ap), Create(drop), Transform(self.note, cap), run_time=1.5)
        plab = MathTex(r"A\hat x", color=GREEN, font_size=30).next_to(p, RIGHT, buff=0.08)
        self.play(FadeIn(plab), run_time=0.5)
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
        eq = MathTex(r"A^{\mathsf T}A\hat x").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"A^{\mathsf T}A\hat x=A^{\mathsf T}b").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A^{\mathsf T}A\hat x=A^{\mathsf T}b").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
