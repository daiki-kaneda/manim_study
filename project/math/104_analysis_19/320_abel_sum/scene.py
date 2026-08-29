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

    def show_formula(self):
        formula = MathTex(r"\sum_{k=1}^{n}a_kb_k=A_nb_n-\sum_{k=1}^{n-1}A_k(b_{k+1}-b_k)").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
