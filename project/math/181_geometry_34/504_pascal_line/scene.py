from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PascalLine(PacedScene):
    """#504 パスカル線：内接六角形の対辺交点が共線（約45秒）"""

    def construct(self):
        self.show_heading("パスカル線")
        self.draw_conic()
        self.hexagon()
        self.show_formula()
        self.read(1.4)

    def draw_conic(self):
        ell = Ellipse(width=5.5, height=3.2, color=BLUE, stroke_width=3).shift(UP * 0.15)
        self.play(Create(ell), run_time=1.2)
        note = self.ja_text("円錐曲線上", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def hexagon(self):
        pts = [
            UP * 1.5 + LEFT * 1.2,
            UP * 0.9 + RIGHT * 1.8,
            DOWN * 0.2 + RIGHT * 2.4,
            DOWN * 1.3 + RIGHT * 0.5,
            DOWN * 1.2 + LEFT * 1.8,
            UP * 0.2 + LEFT * 2.5,
        ]
        hexagon = Polygon(*pts, color=ORANGE, stroke_width=3)
        line = Line(LEFT * 2.8 + DOWN * 0.4, RIGHT * 2.8 + UP * 0.3, color=YELLOW, stroke_width=4)
        cap = self.ja_text("対辺の交点", font_size=24).move_to(self.note)
        self.play(Create(hexagon), Transform(self.note, cap), run_time=1.3)
        self.play(Create(line), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("共線＝パスカル線", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("内接六角形の対辺交点は共線", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
