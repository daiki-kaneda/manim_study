from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Rolle(PacedScene):
    """#186 ロル：端が同じ高さなら途中で傾き 0（約45秒）"""

    def construct(self):
        self.show_heading("ロルの定理")
        self.draw_curve()
        self.mark_horizontal()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-0.3, 4.2, 1],
            y_range=[-0.3, 2.4, 1],
            x_length=7.8,
            y_length=3.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.3)

        def f(x):
            return 0.55 + 1.35 * (x - 0.4) * (3.6 - x) / 2.6

        self.f = f
        self.curve = self.axes.plot(f, x_range=[0.4, 3.6], color=BLUE, stroke_width=5)
        a = Dot(self.axes.c2p(0.4, f(0.4)), color=YELLOW, radius=0.09)
        b = Dot(self.axes.c2p(3.6, f(3.6)), color=YELLOW, radius=0.09)
        chord = DashedLine(a.get_center(), b.get_center(), color=GREY_B, stroke_width=2)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), run_time=1.6)
        self.play(FadeIn(a), FadeIn(b), Create(chord), run_time=1.1)
        note = self.ja_text("同じ高さ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def mark_horizontal(self):
        # max of parabola-like: at midpoint x=2.0
        c = 2.0
        p = self.axes.c2p(c, self.f(c))
        tang = Line(
            self.axes.c2p(c - 1.1, self.f(c)),
            self.axes.c2p(c + 1.1, self.f(c)),
            color=ORANGE,
            stroke_width=4,
        )
        dot = Dot(p, color=ORANGE, radius=0.1)
        cap = self.ja_text("傾き 0", font_size=24).move_to(self.note)
        self.play(FadeIn(dot), Create(tang), Transform(self.note, cap), run_time=1.6)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"f(a)=f(b)\Rightarrow\exists\,c,\;f'(c)=0").scale(0.78)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
