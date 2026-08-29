from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EulerianNumbers(PacedScene):
    """#653 オイラーアリアン数：上昇が k 個の順列を数える（約45秒）"""

    def construct(self):
        self.show_heading("オイラーアリアン数")
        self.draw_perm()
        self.ascents()
        self.show_formula()
        self.read(1.4)

    def draw_perm(self):
        nums = [2, 1, 4, 3, 5]
        boxes = VGroup(*[
            RoundedRectangle(width=0.9, height=0.9, corner_radius=0.08, color=BLUE, stroke_width=3).shift(LEFT * 2.4 + RIGHT * i * 1.2 + UP * 0.3)
            for i in range(5)
        ])
        labs = VGroup(*[MathTex(str(n), font_size=32).move_to(b) for n, b in zip(nums, boxes)])
        # ascent markers between 1-4 and 3-5
        marks = VGroup(
            Arrow(boxes[1].get_top() + UP * 0.05, boxes[2].get_top() + UP * 0.05, buff=0.05, color=ORANGE, stroke_width=3, max_tip_length_to_length_ratio=0.2),
            Arrow(boxes[3].get_top() + UP * 0.05, boxes[4].get_top() + UP * 0.05, buff=0.05, color=ORANGE, stroke_width=3, max_tip_length_to_length_ratio=0.2),
        )
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.08), FadeIn(labs), run_time=1.3)
        self.play(LaggedStart(*[GrowArrow(m) for m in marks], lag_ratio=0.15), run_time=0.8)
        note = self.ja_text("上昇箇所", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ascents(self):
        cap = self.ja_text("ascents = k", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("順列の細分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A(n,k)=\#\{\pi:\mathrm{asc}(\pi)=k\}").scale(0.75)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
