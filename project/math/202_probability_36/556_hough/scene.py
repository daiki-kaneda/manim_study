from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class HoughTransform(PacedScene):
    """#556 ハフ変換：直線をパラメータ空間の点に（約45秒）"""

    def construct(self):
        self.show_heading("ハフ変換")
        self.draw_lines()
        self.param()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_lines(self):
        lines = VGroup(
            Line(LEFT * 3 + DOWN * 1.2, RIGHT * 1.5 + UP * 1.5, color=BLUE, stroke_width=3),
            Line(LEFT * 2.5 + UP * 1.4, RIGHT * 2.5 + DOWN * 0.8, color=TEAL, stroke_width=3),
        )
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in [LEFT * 1.5 + UP * 0.2, ORIGIN, RIGHT * 0.8 + DOWN * 0.3]])
        self.play(Create(lines), FadeIn(dots), run_time=1.3)
        note = self.ja_text("画像上の点", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def param(self):
        box = RoundedRectangle(width=2.8, height=2.0, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.5 + DOWN * 0.1)
        lab = MathTex(r"(\rho,\theta)", font_size=32).move_to(box)
        cap = self.ja_text("パラメータ空間", font_size=24).move_to(self.note)
        self.play(Create(box), FadeIn(lab), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("投票で直線検出", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\rho").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\rho=x\cos\theta+y\sin\theta").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\rho=x\cos\theta+y\sin\theta").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
