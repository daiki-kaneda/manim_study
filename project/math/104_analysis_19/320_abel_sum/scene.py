from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AbelSummation(PacedScene):
    """#320 アーベル総和：部分和で積分（和）を書き換える（約45秒）"""

    def construct(self):
        self.show_heading("アーベル総和法")
        self.draw_parts()
        self.rewrite()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_parts(self):
        a = MathTex(r"a_k", font_size=40).shift(LEFT * 2.5 + UP * 0.8)
        b = MathTex(r"b_k", font_size=40).shift(LEFT * 0.8 + UP * 0.8)
        self.play(FadeIn(a), FadeIn(b), run_time=1.1)
        note = self.ja_text("2 つの列", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def rewrite(self):
        A = MathTex(r"A_n=\sum_{k=1}^{n}a_k", font_size=36, color=ORANGE).shift(DOWN * 0.2)
        cap = self.ja_text("部分和", font_size=24).move_to(self.note)
        self.play(Write(A), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        arrow = Arrow(DOWN * 0.7, DOWN * 1.2, buff=0.05, color=YELLOW)
        cap2 = self.ja_text("和を書き換える", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"\sum_{k").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sum_{k=1}^{n}a_kb_k=A_nb_n-\sum_{k=1}^{n-1}A_k(b_{k+1}-b_k)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sum_{k=1}^{n}a_kb_k=A_nb_n-\sum_{k=1}^{n-1}A_k(b_{k+1}-b_k)").scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.1)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
