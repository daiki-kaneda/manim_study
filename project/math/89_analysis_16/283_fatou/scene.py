from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FatouLemma(PacedScene):
    """#283 ファトゥ：下極限の積分 ≤ 積分の下極限（約45秒）"""

    def construct(self):
        self.show_heading("ファトゥの補題")
        self.draw_curves()
        self.liminf()
        self.show_formula()
        self.read(1.4)

    def draw_curves(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 2.4, 1],
            x_length=6.2,
            y_length=2.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 0.5 + UP * 0.25)
        import math
        c1 = self.axes.plot(lambda x: 0.4 + 0.9 * math.exp(-((x - 1.2) ** 2) / 0.35), x_range=[0.2, 3.8], color=BLUE, stroke_width=3)
        c2 = self.axes.plot(lambda x: 0.35 + 1.1 * math.exp(-((x - 2.0) ** 2) / 0.4), x_range=[0.2, 3.8], color=TEAL, stroke_width=3)
        c3 = self.axes.plot(lambda x: 0.3 + 0.7 * math.exp(-((x - 2.8) ** 2) / 0.45), x_range=[0.2, 3.8], color=GREY, stroke_width=3)
        self.play(Create(self.axes), run_time=0.7)
        self.play(Create(c1), Create(c2), Create(c3), run_time=1.5)
        note = self.ja_text("非負の列", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def liminf(self):
        import math
        lim = self.axes.plot(
            lambda x: 0.25 + 0.55 * math.exp(-((x - 2.0) ** 2) / 0.9),
            x_range=[0.2, 3.8],
            color=ORANGE,
            stroke_width=5,
        )
        cap = self.ja_text("下極限", font_size=24).move_to(self.note)
        self.play(Create(lim), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        area = self.axes.get_area(lim, x_range=[0.4, 3.6], color=ORANGE, opacity=0.35)
        cap2 = self.ja_text("積分は小さい", font_size=24).move_to(self.note)
        self.play(FadeIn(area), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\int\liminf f_n\le\liminf\int f_n").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
