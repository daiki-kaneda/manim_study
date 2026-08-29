from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BigO(PacedScene):
    """#248 ビッグオーは定数倍で押さえる（約45秒）"""

    def construct(self):
        self.show_heading("オーダー記号")
        self.draw_curves()
        self.bound()
        self.show_formula()
        self.read(1.4)

    def draw_curves(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 3.2, 1],
            x_length=8.0,
            y_length=3.1,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.15)
        f = self.axes.plot(lambda x: 0.12 * x * x + 0.2, x_range=[0.1, 5.0], color=BLUE, stroke_width=5)
        g = self.axes.plot(lambda x: 0.35 * x + 0.15, x_range=[0.1, 5.0], color=GREY_B, stroke_width=3)
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(g), Create(f), run_time=1.5)
        fl = MathTex("f", color=BLUE, font_size=28).next_to(f, UP, buff=0.05).shift(RIGHT * 2.2)
        gl = MathTex("g", color=GREY_B, font_size=28).next_to(g, UP, buff=0.05).shift(LEFT * 0.5)
        self.play(FadeIn(fl), FadeIn(gl), run_time=0.45)
        note = self.ja_text("成長", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bound(self):
        # Cg above f for large x: C=2, Cg = 0.7x+0.3
        bound = self.axes.plot(lambda x: 0.7 * x + 0.3, x_range=[1.5, 5.0], color=ORANGE, stroke_width=4)
        cap = self.ja_text("定数倍で上から", font_size=24).move_to(self.note)
        self.play(Create(bound), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        region = self.axes.get_area(bound, x_range=[2.5, 5.0], color=ORANGE, opacity=0.25)
        cap2 = self.ja_text("十分先で", font_size=24).move_to(self.note)
        self.play(FadeIn(region), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"f(x)=O(g(x))").scale(1.1)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
