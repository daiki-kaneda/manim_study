from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CompanionMatrix(PacedScene):
    """#310 コンパニオン行列：多項式の固有値が根（約45秒）"""

    def construct(self):
        self.show_heading("コンパニオン行列")
        self.draw_poly()
        self.matrix()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_poly(self):
        poly = MathTex(r"p(t)=t^{n}+a_{n-1}t^{n-1}+\cdots+a_0", font_size=36).shift(UP * 1.3)
        self.play(Write(poly), run_time=1.5)
        note = self.ja_text("モニック多項式", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def matrix(self):
        C = Matrix(
            [["0", "0", "-a_0"],
             ["1", "0", "-a_1"],
             ["0", "1", "-a_2"]],
            h_buff=1.1,
            v_buff=0.7,
        ).scale(0.85).shift(DOWN * 0.15)
        cap = self.ja_text("コンパニオン", font_size=24).move_to(self.note)
        self.play(FadeIn(C), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("固有値＝根", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"\det(tI-C)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\det(tI-C)=p(t)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\det(tI-C)=p(t)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
