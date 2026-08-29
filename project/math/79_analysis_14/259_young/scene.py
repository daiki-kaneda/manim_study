from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class YoungInequality(PacedScene):
    """#259 ヤング：積はべきの和で押さえる（約45秒）"""

    def construct(self):
        self.show_heading("ヤングの不等式")
        self.draw_axes_curve()
        self.split_areas()
        self.show_formula()
        self.read(1.4)

    def draw_axes_curve(self):
        self.axes = Axes(
            x_range=[0, 3.2, 1],
            y_range=[0, 3.2, 1],
            x_length=4.8,
            y_length=4.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 1.8 + DOWN * 0.15)
        # y = x^{p-1} with p=2 → y=x
        self.curve = self.axes.plot(lambda x: x, x_range=[0.05, 2.6], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.curve), run_time=1.3)
        note = self.ja_text("曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def split_areas(self):
        a, b = 1.8, 1.8
        # rectangle ab
        rect = Rectangle(
            width=abs(self.axes.c2p(a, 0)[0] - self.axes.c2p(0, 0)[0]),
            height=abs(self.axes.c2p(0, b)[1] - self.axes.c2p(0, 0)[1]),
            color=GREY_B,
            stroke_width=2,
        )
        rect.move_to(self.axes.c2p(a / 2, b / 2))
        self.play(Create(rect), run_time=1.0)
        # areas under and left of curve
        under = self.axes.get_area(self.curve, x_range=[0.05, a], color=TEAL, opacity=0.45)
        cap = self.ja_text("2 つの面積", font_size=24).move_to(self.note)
        self.play(FadeIn(under), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        # point (a,b)
        self.play(FadeIn(Dot(self.axes.c2p(a, b), color=ORANGE, radius=0.1)), run_time=0.5)
        cap2 = self.ja_text("積 ≤ 和", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"ab\le\frac{a^{p}}{p}+\frac{b^{q}}{q}").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
