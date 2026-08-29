from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LUDecomposition(PacedScene):
    """#165 LU 分解は下三角と上三角（約45秒）"""

    def construct(self):
        self.show_heading("LU 分解")
        self.show_matrix()
        self.factor()
        self.show_formula()
        self.read(1.4)

    def _mat(self, entries, color=WHITE):
        rows = []
        for row in entries:
            rows.append(MathTex(*[f"{v}" for v in row], font_size=34))
        g = VGroup(*rows).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        box = SurroundingRectangle(g, color=color, buff=0.18, stroke_width=2)
        return VGroup(g, box)

    def show_matrix(self):
        self.A = MathTex(
            r"A=\begin{bmatrix}2&1\\4&3\end{bmatrix}",
            font_size=40,
        ).shift(UP * 1.15)
        self.play(Write(self.A), run_time=1.6)
        note = self.ja_text("正方行列", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def factor(self):
        L = MathTex(r"L=\begin{bmatrix}1&0\\2&1\end{bmatrix}", font_size=36, color=BLUE)
        U = MathTex(r"U=\begin{bmatrix}2&1\\0&1\end{bmatrix}", font_size=36, color=YELLOW)
        pair = VGroup(L, U).arrange(RIGHT, buff=0.7).shift(DOWN * 0.15)
        cap = self.ja_text("下と上", font_size=24).move_to(self.note)
        self.play(FadeIn(L, shift=LEFT * 0.2), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        self.play(FadeIn(U, shift=RIGHT * 0.2), run_time=1.1)
        self.read(0.35)
        # highlight zeros/ones pattern
        brace_l = Brace(L, DOWN, color=BLUE)
        brace_u = Brace(U, DOWN, color=YELLOW)
        lab_l = self.ja_text("下三角", font_size=22, color=BLUE).next_to(brace_l, DOWN, buff=0.08)
        lab_u = self.ja_text("上三角", font_size=22, color=YELLOW).next_to(brace_u, DOWN, buff=0.08)
        self.play(GrowFromCenter(brace_l), GrowFromCenter(brace_u), FadeIn(lab_l), FadeIn(lab_u), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"A=LU").scale(1.2)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.5)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
