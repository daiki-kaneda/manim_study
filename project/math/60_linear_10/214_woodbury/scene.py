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
        self.derive()
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

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"(A+uv^{\mathsf T})^{-1}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"(A+uv^{\mathsf T})^{-1}=A^{-1}-\frac{A^{-1}uv^{\mathsf T}A^{-1}}{1+v^{\mathsf T}A^{-1}u}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(
            r"(A+uv^{\mathsf T})^{-1}=A^{-1}-\frac{A^{-1}uv^{\mathsf T}A^{-1}}{1+v^{\mathsf T}A^{-1}u}"
        ).scale(0.52)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.2)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
