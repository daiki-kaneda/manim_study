from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ComparisonPrinciple(PacedScene):
    """#643 比較原理：劣解≤優解から一意性（約45秒）"""

    def construct(self):
        self.show_heading("比較原理")
        self.draw_two()
        self.order()
        self.show_formula()
        self.read(1.4)

    def draw_two(self):
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        lo = axes.plot(lambda x: 0.5 + 0.2 * x, x_range=[0.1, 2.8], color=BLUE, stroke_width=3)
        hi = axes.plot(lambda x: 1.4 + 0.15 * x, x_range=[0.1, 2.8], color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(lo), Create(hi),
                  FadeIn(MathTex(r"u", font_size=28).next_to(lo, LEFT, buff=0.1)),
                  FadeIn(MathTex(r"v", font_size=28).next_to(hi, LEFT, buff=0.1)), run_time=1.4)
        note = self.ja_text("劣解と優解", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def order(self):
        cap = self.ja_text("常に u≤v", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("一意性の鍵", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"u|_{\partial}\le v|_{\partial}\ \Rightarrow\ u\le v").scale(0.75)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
