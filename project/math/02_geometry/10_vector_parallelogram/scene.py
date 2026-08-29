from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class VectorParallelogram(JapaneseScene):
    """#10 ベクトルと平行四辺形（約90秒）"""

    def construct(self):
        self.show_heading("ベクトルの加法")
        self.draw_vectors()
        self.complete_parallelogram()
        self.show_sum()
        self.hold(1.2)

    def draw_vectors(self):
        self.origin = LEFT * 2.6 + DOWN * 1.1
        self.a = np.array([2.8, 0.55, 0.0])
        self.b = np.array([0.95, 2.15, 0.0])
        self.arrow_a = Arrow(
            self.origin, self.origin + self.a, buff=0, color=BLUE, stroke_width=4, max_tip_length_to_length_ratio=0.12
        )
        self.arrow_b = Arrow(
            self.origin, self.origin + self.b, buff=0, color=ORANGE, stroke_width=4, max_tip_length_to_length_ratio=0.12
        )
        lab_a = MathTex(r"\vec{a}", color=BLUE, font_size=36).next_to(self.arrow_a, DOWN, buff=0.12)
        lab_b = MathTex(r"\vec{b}", color=ORANGE, font_size=36).next_to(self.arrow_b, LEFT, buff=0.12)
        self.play(GrowArrow(self.arrow_a), FadeIn(lab_a), run_time=0.8)
        self.hold(0.5)
        self.play(GrowArrow(self.arrow_b), FadeIn(lab_b), run_time=0.8)
        self.hold(0.6)

    def complete_parallelogram(self):
        a_shift = Arrow(
            self.origin + self.b,
            self.origin + self.a + self.b,
            buff=0,
            color=BLUE,
            stroke_width=2,
            stroke_opacity=0.7,
            max_tip_length_to_length_ratio=0.12,
        )
        b_shift = Arrow(
            self.origin + self.a,
            self.origin + self.a + self.b,
            buff=0,
            color=ORANGE,
            stroke_width=2,
            stroke_opacity=0.7,
            max_tip_length_to_length_ratio=0.12,
        )
        self.play(GrowArrow(a_shift), GrowArrow(b_shift), run_time=0.9)
        note = self.ja_text("平行四辺形", font_size=26).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.8)
        self.play(FadeOut(note), run_time=0.3)

    def show_sum(self):
        diag = Arrow(
            self.origin,
            self.origin + self.a + self.b,
            buff=0,
            color=YELLOW,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.1,
        )
        lab = MathTex(r"\vec{a}+\vec{b}", color=YELLOW, font_size=40)
        lab.next_to(diag.get_end(), UR, buff=0.15)
        self.play(GrowArrow(diag), FadeIn(lab), run_time=1.0)
        self.hold(0.9)
        formula = MathTex(r"\vec{a}+\vec{b}=\vec{b}+\vec{a}").scale(1.05)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=0.9)
        self.play(Indicate(diag, color=YELLOW), run_time=0.8)
        self.hold(1.3)
