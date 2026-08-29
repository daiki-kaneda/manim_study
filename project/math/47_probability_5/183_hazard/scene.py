from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class HazardRate(PacedScene):
    """#183 ハザードはいままでの条件付き（約45秒）"""

    def construct(self):
        self.show_heading("ハザード")
        self.draw_survival()
        self.mark_hazard()
        self.show_formula()
        self.read(1.4)

    def draw_survival(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 1.15, 1],
            x_length=8.0,
            y_length=3.1,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.25)
        self.surv = self.axes.plot(lambda x: math.exp(-0.55 * x), x_range=[0.02, 4.9], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.surv), run_time=1.8)
        note = self.ja_text("生存曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def mark_hazard(self):
        t = 1.8
        # remaining mass from t onward
        area = self.axes.get_area(self.surv, x_range=[t, 4.9], color=YELLOW, opacity=0.4)
        line = DashedLine(self.axes.c2p(t, 0), self.axes.c2p(t, math.exp(-0.55 * t)), color=ORANGE, stroke_width=3)
        cap = self.ja_text("ここまで", font_size=24).move_to(self.note)
        self.play(Create(line), FadeIn(area), Transform(self.note, cap), run_time=1.5)
        self.read(0.35)
        # small slice just after t
        slice_a = self.axes.get_area(self.surv, x_range=[t, t + 0.55], color=RED, opacity=0.55)
        cap2 = self.ja_text("直後", font_size=24).move_to(self.note)
        self.play(FadeIn(slice_a), Transform(self.note, cap2), run_time=1.3)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"h(t)=\frac{f(t)}{S(t)}").scale(1.05)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
