from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SylvesterEquation(PacedScene):
    """#322 シルベスター方程式：AX−XB=C（約45秒）"""

    def construct(self):
        self.show_heading("シルベスター方程式")
        self.draw_eq()
        self.condition()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_eq(self):
        eq = MathTex(r"AX-XB=C", font_size=52).shift(UP * 0.9)
        self.play(Write(eq), run_time=1.4)
        note = self.ja_text("未知は X", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def condition(self):
        spec = MathTex(r"\sigma(A)\cap\sigma(B)=\emptyset", font_size=40, color=ORANGE).shift(DOWN * 0.2)
        cap = self.ja_text("固有値が離れる", font_size=24).move_to(self.note)
        self.play(Write(spec), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("一意に解ける", font_size=24).move_to(self.note)
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
        eq = MathTex(r"AX-XB").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"AX-XB=C").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"AX-XB=C").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
