from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ShermanMorrison(PacedScene):
    """#214 シャーマン・モリソンは逆の補正（約45秒）"""

    def construct(self):
        self.show_heading("シャーマン・モリソン")
        self.show_inverse()
        self.correct()
        self.show_formula()
        self.read(1.4)

    def show_inverse(self):
        a = MathTex(r"A^{-1}").scale(1.4)
        a.shift(LEFT * 2.2 + UP * 0.3)
        self.play(Write(a), run_time=1.2)
        note = self.ja_text("逆が既知", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.a = a

    def correct(self):
        plus = MathTex(r"+").scale(1.2).next_to(self.a, RIGHT, buff=0.35)
        corr = MathTex(r"-\frac{A^{-1}uv^{\mathsf T}A^{-1}}{1+v^{\mathsf T}A^{-1}u}").scale(0.7)
        corr.next_to(plus, RIGHT, buff=0.3)
        box = SurroundingRectangle(corr, color=ORANGE, buff=0.15, corner_radius=0.08)
        cap = self.ja_text("補正項", font_size=24).move_to(self.note)
        self.play(FadeIn(plus), Write(corr), Transform(self.note, cap), run_time=1.8)
        self.play(Create(box), run_time=0.8)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(
            r"(A+uv^{\mathsf T})^{-1}=A^{-1}-\frac{A^{-1}uv^{\mathsf T}A^{-1}}{1+v^{\mathsf T}A^{-1}u}"
        ).scale(0.52)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=2.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
