from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class Skorokhod(PacedScene):
    """#424 スコロホッド：分布収束を経路結合で表す（約45秒）"""

    def construct(self):
        self.show_heading("スコロホッド表現")
        self.draw_laws()
        self.couple()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_laws(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[0, 0.6, 0.5], x_length=6.5, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.45)
        c1 = axes.plot(lambda x: 0.45 * np.exp(-(x + 0.6) ** 2), x_range=[-2.8, 2.8], color=BLUE, stroke_width=3)
        c2 = axes.plot(lambda x: 0.5 * np.exp(-x ** 2), x_range=[-2.8, 2.8], color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(c1), Create(c2), run_time=1.5)
        note = self.ja_text("分布が近づく", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def couple(self):
        arrow = Arrow(DOWN * 0.3 + LEFT * 1.5, DOWN * 0.3 + RIGHT * 1.5, buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("同じ空間に載せる", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("ほぼ確実に収束", font_size=24).move_to(self.note)
        # shorten caption for edge
        cap2 = self.ja_text("a.s. 収束へ", font_size=24).move_to(self.note)
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
        eq = MathTex(r"X_n\Rightarrow X\ \Rightarrow\ \exists\ \tilde X_n\to\tilde X").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"X_n\Rightarrow X\ \Rightarrow\ \exists\ \tilde X_n\to\tilde X").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"X_n\Rightarrow X\ \Rightarrow\ \exists\ \tilde X_n\to\tilde X").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
