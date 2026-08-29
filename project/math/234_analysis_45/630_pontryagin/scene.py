from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Pontryagin(PacedScene):
    """#630 ポントリャーギン：最適制御の最大原理（約45秒）"""

    def construct(self):
        self.show_heading("ポントリャーギン")
        self.draw_ham()
        self.maximum()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ham(self):
        box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 0.8 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"H(x,u,p)", font_size=36).move_to(box)), run_time=1.3)
        note = self.ja_text("ハミルトン関数", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def maximum(self):
        arrow = Arrow(DOWN * 1.3 + LEFT * 0.8, UP * 0.05 + LEFT * 0.8, buff=0.05, color=ORANGE, stroke_width=4)
        cap = self.ja_text("u で最大化", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("随伴方程式", font_size=24).move_to(self.note)
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
        eq = MathTex(r"u^*(t)\in\arg\max_u H(x,u,p)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"u^*(t)\in\arg\max_u H(x,u,p)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"u^*(t)\in\arg\max_u H(x,u,p)").scale(0.75)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
