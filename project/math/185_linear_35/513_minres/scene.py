from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MINRES(PacedScene):
    """#513 MINRES：対称系で残差を最小化（約45秒）"""

    def construct(self):
        self.show_heading("MINRES")
        self.draw_krylov()
        self.min_res()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_krylov(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.2, height=0.85, corner_radius=0.08, color=BLUE, stroke_width=2)
            .shift(LEFT * 2.8 + RIGHT * i * 1.4 + UP * 0.6)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"A^{{{k}}}r", font_size=24).move_to(boxes[i]) for i, k in enumerate(range(4))])
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("クリロフ空間", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def min_res(self):
        arrow = Arrow(UP * -0.2, DOWN * 1.3, buff=0.05, color=ORANGE, stroke_width=4).shift(LEFT * 0.5)
        cap = self.ja_text("残差ノルム最小", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("A=A* 向け", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x_k").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_k=\arg\min_{x\in x_0+\mathcal{K}_k}\|b-Ax\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_k=\arg\min_{x\in x_0+\mathcal{K}_k}\|b-Ax\|").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
