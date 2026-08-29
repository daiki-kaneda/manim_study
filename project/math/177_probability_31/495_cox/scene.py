from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



import numpy as np


class CoxModel(PacedScene):
    """#495 コックスモデル：部分尤度で β を推定（約45秒）"""

    def construct(self):
        self.show_heading("コックスモデル")
        self.draw_risk()
        self.partial()
        self.show_formula()
        self.read(1.4)

    def draw_risk(self):
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 1.2, 1],
            x_length=6.2, y_length=2.5, tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.45)
        s0 = axes.plot(lambda t: np.exp(-0.25 * t), x_range=[0, 5], color=BLUE, stroke_width=4)
        s1 = axes.plot(lambda t: np.exp(-0.55 * t), x_range=[0, 5], color=ORANGE, stroke_width=4)
        self.play(Create(axes), Create(s0), Create(s1), run_time=1.4)
        note = self.ja_text("生存曲線が分岐", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def partial(self):
        cap = self.ja_text("部分尤度", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("基準ハザード不要", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"L(\beta)=\prod_i\frac{e^{\beta^\top x_i}}{\sum_{j\in R(t_i)}e^{\beta^\top x_j}}").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
