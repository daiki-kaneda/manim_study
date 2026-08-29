from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Arnoldi(PacedScene):
    """#393 アーノルディ：Krylov 基底の直交化（約45秒）"""

    def construct(self):
        self.show_heading("アーノルディ法")
        self.draw_krylov()
        self.hessenberg()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_krylov(self):
        v0 = Arrow(ORIGIN, UP * 1.6, buff=0, color=BLUE, stroke_width=4).shift(LEFT * 2.5 + DOWN * 0.2)
        v1 = Arrow(ORIGIN, RIGHT * 1.5 + UP * 0.9, buff=0, color=TEAL, stroke_width=4).shift(LEFT * 2.5 + DOWN * 0.2)
        v2 = Arrow(ORIGIN, RIGHT * 1.8 + DOWN * 0.4, buff=0, color=ORANGE, stroke_width=4).shift(LEFT * 2.5 + DOWN * 0.2)
        self.play(GrowArrow(v0), run_time=0.7)
        self.play(GrowArrow(v1), GrowArrow(v2), run_time=1.0)
        note = self.ja_text("Krylov 空間", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def hessenberg(self):
        H = Matrix(
            [["*", "*", "0"], ["*", "*", "*"], ["0", "*", "*"]],
            h_buff=0.7, v_buff=0.55,
        ).scale(0.75).shift(RIGHT * 2.2 + UP * 0.3)
        cap = self.ja_text("直交化", font_size=24).move_to(self.note)
        self.play(FadeIn(H), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("Hessenberg", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(H, color=YELLOW), run_time=1.1)
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
        eq = MathTex(r"AQ_k").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"AQ_k=Q_{k+1}\tilde H_k").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"AQ_k=Q_{k+1}\tilde H_k").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
