from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LevenbergMarquardt(PacedScene):
    """#633 レーベンバーグ・マーカート：GNと勾配の間を減衰（約45秒）"""

    def construct(self):
        self.show_heading("レーベンバーグ")
        self.draw_blend()
        self.damping()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_blend(self):
        left = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.4 + UP * 0.25)
        right = RoundedRectangle(width=2.4, height=1.3, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.4 + UP * 0.25)
        mid = RoundedRectangle(width=2.0, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(UP * 0.25)
        self.play(Create(left), Create(right), Create(mid),
                  FadeIn(MathTex(r"J^\top J", font_size=28).move_to(left)),
                  FadeIn(MathTex(r"\lambda I", font_size=28).move_to(right)),
                  FadeIn(MathTex(r"LM", font_size=28).move_to(mid)),
                  run_time=1.5)
        note = self.ja_text("減衰付きGN", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def damping(self):
        cap = self.ja_text("λ で切替え", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("信頼領域に近い", font_size=24).move_to(self.note)
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
        eq = MathTex(r"(J^\top J+\lambda I)\delta").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"(J^\top J+\lambda I)\delta=-J^\top r").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"(J^\top J+\lambda I)\delta=-J^\top r").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
