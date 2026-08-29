from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class RieszLemma(PacedScene):
    """#307 リースの補題：単位球のほぼ直交な点（約45秒）"""

    def construct(self):
        self.show_heading("リースの補題")
        self.draw_subspace()
        self.pick_point()
        self.show_formula()
        self.read(1.4)

    def draw_subspace(self):
        self.O = LEFT * 0.5 + DOWN * 0.2
        plane = Line(self.O + LEFT * 2.8, self.O + RIGHT * 2.8, color=GREY, stroke_width=4)
        self.play(Create(plane), run_time=1.0)
        note = self.ja_text("閉部分空間", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def pick_point(self):
        v = Arrow(self.O, self.O + RIGHT * 1.2 + UP * 1.8, buff=0, color=BLUE, stroke_width=5)
        # distance dashed to plane
        foot = self.O + RIGHT * 1.2
        dash = DashedLine(v.get_end(), foot, color=ORANGE, stroke_width=3)
        cap = self.ja_text("ほぼ直交", font_size=24).move_to(self.note)
        self.play(GrowArrow(v), Transform(self.note, cap), run_time=1.3)
        self.play(Create(dash), run_time=0.9)
        self.read(0.25)
        ball = Circle(radius=0.35, color=YELLOW, stroke_width=3).move_to(v.get_end())
        cap2 = self.ja_text("距離 ≥ θ", font_size=24).move_to(self.note)
        self.play(Create(ball), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\|x-y\|\ge\theta\ (y\in Y),\ \|x\|=1").scale(0.8)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
