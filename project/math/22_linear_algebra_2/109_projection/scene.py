from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class OrthogonalProjection(JapaneseScene):
    """#109 正射影は最短（約90秒）"""

    def construct(self):
        self.origin = LEFT * 3.4 + DOWN * 1.35
        self.show_heading("正射影")
        self.draw_line_and_point()
        self.drop()
        self.show_formula()
        self.hold(1.2)

    def draw_line_and_point(self):
        self.line = Line(self.origin, self.origin + RIGHT * 6.2 + UP * 1.55, color=WHITE, stroke_width=4)
        self.p = self.origin + RIGHT * 2.15 + UP * 2.55
        self.play(Create(self.line), run_time=0.55)
        self.play(FadeIn(Dot(self.p, color=BLUE, radius=0.08)), run_time=0.35)
        lab = MathTex("x", color=BLUE, font_size=32).next_to(self.p, UP, buff=0.1)
        self.play(FadeIn(lab), run_time=0.25)
        self.hold(0.4)

    def drop(self):
        d = np.array([6.2, 1.55, 0.0])
        d = d / np.linalg.norm(d)
        rel = self.p - self.origin
        foot = self.origin + np.dot(rel, d) * d
        drop = DashedLine(self.p, foot, color=YELLOW, stroke_width=3)
        self.play(Create(drop), FadeIn(Dot(foot, color=YELLOW, radius=0.08)), run_time=0.7)
        note = self.ja_text("垂線が最短", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\mathrm{proj}_v x=\frac{x\cdot v}{v\cdot v}\,v").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
