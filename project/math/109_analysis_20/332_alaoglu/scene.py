from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Alaoglu(PacedScene):
    """#332 アラオグル：弱*コンパクト（約45秒）"""

    def construct(self):
        self.show_heading("アラオグルの定理")
        self.draw_ball()
        self.weakstar()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ball(self):
        self.ball = Circle(radius=2.0, color=BLUE, fill_opacity=0.25, stroke_width=3).shift(LEFT * 0.5 + DOWN * 0.1)
        self.play(FadeIn(self.ball), run_time=1.2)
        note = self.ja_text("単位球", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def weakstar(self):
        pts = VGroup(*[
            Dot(self.ball.get_center() + RIGHT * dx + UP * dy, color=ORANGE, radius=0.08)
            for dx, dy in [(0.6, 0.4), (-0.7, 0.5), (0.2, -0.8), (-0.4, -0.3), (1.1, -0.2)]
        ])
        cap = self.ja_text("点列", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.1), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        # converging subnet hint
        lim = Dot(self.ball.get_center() + RIGHT * 0.3 + UP * 0.1, color=YELLOW, radius=0.12)
        cap2 = self.ja_text("収束部分", font_size=24).move_to(self.note)
        self.play(FadeIn(lim, scale=0.5), Transform(self.note, cap2), run_time=1.2)
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
        formula = self.ja_text("弱*コンパクト", font_size=30)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
