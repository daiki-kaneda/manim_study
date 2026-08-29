from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class T1Theorem(PacedScene):
    """#571 T1定理：特異積分の有界性判定（約45秒）"""

    def construct(self):
        self.show_heading("T1定理")
        self.draw_T()
        self.test()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_T(self):
        box = RoundedRectangle(width=2.6, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.3 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"T", font_size=40).move_to(box)), run_time=1.2)
        note = self.ja_text("カルデロン・ジグムント", font_size=24)
        note.to_edge(RIGHT, buff=0.3).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def test(self):
        ones = MathTex(r"T(1),\ T^*(1)", font_size=34).shift(RIGHT * 2.0 + UP * 0.2)
        cap = self.ja_text("1 の像を見る", font_size=24).move_to(self.note)
        self.play(FadeIn(ones), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("BMO 条件で十分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"T:L^2\to L^2\ \Leftrightarrow\ T(1),T^*(1)\in\mathrm{BMO}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"T:L^2\to L^2\ \Leftrightarrow\ T(1),T^*(1)\in\mathrm{BMO}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"T:L^2\to L^2\ \Leftrightarrow\ T(1),T^*(1)\in\mathrm{BMO}").scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
