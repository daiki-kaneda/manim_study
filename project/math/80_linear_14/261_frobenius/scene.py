from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FrobeniusNorm(PacedScene):
    """#261 フロベニウスは成分の二乗和（約45秒）"""

    def construct(self):
        self.show_heading("フロベニウスノルム")
        self.draw_matrix()
        self.sum_squares()
        self.show_formula()
        self.read(1.4)

    def draw_matrix(self):
        self.mat = Matrix([["1", "2"], ["0", "2"]], h_buff=0.9, v_buff=0.75).scale(1.0)
        self.mat.shift(LEFT * 2.2 + UP * 0.2)
        self.play(FadeIn(self.mat), run_time=1.2)
        note = self.ja_text("成分", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sum_squares(self):
        terms = MathTex(r"1^{2}+2^{2}+0^{2}+2^{2}", color=ORANGE).scale(0.9)
        terms.shift(RIGHT * 1.8 + UP * 0.6)
        cap = self.ja_text("二乗して足す", font_size=24).move_to(self.note)
        self.play(Write(terms), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        result = MathTex(r"\sqrt{9}=3", color=YELLOW).scale(1.1).next_to(terms, DOWN, buff=0.35)
        cap2 = self.ja_text("ノルム", font_size=24).move_to(self.note)
        self.play(Write(result), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\|A\|_F=\sqrt{\sum_{ij}a_{ij}^{2}}").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
