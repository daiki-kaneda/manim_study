from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class EmpiricalCDF(PacedScene):
    """#232 経験分布は階段で真の CDF へ（約45秒）"""

    def construct(self):
        self.show_heading("経験分布関数")
        self.draw_true()
        self.build_empirical()
        self.show_formula()
        self.read(1.4)

    def draw_true(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[0, 1.15, 1],
            x_length=7.8,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.2)
        # true CDF of Exp-ish: 1-e^{-x}
        self.true = self.axes.plot(lambda x: 1 - np.exp(-0.7 * x), x_range=[0.02, 4.0], color=GREY_B, stroke_width=3)
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.true), run_time=1.3)
        note = self.ja_text("真の CDF", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def build_empirical(self):
        rng = np.random.default_rng(5)
        samples = np.sort(rng.exponential(1 / 0.7, size=10))
        samples = np.clip(samples, 0.1, 3.9)
        dots = VGroup(*[Dot(self.axes.c2p(float(x), 0), radius=0.06, color=YELLOW) for x in samples])
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.08), run_time=1.2)
        # staircase
        n = len(samples)
        pts = [self.axes.c2p(0, 0)]
        for i, x in enumerate(samples):
            y = (i + 1) / n
            pts.append(self.axes.c2p(float(x), i / n))
            pts.append(self.axes.c2p(float(x), y))
        pts.append(self.axes.c2p(4.0, 1.0))
        stair = VMobject(color=TEAL, stroke_width=4)
        stair.set_points_as_corners(pts)
        cap = self.ja_text("階段関数", font_size=24).move_to(self.note)
        self.play(Create(stair), Transform(self.note, cap), run_time=1.6)
        self.read(0.3)
        cap2 = self.ja_text("一様に近づく", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"F_n(x)=\frac{1}{n}\#\{i:X_i\le x\}").scale(0.82)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
