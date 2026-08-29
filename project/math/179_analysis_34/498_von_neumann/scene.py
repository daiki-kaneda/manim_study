from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class VonNeumannAlgebra(PacedScene):
    """#498 フォンノイマン代数：弱閉な*代数（約45秒）"""

    def construct(self):
        self.show_heading("フォンノイマン代数")
        self.draw_ops()
        self.weak_closure()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.4, height=1.0, corner_radius=0.08, color=BLUE, stroke_width=2)
            .shift(LEFT * 2.5 + RIGHT * i * 1.6 + UP * 0.5)
            for i in range(3)
        ])
        labs = VGroup(*[MathTex(s, font_size=28).move_to(boxes[i]) for i, s in enumerate(["A", "A^*", "AB"])])
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.12), FadeIn(labs), run_time=1.4)
        note = self.ja_text("*代数", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def weak_closure(self):
        shell = RoundedRectangle(width=5.5, height=2.2, corner_radius=0.15, color=ORANGE, stroke_width=3).shift(UP * 0.3)
        cap = self.ja_text("弱作用素で閉", font_size=24).move_to(self.note)
        self.play(Create(shell), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("二重交換子", font_size=24).move_to(self.note)
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
        eq = MathTex(r"M").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"M=M''\subset B(H)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"M=M''\subset B(H)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
