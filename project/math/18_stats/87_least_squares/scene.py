from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class LeastSquares(JapaneseScene):
    """#87 最小二乗（約90秒）"""

    def construct(self):
        self.show_heading("最小二乗")
        self.draw_points()
        self.fit()
        self.show_formula()
        self.hold(1.2)

    def draw_points(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 4.4, 1],
            x_length=7.0,
            y_length=3.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.7)
        self.xy = [(0.7, 1.1), (1.6, 1.55), (2.5, 2.35), (3.3, 2.6), (4.2, 3.35)]
        self.play(Create(self.axes), run_time=0.5)
        dots = VGroup(*[Dot(self.axes.c2p(x, y), radius=0.08, color=BLUE) for x, y in self.xy])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.1), run_time=0.7)
        self.hold(0.35)
        self.dots = dots

    def _line(self, slope, intercept, color=ORANGE):
        return self.axes.plot(lambda x: slope * x + intercept, x_range=[0.3, 4.8], color=color, stroke_width=4)

    def _residuals(self, slope, intercept, color=YELLOW):
        segs = VGroup()
        for x, y in self.xy:
            yhat = slope * x + intercept
            segs.add(DashedLine(self.axes.c2p(x, y), self.axes.c2p(x, yhat), color=color, stroke_width=3))
        return segs

    def fit(self):
        bad = self._line(0.15, 2.4)
        res = self._residuals(0.15, 2.4)
        note = self.ja_text("ずれが大きい", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(Create(bad), FadeIn(res), FadeIn(note), run_time=0.75)
        self.hold(0.5)
        good = self._line(0.58, 0.7, color=YELLOW)
        res2 = self._residuals(0.58, 0.7)
        cap = self.ja_text("ずれが小さい", font_size=24).move_to(note)
        self.play(Transform(bad, good), Transform(res, res2), Transform(note, cap), run_time=0.9)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\min\sum_i (y_i-\hat y_i)^2").scale(1.0)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
