from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class StrongConvergence(PacedScene):
    """#534 強収束：ノルムで近づく（約45秒）"""

    def construct(self):
        self.show_heading("強収束")
        self.draw_balls()
        self.norm()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_balls(self):
        target = Dot(RIGHT * 1.5, color=YELLOW, radius=0.12)
        dots = VGroup(*[Dot(LEFT * 2.5 + RIGHT * i * 0.7, color=BLUE, radius=0.1) for i in range(5)])
        arrows = VGroup(*[Arrow(dots[i].get_center(), target.get_center(), buff=0.15, color=GREY, stroke_width=2) for i in range(5)])
        self.play(FadeIn(dots), FadeIn(target), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), run_time=1.5)
        note = self.ja_text("ノルム収束", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def norm(self):
        cap = self.ja_text("距離が0へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("弱収束より強い", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x_n\to x\ \Leftrightarrow\ \|x_n-x\|\to0").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_n\to x\ \Leftrightarrow\ \|x_n-x\|\to0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_n\to x\ \Leftrightarrow\ \|x_n-x\|\to0").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
