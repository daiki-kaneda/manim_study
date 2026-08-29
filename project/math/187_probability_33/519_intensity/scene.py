from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



import numpy as np


class IntensityFunction(PacedScene):
    """#519 強度関数：点過程の瞬間発生率（約45秒）"""

    def construct(self):
        self.show_heading("強度関数")
        self.draw_lambda()
        self.points()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_lambda(self):
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 2.2, 1],
            x_length=6.5, y_length=2.5, tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.45)
        lam = axes.plot(lambda t: 0.6 + 0.5 * np.sin(1.3 * t) + 0.3 * t / 5, x_range=[0, 5], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(lam), run_time=1.4)
        note = self.ja_text("時間で変化", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def points(self):
        xs = [0.6, 1.4, 2.1, 2.8, 3.7, 4.4]
        dots = VGroup(*[Dot(self.axes.c2p(x, 0), color=YELLOW, radius=0.09) for x in xs])
        cap = self.ja_text("点が並ぶ速さ", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("条件付き期待", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\lambda(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\lambda(t)=\lim_{h\downarrow0}\frac{P(N(t+h)-N(t)=1\mid\mathcal{F}_t)}{h}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\lambda(t)=\lim_{h\downarrow0}\frac{P(N(t+h)-N(t)=1\mid\mathcal{F}_t)}{h}").scale(0.58)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
