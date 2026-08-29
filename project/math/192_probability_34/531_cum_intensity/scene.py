from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np



class CumulativeIntensity(PacedScene):
    """#531 累積強度：Λ(t)=∫λ が点の期待値（約45秒）"""

    def construct(self):
        self.show_heading("累積強度")
        self.draw_Lambda()
        self.mean()
        self.show_formula()
        self.read(1.4)

    def draw_Lambda(self):
        axes = Axes(x_range=[0, 4.5, 1], y_range=[0, 3.2, 1], x_length=6.5, y_length=2.5, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.4)
        Lam = axes.plot(lambda t: 0.4 * t + 0.15 * t ** 2 / 2, x_range=[0, 4.2], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(Lam), run_time=1.4)
        note = self.ja_text("積分した強度", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mean(self):
        cap = self.ja_text("点の期待個数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("補償過程の鍵", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\Lambda(t)=\int_0^t\lambda(s)\,ds,\quad \mathbb{E}[N(t)]=\Lambda(t)").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
