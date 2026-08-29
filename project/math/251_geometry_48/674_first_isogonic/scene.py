from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FirstIsogonicCenter(PacedScene):
    """#674 第一等角中心：等角共役系の三角形中心（約45秒）"""

    def construct(self):
        self.show_heading("第一等角中心")
        self.draw()
        self.isog()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.7 + DOWN * 1.2, RIGHT * 2.7 + DOWN * 1.2, UP * 1.8, color=BLUE, stroke_width=3)
        # equilateral erected outward hints
        tips = VGroup(
            Dot(LEFT * 3.3 + UP * 0.5, color=ORANGE, radius=0.08),
            Dot(RIGHT * 3.3 + UP * 0.5, color=ORANGE, radius=0.08),
            Dot(DOWN * 2.2, color=ORANGE, radius=0.08),
        )
        X = Dot(ORIGIN + UP * 0.1, color=TEAL, radius=0.1)
        self.play(Create(tri), FadeIn(tips), FadeIn(X), run_time=1.4)
        note = self.ja_text("正三角形を立てる", font_size=22)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def isog(self):
        cap = self.ja_text("線が一点に", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("X(13)", font_size=24).move_to(self.note)
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
        eq = MathTex(r"X(13)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"X(13)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"X(13)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
