from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CayleyTransform(PacedScene):
    """#323 ケイリー変換：ユニタリ ↔ エルミート（約45秒）"""

    def construct(self):
        self.show_heading("ケイリー変換")
        self.draw_maps()
        self.correspond()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_maps(self):
        left = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.6 + UP * 0.3)
        right = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.6 + UP * 0.3)
        l = self.ja_text("エルミート", font_size=28).move_to(left)
        r = self.ja_text("ユニタリ", font_size=28).move_to(right)
        self.play(FadeIn(left), FadeIn(l), FadeIn(right), FadeIn(r), run_time=1.4)
        note = self.ja_text("対応", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.left, self.right = left, right

    def correspond(self):
        a1 = Arrow(self.left.get_right(), self.right.get_left(), buff=0.15, color=ORANGE, stroke_width=4)
        a2 = Arrow(self.right.get_left() + DOWN * 0.25, self.left.get_right() + DOWN * 0.25, buff=0.15, color=YELLOW, stroke_width=4)
        cap = self.ja_text("行き来できる", font_size=24).move_to(self.note)
        self.play(GrowArrow(a1), Transform(self.note, cap), run_time=1.2)
        self.play(GrowArrow(a2), run_time=0.9)
        self.read(0.3)
        cap2 = self.ja_text("分数線形", font_size=24).move_to(self.note)
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
        eq = MathTex(r"U").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"U=(I-iH)(I+iH)^{-1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"U=(I-iH)(I+iH)^{-1}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
