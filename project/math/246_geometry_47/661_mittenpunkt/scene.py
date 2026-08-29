from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Mittenpunkt(PacedScene):
    """#661 ミッテンプンクト：傍心三角形の類似中線交点（約45秒）"""

    def construct(self):
        self.show_heading("ミッテンプンクト")
        self.draw()
        self.sym()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.6 + DOWN * 1.1, RIGHT * 2.6 + DOWN * 1.1, UP * 1.7, color=BLUE, stroke_width=3)
        # excenters approx outside
        ex = VGroup(
            Dot(DOWN * 2.0, color=ORANGE, radius=0.09),
            Dot(RIGHT * 3.2 + UP * 0.8, color=ORANGE, radius=0.09),
            Dot(LEFT * 3.2 + UP * 0.8, color=ORANGE, radius=0.09),
        )
        self.play(Create(tri), FadeIn(ex), run_time=1.3)
        note = self.ja_text("傍心たち", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.ex = ex

    def sym(self):
        M = Dot(ORIGIN + DOWN * 0.2, color=TEAL, radius=0.1)
        lines = VGroup(*[DashedLine(e.get_center(), M.get_center(), color=GREY, stroke_width=2) for e in self.ex])
        cap = self.ja_text("類似中線の交点", font_size=22).move_to(self.note)
        self.play(Create(lines), FadeIn(M), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("ナーゲルと共役", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M=X(9)").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
