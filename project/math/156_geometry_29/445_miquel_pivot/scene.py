from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class MiquelPivot(PacedScene):
    """#445 ミケル枢軸：完全四辺形の共円（約45秒）"""

    def construct(self):
        self.show_heading("ミケル枢軸")
        self.draw_lines()
        self.circles()
        self.show_formula()
        self.read(1.4)

    def draw_lines(self):
        # four lines forming complete quadrilateral schematic
        lines = VGroup(
            Line(LEFT * 3.2 + UP * 1.8, RIGHT * 3.2 + UP * 0.6, color=BLUE, stroke_width=2),
            Line(LEFT * 3.2 + DOWN * 0.2, RIGHT * 3.2 + DOWN * 1.6, color=BLUE, stroke_width=2),
            Line(LEFT * 2.0 + UP * 2.2, LEFT * 0.5 + DOWN * 2.0, color=TEAL, stroke_width=2),
            Line(RIGHT * 0.2 + UP * 2.2, RIGHT * 2.2 + DOWN * 2.0, color=TEAL, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.1), run_time=1.5)
        note = self.ja_text("4 直線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def circles(self):
        c1 = Circle(radius=1.1, color=ORANGE, stroke_width=2).shift(LEFT * 1.2 + UP * 0.3)
        c2 = Circle(radius=1.0, color=YELLOW, stroke_width=2).shift(RIGHT * 1.0 + DOWN * 0.2)
        m = Dot(ORIGIN + DOWN * 0.1, color=RED, radius=0.11)
        cap = self.ja_text("三角形の外接円", font_size=24).move_to(self.note)
        self.play(Create(c1), Create(c2), Transform(self.note, cap), run_time=1.3)
        self.read(0.2)
        cap2 = self.ja_text("一点で会う", font_size=24).move_to(self.note)
        self.play(FadeIn(m, scale=0.5), Transform(self.note, cap2), run_time=1.1)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("外接円は共点（枢軸）", font_size=28)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
