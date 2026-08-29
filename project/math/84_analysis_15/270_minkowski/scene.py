from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class MinkowskiInequality(PacedScene):
    """#270 ミンコフスキー：ノルムの三角不等式（約45秒）"""

    def construct(self):
        self.show_heading("ミンコフスキーの不等式")
        self.draw_vectors()
        self.compare_norms()
        self.show_formula()
        self.read(1.4)

    def draw_vectors(self):
        self.O = LEFT * 1.2 + DOWN * 0.3
        a_end = self.O + RIGHT * 2.4 + UP * 1.1
        b_end = a_end + RIGHT * 1.5 + UP * 0.9
        self.a = Arrow(self.O, a_end, buff=0, color=BLUE, stroke_width=5)
        self.b = Arrow(a_end, b_end, buff=0, color=TEAL, stroke_width=5)
        self.s = Arrow(self.O, b_end, buff=0, color=ORANGE, stroke_width=5)
        self.play(GrowArrow(self.a), run_time=1.0)
        self.play(GrowArrow(self.b), run_time=1.0)
        note = self.ja_text("2 本の矢印", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.b_end = b_end

    def compare_norms(self):
        cap = self.ja_text("和の長さ", font_size=24).move_to(self.note)
        self.play(GrowArrow(self.s), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        # dashed equal-length path along a then b as comparison idea
        brace = BraceBetweenPoints(self.O, self.b_end, direction=DOWN, color=YELLOW)
        cap2 = self.ja_text("≤ 長さの和", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\|x+y\|_p\le\|x\|_p+\|y\|_p").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
