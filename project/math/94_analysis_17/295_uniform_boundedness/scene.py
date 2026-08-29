from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class UniformBoundedness(PacedScene):
    """#295 一様有界性：点ごと有界なら一様有界（約45秒）"""

    def construct(self):
        self.show_heading("一様有界性原理")
        self.draw_ops()
        self.uniform()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        self.bars = VGroup()
        heights = [1.2, 1.8, 1.4, 2.0, 1.6]
        for i, h in enumerate(heights):
            b = Rectangle(width=0.7, height=h, color=BLUE, fill_opacity=0.5, stroke_width=2)
            b.move_to(LEFT * 2.8 + RIGHT * i * 1.05 + UP * (h / 2 - 0.5))
            self.bars.add(b)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in self.bars], lag_ratio=0.1), run_time=1.5)
        note = self.ja_text("作用素ごと", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def uniform(self):
        line = DashedLine(LEFT * 3.4 + UP * 1.55, RIGHT * 2.4 + UP * 1.55, color=ORANGE, stroke_width=4)
        cap = self.ja_text("同じ天井", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("一様に有界", font_size=24).move_to(self.note)
        box = SurroundingRectangle(self.bars, color=YELLOW, buff=0.18)
        self.play(Create(box), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\sup_n\|T_n x\|<\infty\ \Rightarrow\ \sup_n\|T_n\|<\infty").scale(0.7)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
