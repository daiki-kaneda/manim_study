from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SchurComplement(PacedScene):
    """#309 シューア補元：ブロック消去の残り（約45秒）"""

    def construct(self):
        self.show_heading("シューア補元")
        self.draw_block()
        self.eliminate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_block(self):
        mat = MathTex(r"\begin{pmatrix}A&B\\C&D\end{pmatrix}", font_size=52).shift(LEFT * 1.8 + UP * 0.3)
        self.play(FadeIn(mat), run_time=1.3)
        note = self.ja_text("ブロック行列", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def eliminate(self):
        arrow = Arrow(LEFT * 0.1, RIGHT * 1.0, buff=0.05, color=YELLOW)
        s = MathTex(r"S=D-CA^{-1}B", color=ORANGE, font_size=40).shift(RIGHT * 2.3 + UP * 0.3)
        cap = self.ja_text("消去の残り", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.1)
        self.play(Write(s), run_time=1.2)
        self.read(0.3)
        cap2 = self.ja_text("S と呼ぶ", font_size=24).move_to(self.note)
        self.play(Indicate(s, color=YELLOW), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"S").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S=D-CA^{-1}B").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S=D-CA^{-1}B").scale(1.05)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
