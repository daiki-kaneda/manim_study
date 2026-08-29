from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class LawOfLargeNumbers(PacedScene):
    """#411 大数の法則：標本平均 → 期待値（約45秒）"""

    def construct(self):
        self.show_heading("大数の法則")
        self.draw_avg()
        self.converge()
        self.show_formula()
        self.read(1.4)

    def draw_avg(self):
        axes = Axes(x_range=[0, 8, 1], y_range=[0, 2.2, 1], x_length=7.2, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.3)
        ys = [0.5, 1.4, 0.8, 1.5, 1.1, 1.3, 1.15, 1.22, 1.2]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([axes.c2p(i, y) for i, y in enumerate(ys)])
        self.play(Create(axes), Create(path), run_time=1.5)
        note = self.ja_text("標本平均", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def converge(self):
        line = DashedLine(self.axes.c2p(0, 1.2), self.axes.c2p(8, 1.2), color=ORANGE, stroke_width=3)
        cap = self.ja_text("期待値へ", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("ほとんど確実", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\bar{X}_n \to \mathbb{E}[X]\ \mathrm{a.s.}").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
