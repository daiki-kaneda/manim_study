from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class ApolloniusMedian(PacedScene):
    """#252 アポロニウス：中線の長さの公式（約45秒）"""

    def construct(self):
        self.show_heading("アポロニウスの定理")
        self.draw_triangle()
        self.median()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.8 + UP * 1.6
        self.B = LEFT * 2.6 + DOWN * 1.6
        self.C = RIGHT * 3.0 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def median(self):
        M = 0.5 * (self.B + self.C)
        med = Line(self.A, M, color=ORANGE, stroke_width=4)
        self.play(Create(med), FadeIn(Dot(M, color=YELLOW, radius=0.09)), run_time=1.3)
        cap = self.ja_text("中線", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.3)
        # highlight sides AB, AC, BC briefly
        self.play(
            Indicate(Line(self.A, self.B), color=BLUE),
            Indicate(Line(self.A, self.C), color=TEAL),
            Indicate(Line(self.B, self.C), color=GREY_B),
            run_time=1.2,
        )
        cap2 = self.ja_text("辺で表す", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"m_a^{2}=\frac{2b^{2}+2c^{2}-a^{2}}{4}").scale(0.85)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
