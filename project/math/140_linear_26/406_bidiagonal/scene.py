from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class Bidiagonalization(PacedScene):
    """#406 二対角化：SVD 前処理で帯行列へ（約45秒）"""

    def construct(self):
        self.show_heading("二対角化")
        self.draw_dense()
        self.bidiag()
        self.show_formula()
        self.read(1.4)

    def draw_dense(self):
        A = Matrix(
            [["*", "*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*"], ["*", "*", "*", "*"]],
            h_buff=0.55, v_buff=0.45,
        ).scale(0.65).shift(LEFT * 2.8 + UP * 0.2)
        self.play(FadeIn(A), run_time=1.2)
        note = self.ja_text("密な行列", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bidiag(self):
        arrow = Arrow(LEFT * 0.6, RIGHT * 0.2, buff=0.05, color=YELLOW, stroke_width=4)
        B = Matrix(
            [["*", "*", "0", "0"], ["0", "*", "*", "0"], ["0", "0", "*", "*"], ["0", "0", "0", "*"]],
            h_buff=0.55, v_buff=0.45,
        ).scale(0.65).shift(RIGHT * 2.4 + UP * 0.2)
        cap = self.ja_text("帯だけ残す", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), FadeIn(B), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("上下二対角", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A=UBV^{\!*}\quad (B\ \text{bidiag})").scale(0.85)
        formula = MathTex(r"A=UBV^{*},\ B\ \mathrm{bidiagonal}").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
