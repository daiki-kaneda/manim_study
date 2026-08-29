from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class CumulativeHazard(PacedScene):
    """#460 累積ハザード：H=-log S（約45秒）"""

    def construct(self):
        self.show_heading("累積ハザード")
        self.draw_survival()
        self.hazard()
        self.show_formula()
        self.read(1.4)

    def draw_survival(self):
        axes = Axes(x_range=[0, 5.2, 1], y_range=[0, 1.15, 1], x_length=6.5, y_length=2.6,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.4 + LEFT * 0.2)
        S = axes.plot(lambda t: np.exp(-0.35 * t), x_range=[0.05, 5.0], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(S), run_time=1.4)
        note = self.ja_text("生存関数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def hazard(self):
        H = self.axes.plot(lambda t: 0.35 * t, x_range=[0.05, 5.0], color=ORANGE, stroke_width=4)
        # rescale visually - hazard grows; clip by using secondary feel
        H = self.axes.plot(lambda t: min(1.05, 0.28 * t), x_range=[0.05, 5.0], color=ORANGE, stroke_width=4)
        cap = self.ja_text("累積ハザード", font_size=24).move_to(self.note)
        self.play(Create(H), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("ログで結ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"H(t)=-\log S(t)=\int_0^t h(u)\,du").scale(0.82)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
