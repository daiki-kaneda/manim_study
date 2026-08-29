from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CompactOperator(PacedScene):
    """#378 コンパクト作用素：像が相対コンパクト（約45秒）"""

    def construct(self):
        self.show_heading("コンパクト作用素")
        self.draw_ball()
        self.image()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ball(self):
        self.ball = Circle(radius=1.6, color=BLUE, fill_opacity=0.25, stroke_width=3).shift(LEFT * 2.4 + UP * 0.1)
        self.play(FadeIn(self.ball), run_time=1.1)
        note = self.ja_text("有界集合", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def image(self):
        arrow = Arrow(LEFT * 0.5, RIGHT * 0.5, buff=0.05, color=YELLOW, stroke_width=4)
        img = Ellipse(width=2.4, height=1.5, color=ORANGE, fill_opacity=0.3, stroke_width=3).shift(RIGHT * 2.4 + UP * 0.1)
        pts = VGroup(*[
            Dot(img.get_center() + RIGHT * dx + UP * dy, color=YELLOW, radius=0.06)
            for dx, dy in [(0.4, 0.2), (-0.5, 0.3), (0.1, -0.4), (-0.2, 0.0), (0.5, -0.2)]
        ])
        cap = self.ja_text("像", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), FadeIn(img), Transform(self.note, cap), run_time=1.3)
        self.play(FadeIn(pts), run_time=0.8)
        self.read(0.25)
        cap2 = self.ja_text("相対コンパクト", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("像が相対コンパクト", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
