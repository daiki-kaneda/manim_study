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

    def show_formula(self):
        formula = MathTex(r"x_n\to x\ \Leftrightarrow\ \|x_n-x\|\to0").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
