from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class TriangleInequality(JapaneseScene):
    """#79 三角不等式（約90秒）"""

    def construct(self):
        self.origin = LEFT * 3.3 + DOWN * 1.4
        self.show_heading("三角不等式")
        self.draw_path()
        self.compare()
        self.show_formula()
        self.hold(1.2)

    def draw_path(self):
        self.a = np.array([2.4, 0.35, 0.0])
        self.b = np.array([1.1, 2.15, 0.0])
        mid = self.origin + self.a
        end = mid + self.b
        aa = Arrow(self.origin, mid, buff=0, color=BLUE, stroke_width=4)
        ab = Arrow(mid, end, buff=0, color=GREEN, stroke_width=4)
        la = MathTex("a", color=BLUE, font_size=32).next_to(aa.get_center(), DOWN, buff=0.12)
        lb = MathTex("b", color=GREEN, font_size=32).next_to(ab.get_center(), RIGHT, buff=0.1)
        self.play(GrowArrow(aa), FadeIn(la), run_time=0.55)
        self.play(GrowArrow(ab), FadeIn(lb), run_time=0.55)
        self.hold(0.4)
        self.mid, self.end = mid, end

    def compare(self):
        diag = Arrow(self.origin, self.end, buff=0, color=YELLOW, stroke_width=5)
        lab = MathTex(r"a+b", color=YELLOW, font_size=32).next_to(diag.get_center(), UL, buff=0.08)
        self.play(GrowArrow(diag), FadeIn(lab), run_time=0.7)
        note = self.ja_text("回り道は長い", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"|a+b|\le|a|+|b|").scale(1.15)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
