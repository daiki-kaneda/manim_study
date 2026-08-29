from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class IsometricDeformation(PacedScene):
    """#517 等長変形：距離を保ったまま形を変える（約45秒）"""

    def construct(self):
        self.show_heading("等長変形")
        self.draw_surface()
        self.bend()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_surface(self):
        grid = VGroup(*[
            Line(LEFT * 2.5 + UP * (1.0 - i * 0.5), RIGHT * 2.5 + UP * (1.0 - i * 0.5), color=BLUE, stroke_width=2)
            for i in range(5)
        ] + [
            Line(LEFT * (2.5 - j * 1.0) + UP * 1.0, LEFT * (2.5 - j * 1.0) + DOWN * 1.0, color=BLUE, stroke_width=2)
            for j in range(6)
        ])
        self.play(LaggedStart(*[Create(l) for l in grid], lag_ratio=0.02), run_time=1.4)
        note = self.ja_text("曲面パッチ", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bend(self):
        arc = Arc(radius=2.8, start_angle=-0.6, angle=1.2, color=ORANGE, stroke_width=4).shift(DOWN * 0.2)
        cap = self.ja_text("曲げても距離同じ", font_size=24).move_to(self.note)
        self.play(Create(arc), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("ガウス曲率が不変", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\|f(p)-f(q)\|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|f(p)-f(q)\|=\|p-q\|\quad(\text{local})").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|f(p)-f(q)\|=\|p-q\|\quad(\text{local})").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
