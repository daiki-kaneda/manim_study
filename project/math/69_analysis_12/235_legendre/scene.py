from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LegendreTransform(PacedScene):
    """#235 ルジャンドルは接線の切片（約45秒）"""

    def construct(self):
        self.show_heading("ルジャンドル変換")
        self.draw_convex()
        self.tangent_intercept()
        self.show_formula()
        self.read(1.4)

    def draw_convex(self):
        self.axes = Axes(
            x_range=[-0.2, 3.2, 1],
            y_range=[-0.2, 3.0, 1],
            x_length=7.2,
            y_length=3.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.1 + LEFT * 0.4)
        self.curve = self.axes.plot(lambda x: 0.35 * x * x + 0.2, x_range=[0.1, 2.9], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.curve), run_time=1.5)
        note = self.ja_text("凸関数", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def tangent_intercept(self):
        x0 = 1.6
        y0 = 0.35 * x0 * x0 + 0.2
        slope = 0.7 * x0
        # tangent: y - y0 = slope (x - x0)
        tang = self.axes.plot(lambda x: y0 + slope * (x - x0), x_range=[0.2, 2.8], color=ORANGE, stroke_width=4)
        p = Dot(self.axes.c2p(x0, y0), color=ORANGE, radius=0.1)
        self.play(FadeIn(p), Create(tang), run_time=1.3)
        # intercept on y-axis of the dual: x*p - f(x) style marker
        intercept = y0 - slope * x0
        q = Dot(self.axes.c2p(0, intercept), color=YELLOW, radius=0.1)
        dash = DashedLine(self.axes.c2p(0, intercept), self.axes.c2p(0.01, intercept), color=YELLOW)
        # vertical from origin area
        mark = Line(self.axes.c2p(0, 0), self.axes.c2p(0, max(intercept, 0.05)), color=YELLOW, stroke_width=4)
        cap = self.ja_text("接線の切片", font_size=24).move_to(self.note)
        self.play(FadeIn(q), Create(mark), Transform(self.note, cap), run_time=1.4)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"f^{*}(p)=\sup_x(px-f(x))").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
