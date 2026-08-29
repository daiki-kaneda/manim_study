from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ConditionNumber(PacedScene):
    """#179 条件数はゆがみの大きさ（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.2 + DOWN * 0.1
        self.show_heading("条件数")
        self.draw_unit()
        self.stretch()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_unit(self):
        ax = Line(self.origin + LEFT * 2.4, self.origin + RIGHT * 3.5, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.1, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        self.circ = Circle(radius=1.15, color=BLUE, stroke_width=4).move_to(self.origin)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.play(Create(self.circ), run_time=1.3)
        note = self.ja_text("単位円", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def stretch(self):
        ell = Ellipse(width=3.8, height=0.9, color=YELLOW, stroke_width=5).move_to(self.origin)
        cap = self.ja_text("大きくゆがむ", font_size=24).move_to(self.note)
        self.play(Transform(self.circ, ell), Transform(self.note, cap), run_time=1.9)
        self.read(0.35)
        long_a = Arrow(self.origin, self.origin + RIGHT * 1.9, buff=0, color=ORANGE, stroke_width=4)
        short_a = Arrow(self.origin, self.origin + UP * 0.45, buff=0, color=GREEN, stroke_width=4)
        self.play(GrowArrow(long_a), GrowArrow(short_a), run_time=1.2)
        ratio = MathTex(r"\kappa", color=YELLOW, font_size=40).move_to(self.origin + RIGHT * 3.2 + UP * 1.2)
        cap2 = self.ja_text("長い/短い", font_size=24).move_to(self.note)
        self.play(FadeIn(ratio), Transform(self.note, cap2), run_time=0.9)
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
        eq = MathTex(r"\kappa(A)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\kappa(A)=\|A\|\|A^{-1}\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\kappa(A)=\|A\|\|A^{-1}\|").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
