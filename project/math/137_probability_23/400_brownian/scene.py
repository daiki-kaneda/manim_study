from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class BrownianMotion(PacedScene):
    """#400 ブラウン運動：連続なランダム経路（約45秒）"""

    def construct(self):
        self.show_heading("ブラウン運動")
        self.draw_path()
        self.properties()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[-1.5, 1.8, 1], x_length=7.2, y_length=3.2,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25)
        rng = np.random.default_rng(7)
        steps = rng.normal(0, 0.28, size=40)
        ys = np.cumsum(steps)
        ys = ys - ys[0]
        xs = np.linspace(0, 6, len(ys))
        path = VMobject(color=BLUE, stroke_width=3.5)
        path.set_points_as_corners([axes.c2p(x, y) for x, y in zip(xs, ys)])
        self.play(Create(axes), run_time=0.8)
        self.play(Create(path), run_time=1.6)
        note = self.ja_text("ランダム経路", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def properties(self):
        # variance bands ~ sqrt(t)
        upper = self.axes.plot(lambda t: 0.55 * np.sqrt(t + 0.01), x_range=[0.05, 6], color=ORANGE, stroke_width=2)
        lower = self.axes.plot(lambda t: -0.55 * np.sqrt(t + 0.01), x_range=[0.05, 6], color=ORANGE, stroke_width=2)
        cap = self.ja_text("連続だが粗い", font_size=24).move_to(self.note)
        self.play(Create(upper), Create(lower), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("分散は時間に比例", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"B_t\sim\mathcal{N}(0,t),\quad B\ \mathrm{continuous}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
