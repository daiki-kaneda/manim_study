from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class EmpiricalRule(JapaneseScene):
    """#90 正規分布の 68–95–99.7（約90秒）"""

    def construct(self):
        self.show_heading("68–95–99.7")
        self.draw_curve()
        self.shade()
        self.show_formula()
        self.hold(1.2)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-3.6, 3.6, 1],
            y_range=[0, 0.48, 0.2],
            x_length=9.0,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        self.curve = self.axes.plot(
            lambda x: 0.40 * math.exp(-0.5 * x * x),
            x_range=[-3.4, 3.4],
            color=WHITE,
            stroke_width=4,
        )
        self.play(Create(self.axes), run_time=0.45)
        self.play(Create(self.curve), run_time=0.75)
        self.hold(0.3)

    def shade(self):
        specs = [
            (1, BLUE, "68%"),
            (2, TEAL, "95%"),
            (3, YELLOW, "99.7%"),
        ]
        area = None
        note = self.ja_text("1σ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        for i, (s, color, pct) in enumerate(specs):
            nxt = self.axes.get_area(self.curve, x_range=[-s, s], color=color, opacity=0.45)
            lab = self.ja_text(pct, font_size=24).move_to(note)
            if area is None:
                self.play(FadeIn(nxt), FadeIn(note), run_time=0.7)
                area = nxt
                self.play(Transform(note, lab), run_time=0.3)
            else:
                self.play(Transform(area, nxt), Transform(note, lab), run_time=0.75)
            self.hold(0.4)

    def show_formula(self):
        formula = MathTex(r"1\sigma\colon 68\%,\ 2\sigma\colon 95\%,\ 3\sigma\colon 99.7\%").scale(0.78)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
