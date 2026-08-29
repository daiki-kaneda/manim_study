from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class IntegralArea(JapaneseScene):
    """#17 積分＝面積（約90秒）"""

    def construct(self):
        self.show_heading("積分")
        self.draw_curve()
        self.riemann()
        self.show_formula()
        self.hold(1.2)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            x_length=6.4,
            y_length=4.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 1.4 + DOWN * 0.4)
        self.graph = self.axes.plot(lambda x: 0.22 * (x - 0.3) ** 2 + 0.7, x_range=[0.3, 4.4], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(self.graph), run_time=0.9)
        self.hold(0.4)

    def _rects(self, n, color=GREEN):
        a, b = 0.8, 3.6
        dx = (b - a) / n
        group = VGroup()
        for i in range(n):
            x = a + i * dx
            y = 0.22 * (x - 0.3) ** 2 + 0.7
            p00 = self.axes.c2p(x, 0)
            p10 = self.axes.c2p(x + dx, 0)
            p11 = self.axes.c2p(x + dx, y)
            p01 = self.axes.c2p(x, y)
            poly = Polygon(p00, p10, p11, p01, color=color, fill_opacity=0.55, stroke_width=1)
            group.add(poly)
        return group

    def riemann(self):
        coarse = self._rects(4)
        self.play(FadeIn(coarse), run_time=0.7)
        note = self.ja_text("長方形で近似", font_size=24).to_edge(RIGHT, buff=0.5).shift(UP * 1.1)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.6)
        fine = self._rects(12, color=TEAL)
        self.play(FadeOut(coarse), FadeIn(fine), run_time=0.8)
        better = self.ja_text("細かくすると面積へ", font_size=24).move_to(note)
        self.play(Transform(note, better), run_time=0.4)
        self.hold(0.8)
        self.rects = fine
        self.note = note

    def show_formula(self):
        formula = VGroup(
            MathTex(r"\int_a^b f(x)\,dx", font_size=40),
            MathTex(r"=", font_size=40),
            self.ja_text("面積", font_size=32),
        ).arrange(RIGHT, buff=0.18)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(self.rects, color=YELLOW), run_time=0.8)
        self.hold(1.2)
