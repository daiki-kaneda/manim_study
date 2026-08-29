from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GlivenkoCantelli(PacedScene):
    """#315 グリベンコ・カンテリ：経験分布が一様収束（約45秒）"""

    def construct(self):
        self.show_heading("グリベンコ・カンテリ")
        self.draw_cdf()
        self.empirical()
        self.show_formula()
        self.read(1.4)

    def draw_cdf(self):
        self.axes = Axes(x_range=[-0.2, 4.2, 1], y_range=[0, 1.15, 1], x_length=6.8, y_length=2.8,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35 + LEFT * 0.2)
        import math
        F = self.axes.plot(lambda x: 1 / (1 + math.exp(-1.6 * (x - 2.0))), x_range=[0.1, 4.0], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(F), run_time=1.4)
        note = self.ja_text("分布関数", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def empirical(self):
        # step empirical
        xs = [0.6, 1.2, 1.8, 2.3, 2.9, 3.5]
        points = [self.axes.c2p(x, i / len(xs)) for i, x in enumerate(xs, 1)]
        step = VMobject(color=ORANGE, stroke_width=4)
        corners = [self.axes.c2p(0.2, 0)]
        for i, x in enumerate(xs):
            y0 = i / len(xs)
            y1 = (i + 1) / len(xs)
            corners.append(self.axes.c2p(x, y0))
            corners.append(self.axes.c2p(x, y1))
        corners.append(self.axes.c2p(4.0, 1.0))
        step.set_points_as_corners(corners)
        cap = self.ja_text("経験分布", font_size=24).move_to(self.note)
        self.play(Create(step), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("一様に近づく", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\|F_n-F\|_{\infty}\to 0\ \mathrm{a.s.}").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
