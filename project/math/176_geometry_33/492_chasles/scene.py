from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ChaslesTheorem(PacedScene):
    """#492 シャールの定理：根軸の共点（約45秒）"""

    def construct(self):
        self.show_heading("シャールの定理")
        self.draw_circles()
        self.radical()
        self.show_formula()
        self.read(1.4)

    def draw_circles(self):
        c1 = Circle(radius=1.2, color=BLUE, stroke_width=3).shift(LEFT * 1.8 + UP * 0.4)
        c2 = Circle(radius=1.0, color=TEAL, stroke_width=3).shift(RIGHT * 0.3 + UP * 0.6)
        c3 = Circle(radius=1.35, color=ORANGE, stroke_width=3).shift(DOWN * 0.9 + LEFT * 0.2)
        self.play(Create(c1), Create(c2), Create(c3), run_time=1.4)
        note = self.ja_text("3 円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def radical(self):
        lines = VGroup(
            Line(UP * 1.8 + LEFT * 0.5, DOWN * 1.8 + LEFT * 0.5, color=YELLOW, stroke_width=3),
            Line(LEFT * 2.8 + DOWN * 0.2, RIGHT * 2.5 + UP * 0.6, color=YELLOW, stroke_width=3),
            Line(LEFT * 2.2 + UP * 1.5, RIGHT * 2.0 + DOWN * 1.6, color=YELLOW, stroke_width=3),
        )
        p = Dot(LEFT * 0.5 + DOWN * 0.05, color=RED, radius=0.1)
        cap = self.ja_text("根軸が共点", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.15), FadeIn(p), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("根心", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("3 円の根軸は一点で交わる", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
