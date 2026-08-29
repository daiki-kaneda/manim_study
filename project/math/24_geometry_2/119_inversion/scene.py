from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class CircleInversion(JapaneseScene):
    """#119 円に関する反転（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.0 + DOWN * 0.1
        self.R = 1.85
        self.show_heading("反転")
        self.draw()
        self.show_formula()
        self.hold(1.2)

    def draw(self):
        ax = Line(self.origin + LEFT * 2.4, self.origin + RIGHT * 3.3, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.2, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        circ = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        self.play(Create(ax), Create(ay), Create(circ), run_time=0.6)
        p = np.array([2.7, 0.85, 0.0])
        r2 = np.dot(p, p)
        q = (self.R ** 2 / r2) * p
        P = self.origin + p
        Q = self.origin + q
        ray = Line(self.origin, P, color=GREY, stroke_width=2)
        self.play(Create(ray), FadeIn(Dot(P, color=BLUE, radius=0.08)), run_time=0.55)
        lp = MathTex("P", color=BLUE, font_size=30).next_to(P, UR, buff=0.08)
        self.play(FadeIn(lp), run_time=0.25)
        self.play(FadeIn(Dot(Q, color=YELLOW, radius=0.08)), run_time=0.4)
        lq = MathTex(r"P'", color=YELLOW, font_size=30).next_to(Q, UL, buff=0.08)
        self.play(FadeIn(lq), run_time=0.25)
        note = self.ja_text("内外が交換", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"|OP|\,|OP'|=R^{2}").scale(1.1)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
