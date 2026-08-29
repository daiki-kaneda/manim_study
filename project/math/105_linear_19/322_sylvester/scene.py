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

    def show_formula(self):
        formula = MathTex(r"AX-XB=C").scale(1.15)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
