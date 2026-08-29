from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Perspector(PacedScene):
    """#566 配景の中心：対応頂点を結ぶ線の共点（約45秒）"""

    def construct(self):
        self.show_heading("配景の中心")
        self.draw_two()
        self.perspect()
        self.show_formula()
        self.read(1.4)

    def draw_two(self):
        t1 = Polygon(UP * 2.0, LEFT * 2.4 + DOWN * 1.2, RIGHT * 2.0 + DOWN * 1.3, color=BLUE, stroke_width=3)
        t2 = Polygon(UP * 0.9, LEFT * 1.2 + DOWN * 0.3, RIGHT * 1.0 + DOWN * 0.4, color=TEAL, stroke_width=3)
        self.play(Create(t1), Create(t2), run_time=1.3)
        note = self.ja_text("2 三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.t1, self.t2 = t1, t2

    def perspect(self):
        # approximate joining corresponding vertices
        lines = VGroup(
            Line(UP * 2.0, UP * 0.9, color=ORANGE, stroke_width=3),
            Line(LEFT * 2.4 + DOWN * 1.2, LEFT * 1.2 + DOWN * 0.3, color=ORANGE, stroke_width=3),
            Line(RIGHT * 2.0 + DOWN * 1.3, RIGHT * 1.0 + DOWN * 0.4, color=ORANGE, stroke_width=3),
        )
        p = Dot(UP * 0.2 + LEFT * 0.1, color=YELLOW, radius=0.1)
        cap = self.ja_text("対応頂点が共点", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.1), FadeIn(p), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("配景中心", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("配景：対応頂点を結ぶ線が共点", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
