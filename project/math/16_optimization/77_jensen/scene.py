from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class Jensen(JapaneseScene):
    """#77 凸関数とイェンゼン（約90秒）"""

    def construct(self):
        self.show_heading("凸とイェンゼン")
        self.draw_curve()
        self.draw_chord()
        self.show_formula()
        self.hold(1.2)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-2.4, 2.4, 1],
            y_range=[0, 4.2, 1],
            x_length=7.2,
            y_length=3.8,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.55)
        curve = self.axes.plot(lambda x: 0.55 * x * x, x_range=[-2.2, 2.2], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.5)
        self.play(Create(curve), run_time=0.8)
        self.hold(0.35)

    def draw_chord(self):
        x1, x2 = -1.7, 1.85
        p1 = self.axes.c2p(x1, 0.55 * x1 * x1)
        p2 = self.axes.c2p(x2, 0.55 * x2 * x2)
        chord = Line(p1, p2, color=ORANGE, stroke_width=4)
        d1 = Dot(p1, color=ORANGE, radius=0.07)
        d2 = Dot(p2, color=ORANGE, radius=0.07)
        self.play(Create(chord), FadeIn(d1), FadeIn(d2), run_time=0.7)
        xm = (x1 + x2) / 2
        mid_chord = (np.array(p1) + np.array(p2)) / 2
        mid_curve = self.axes.c2p(xm, 0.55 * xm * xm)
        drop = DashedLine(mid_chord, mid_curve, color=YELLOW, stroke_width=3)
        self.play(Create(drop), FadeIn(Dot(mid_curve, color=YELLOW, radius=0.07)), run_time=0.6)
        note = self.ja_text("弦は上", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"f\!\left(\frac{x+y}{2}\right)\le\frac{f(x)+f(y)}{2}").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=ORANGE), run_time=0.7)
        self.hold(1.2)
