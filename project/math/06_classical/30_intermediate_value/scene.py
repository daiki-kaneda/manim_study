from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class IntermediateValue(JapaneseScene):
    """#30 中間値の定理（約90秒）"""

    def construct(self):
        self.show_heading("中間値の定理")
        self.draw_continuous()
        self.contrast_jump()
        self.show_formula()
        self.hold(1.2)

    def draw_continuous(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[-2.2, 2.4, 1],
            x_length=6.2,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 1.35 + DOWN * 0.15)
        def f(x):
            return 0.7 * (x - 2.1) + 0.22 * np.sin(2.0 * (x - 2.1))

        graph = self.axes.plot(lambda x: f(x), x_range=[0.3, 3.9], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), run_time=0.55)
        self.play(Create(graph), run_time=0.85)
        a, b = 0.5, 3.7
        da = Dot(self.axes.c2p(a, f(a)), color=ORANGE, radius=0.08)
        db = Dot(self.axes.c2p(b, f(b)), color=ORANGE, radius=0.08)
        la = MathTex("a", font_size=28).next_to(self.axes.c2p(a, 0), DOWN, buff=0.12)
        lb = MathTex("b", font_size=28).next_to(self.axes.c2p(b, 0), DOWN, buff=0.12)
        self.play(FadeIn(da), FadeIn(db), FadeIn(la), FadeIn(lb), run_time=0.5)
        zero = DashedLine(
            self.axes.c2p(0.2, 0),
            self.axes.c2p(4.0, 0),
            color=GREY,
            stroke_width=1.5,
        )
        self.play(Create(zero), run_time=0.35)
        cross = Dot(self.axes.c2p(2.1, 0), color=YELLOW, radius=0.09)
        note = self.ja_text("連続なら 0 を通る", font_size=26)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(cross), FadeIn(note), run_time=0.55)
        self.hold(0.9)
        self.graph, self.note = graph, note
        self.da, self.db, self.cross = da, db, cross

    def contrast_jump(self):
        jump_note = self.ja_text("不連続なら飛び越えられる", font_size=24)
        jump_note.move_to(self.note)
        left = self.axes.plot(lambda x: -1.15, x_range=[0.4, 2.0], color=RED, stroke_width=4)
        right = self.axes.plot(lambda x: 1.15, x_range=[2.0, 3.8], color=RED, stroke_width=4)
        self.play(
            FadeOut(self.graph),
            FadeOut(self.da),
            FadeOut(self.db),
            FadeOut(self.cross),
            FadeIn(left),
            FadeIn(right),
            Transform(self.note, jump_note),
            run_time=0.8,
        )
        self.hold(0.9)

    def show_formula(self):
        formula = VGroup(
            self.ja_text("連続な f が", font_size=26),
            MathTex(r"f(a)<0<f(b)", font_size=32),
            self.ja_text("なら", font_size=26),
            MathTex(r"f(c)=0", font_size=32),
        ).arrange(RIGHT, buff=0.14)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
