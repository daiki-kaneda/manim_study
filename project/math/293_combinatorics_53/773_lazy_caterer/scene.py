from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LazyCaterer(PacedScene):
    """#773 怠惰な料理人：平面を最大分割する切断面数（約45秒）"""

    def construct(self):
        self.show_heading("怠惰な料理人")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        plane = Square(side_length=3.4, color=GREY, stroke_width=2).shift(UP * 0.1)
        cuts = VGroup(
            Line(LEFT * 1.7 + DOWN * 1.5, RIGHT * 1.7 + UP * 1.5, color=BLUE, stroke_width=3),
            Line(LEFT * 1.7 + UP * 1.2, RIGHT * 1.7 + DOWN * 1.0, color=ORANGE, stroke_width=3),
            Line(LEFT * 0.2 + DOWN * 1.7, RIGHT * 0.5 + UP * 1.7, color=TEAL, stroke_width=3),
        )
        self.play(Create(plane), LaggedStart(*[Create(c) for c in cuts], lag_ratio=0.15), run_time=1.5)
        note = self.ja_text("n 回切る", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("最大ピース数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("二次式", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.75)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"p(n)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"p(n)=\frac{n(n+1)}{2}+1").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"p(n)=\frac{n(n+1)}{2}+1").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
