from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class MarkovInequality(PacedScene):
    """#207 マルコフ：しきい値の右は平均／a 以下（約45秒）"""

    def construct(self):
        self.show_heading("マルコフ不等式")
        self.draw_density()
        self.bound_tail()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_density(self):
        self.axes = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 1.1, 1],
            x_length=8.0,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.2)
        self.pdf = self.axes.plot(lambda x: 0.85 * math.exp(-0.55 * x), x_range=[0.05, 5.0], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.pdf), run_time=1.5)
        note = self.ja_text("正の確率", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bound_tail(self):
        a = 2.4
        line = DashedLine(self.axes.c2p(a, 0), self.axes.c2p(a, 0.95), color=ORANGE, stroke_width=3)
        tail = self.axes.get_area(self.pdf, x_range=[a, 5.0], color=RED, opacity=0.5)
        cap = self.ja_text("しきい値 a", font_size=24).move_to(self.note)
        self.play(Create(line), FadeIn(tail), Transform(self.note, cap), run_time=1.5)
        self.read(0.35)
        # mean marker
        mean_x = 1.0 / 0.55  # for Exp(0.55) mean
        mean_dot = Dot(self.axes.c2p(min(mean_x, 4.5), 0), color=YELLOW, radius=0.09)
        cap2 = self.ja_text("平均で押さえる", font_size=24).move_to(self.note)
        self.play(FadeIn(mean_dot), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"P(X\ge a)\le\frac{\mathbb{E}[X]}{a}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P(X\ge a)\le\frac{\mathbb{E}[X]}{a}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P(X\ge a)\le\frac{\mathbb{E}[X]}{a}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
