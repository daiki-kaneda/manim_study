from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Lanczos(PacedScene):
    """#394 ランチョス：対称行列の三重対角還元（約45秒）"""

    def construct(self):
        self.show_heading("ランチョス法")
        self.draw_symmetric()
        self.tridiag()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_symmetric(self):
        A = Matrix(
            [["2", "1", "0"], ["1", "2", "1"], ["0", "1", "2"]],
            h_buff=0.7, v_buff=0.55,
        ).scale(0.75).shift(LEFT * 2.8 + UP * 0.3)
        self.play(FadeIn(A), run_time=1.2)
        note = self.ja_text("対称行列", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def tridiag(self):
        arrow = Arrow(LEFT * 0.7, RIGHT * 0.3, buff=0.05, color=YELLOW, stroke_width=4)
        T = Matrix(
            [[r"\alpha_1", r"\beta_1", "0"], [r"\beta_1", r"\alpha_2", r"\beta_2"], ["0", r"\beta_2", r"\alpha_3"]],
            h_buff=0.85, v_buff=0.55,
        ).scale(0.7).shift(RIGHT * 2.4 + UP * 0.3)
        cap = self.ja_text("三重対角へ", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), FadeIn(T), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("3 項漸化", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\beta_j q_{j+1}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\beta_j q_{j+1}=Aq_j-\alpha_j q_j-\beta_{j-1}q_{j-1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\beta_j q_{j+1}=Aq_j-\alpha_j q_j-\beta_{j-1}q_{j-1}").scale(0.7)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
