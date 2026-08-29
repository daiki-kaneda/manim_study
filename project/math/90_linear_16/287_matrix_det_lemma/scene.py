from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MatrixDetLemma(PacedScene):
    """#287 行列式補題：ランク1更新の行列式（約45秒）"""

    def construct(self):
        self.show_heading("行列式補題")
        self.draw_update()
        self.factor()
        self.show_formula()
        self.read(1.4)

    def draw_update(self):
        a = MathTex(r"A", font_size=52).shift(LEFT * 2.4 + UP * 0.5)
        plus = MathTex(r"+", font_size=42).next_to(a, RIGHT, buff=0.25)
        uv = MathTex(r"uv^{\top}", font_size=48, color=ORANGE).next_to(plus, RIGHT, buff=0.25)
        self.play(FadeIn(a), FadeIn(plus), FadeIn(uv), run_time=1.4)
        note = self.ja_text("ランク1更新", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.expr = VGroup(a, plus, uv)

    def factor(self):
        arrow = Arrow(UP * -0.1, DOWN * 0.7, buff=0.05, color=YELLOW)
        det = MathTex(r"\det(A+uv^{\top})", font_size=40).shift(DOWN * 0.55)
        cap = self.ja_text("行列式は", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Write(det), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        fact = MathTex(r"=\det(A)\,(1+v^{\top}A^{-1}u)", font_size=36, color=YELLOW).next_to(det, DOWN, buff=0.3)
        cap2 = self.ja_text("スカラーに帰着", font_size=24).move_to(self.note)
        self.play(Write(fact), Transform(self.note, cap2), run_time=1.4)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\det(A+uv^{\top})=\det(A)(1+v^{\top}A^{-1}u)").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
