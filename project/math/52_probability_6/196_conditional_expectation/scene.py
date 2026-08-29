from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class ConditionalExpectation(PacedScene):
    """#196 条件付き期待値は切り口の平均（約45秒）"""

    def construct(self):
        self.show_heading("条件付き期待値")
        self.draw_cloud()
        self.slice_mean()
        self.show_formula()
        self.read(1.4)

    def draw_cloud(self):
        self.axes = Axes(
            x_range=[-0.2, 4.0, 1],
            y_range=[-0.2, 3.0, 1],
            x_length=7.4,
            y_length=3.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.3)
        self.play(Create(self.axes), run_time=0.85)
        rng = np.random.default_rng(3)
        pts = []
        for _ in range(32):
            x = rng.uniform(0.4, 3.6)
            y = 0.35 * x + 0.9 + rng.normal(0, 0.45)
            y = float(np.clip(y, 0.25, 2.7))
            pts.append(Dot(self.axes.c2p(float(x), y), radius=0.05, color=BLUE))
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in pts], lag_ratio=0.03), run_time=1.7)
        note = self.ja_text("同時分布", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def slice_mean(self):
        x0 = 2.2
        line = DashedLine(self.axes.c2p(x0, 0.15), self.axes.c2p(x0, 2.8), color=ORANGE, stroke_width=3)
        cap = self.ja_text("x を固定", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.2)
        self.read(0.3)
        # regression curve E[Y|X=x] ≈ 0.35x+0.9
        reg = self.axes.plot(lambda x: 0.35 * x + 0.9, x_range=[0.35, 3.7], color=YELLOW, stroke_width=5)
        mean_dot = Dot(self.axes.c2p(x0, 0.35 * x0 + 0.9), color=RED, radius=0.1)
        cap2 = self.ja_text("切り口の平均", font_size=24).move_to(self.note)
        self.play(Create(reg), FadeIn(mean_dot), Transform(self.note, cap2), run_time=1.7)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"m(x)=\mathbb{E}[Y\mid X=x]").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
