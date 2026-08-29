from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Lemoine(PacedScene):
    """#290 ルモワーヌ点：中線の等角共役（約45秒）"""

    def construct(self):
        self.show_heading("ルモワーヌ点")
        self.draw_triangle()
        self.symmedians()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1 + LEFT * 0.3
        self.B = LEFT * 2.5 + DOWN * 1.5
        self.C = RIGHT * 2.9 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def symmedians(self):
        Ma = (self.B + self.C) / 2
        Mb = (self.A + self.C) / 2
        Mc = (self.A + self.B) / 2
        # medians faint
        meds = VGroup(
            DashedLine(self.A, Ma, color=GREY, stroke_width=2),
            DashedLine(self.B, Mb, color=GREY, stroke_width=2),
            DashedLine(self.C, Mc, color=GREY, stroke_width=2),
        )
        # symmedians: reflect medians approx toward larger side — visual only
        Sa = Ma + LEFT * 0.35
        Sb = Mb + DOWN * 0.2
        Sc = Mc + RIGHT * 0.15
        syms = VGroup(
            Line(self.A, Sa, color=ORANGE, stroke_width=3),
            Line(self.B, Sb, color=ORANGE, stroke_width=3),
            Line(self.C, Sc, color=ORANGE, stroke_width=3),
        )
        cap = self.ja_text("中線", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(m) for m in meds], lag_ratio=0.1), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("類似中線", font_size=24).move_to(self.note)
        K = Dot((self.A + self.B + self.C) / 3 + RIGHT * 0.15, color=RED, radius=0.11)
        self.play(LaggedStart(*[Create(s) for s in syms], lag_ratio=0.1), FadeIn(K), Transform(self.note, cap2), run_time=1.5)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"K\sim(a^{2}:b^{2}:c^{2})").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
