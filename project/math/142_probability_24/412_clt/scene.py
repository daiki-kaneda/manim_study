from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class CentralLimitTheorem(PacedScene):
    """#412 中心極限：正規化した和は正規分布へ（約45秒）"""

    def construct(self):
        self.show_heading("中心極限定理")
        self.draw_hist()
        self.gaussian()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_hist(self):
        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[0, 0.55, 0.5], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25)
        # rough histogram bars
        xs = np.linspace(-2.5, 2.5, 11)
        heights = np.exp(-xs**2 / 2) / np.sqrt(2 * np.pi)
        bars = VGroup(*[
            Rectangle(width=0.45, height=h * 5.0, color=BLUE, fill_opacity=0.5, stroke_width=1)
            .move_to(axes.c2p(x, h * 2.5))
            for x, h in zip(xs, heights)
        ])
        self.play(Create(axes), LaggedStart(*[FadeIn(b) for b in bars], lag_ratio=0.05), run_time=1.5)
        note = self.ja_text("和の分布", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def gaussian(self):
        curve = self.axes.plot(lambda x: np.exp(-x**2 / 2) / np.sqrt(2 * np.pi), x_range=[-3.2, 3.2], color=ORANGE, stroke_width=4)
        cap = self.ja_text("正規に近づく", font_size=24).move_to(self.note)
        self.play(Create(curve), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("どんな分布からでも", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\frac{S_n-n\mu}{\sigma\sqrt{n}}\Rightarrow N(0,1)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{S_n-n\mu}{\sigma\sqrt{n}}\Rightarrow N(0,1)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{S_n-n\mu}{\sigma\sqrt{n}}\Rightarrow N(0,1)").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
