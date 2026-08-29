from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class WeylInequality(PacedScene):
    """#297 ワイル：固有値の摂動はノルムで押さえる（約45秒）"""

    def construct(self):
        self.show_heading("ワイルの不等式")
        self.draw_eigs()
        self.perturb()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_eigs(self):
        self.O = LEFT * 0.5 + DOWN * 0.1
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 3.0, color=GREY, stroke_width=2)
        self.play(Create(ax), run_time=0.7)
        self.eigs = VGroup(*[
            Dot(self.O + RIGHT * x, color=BLUE, radius=0.1)
            for x in [-1.6, -0.3, 1.2, 2.1]
        ])
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in self.eigs], lag_ratio=0.1), run_time=1.2)
        note = self.ja_text("固有値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def perturb(self):
        shifts = [0.25, -0.2, 0.15, -0.3]
        news = VGroup(*[
            Dot(d.get_center() + RIGHT * s, color=ORANGE, radius=0.1)
            for d, s in zip(self.eigs, shifts)
        ])
        arrows = VGroup(*[
            Arrow(d.get_center(), n.get_center(), buff=0.08, color=YELLOW, stroke_width=3)
            for d, n in zip(self.eigs, news)
        ])
        cap = self.ja_text("摂動", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), Transform(self.note, cap), run_time=1.3)
        self.play(FadeIn(news), run_time=0.8)
        self.read(0.25)
        brace = BraceBetweenPoints(self.eigs[0].get_center(), news[0].get_center(), direction=UP, color=TEAL)
        cap2 = self.ja_text("差 ≤ ノルム", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"|\lambda_i(A+E)-\lambda_i(A)|\le\|E\|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|\lambda_i(A+E)-\lambda_i(A)|\le\|E\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|\lambda_i(A+E)-\lambda_i(A)|\le\|E\|").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
