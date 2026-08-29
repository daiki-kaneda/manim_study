from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class FTC(JapaneseScene):
    """#104 微分積分学の基本定理（約90秒）"""

    def construct(self):
        self.show_heading("基本定理")
        self.draw_area()
        self.show_increment()
        self.show_formula()
        self.hold(1.2)

    def draw_area(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 3.2, 1],
            x_length=7.2,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.55)
        self.curve = self.axes.plot(lambda x: 0.28 * x * x + 0.45, x_range=[0.2, 3.8], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.45)
        self.play(Create(self.curve), run_time=0.7)
        area = self.axes.get_area(self.curve, x_range=[1.0, 3.0], color=YELLOW, opacity=0.4)
        self.play(FadeIn(area), run_time=0.6)
        a = MathTex("a", font_size=28).next_to(self.axes.c2p(1.0, 0), DOWN, buff=0.12)
        b = MathTex("b", font_size=28).next_to(self.axes.c2p(3.0, 0), DOWN, buff=0.12)
        self.play(FadeIn(a), FadeIn(b), run_time=0.35)
        note = self.ja_text("面積", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.55)
        self.note = note

    def show_increment(self):
        cap = self.ja_text("F の増分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.55)

    def show_formula(self):
        formula = MathTex(r"\int_a^b f(x)\,dx=F(b)-F(a)").scale(0.95)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
