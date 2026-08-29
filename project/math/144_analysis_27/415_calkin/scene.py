from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class CalkinAlgebra(PacedScene):
    """#415 カルキン代数：作用素をコンパクトで割る（約45秒）"""

    def construct(self):
        self.show_heading("カルキン代数")
        self.draw_ops()
        self.quotient()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        big = RoundedRectangle(width=3.2, height=2.2, corner_radius=0.15, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.2)
        lab = MathTex(r"\mathcal{B}(H)", font_size=34).move_to(big)
        self.play(Create(big), FadeIn(lab), run_time=1.2)
        note = self.ja_text("有界作用素", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.big = big

    def quotient(self):
        arrow = Arrow(LEFT * 0.6, RIGHT * 0.4, buff=0.05, color=YELLOW, stroke_width=4)
        q = RoundedRectangle(width=2.6, height=1.8, corner_radius=0.15, color=ORANGE, stroke_width=3).shift(RIGHT * 2.4 + UP * 0.2)
        qlab = MathTex(r"\mathcal{B}/\mathcal{K}", font_size=32).move_to(q)
        cap = self.ja_text("コンパクトを無視", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Create(q), FadeIn(qlab), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("商代数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathcal{Q}=\mathcal{B}(H)/\mathcal{K}(H)").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
