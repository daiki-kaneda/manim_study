from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AdaFactor(PacedScene):
    """#742 AdaFactor：事実上の低ランク2次統計（約45秒）"""

    def construct(self):
        self.show_heading("AdaFactor")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        mat = RoundedRectangle(width=3.2, height=2.0, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 0.5 + UP * 0.2)
        row = Line(mat.get_left() + UP * 0.6, mat.get_right() + UP * 0.6, color=ORANGE, stroke_width=4)
        col = Line(mat.get_bottom() + RIGHT * 0.8, mat.get_top() + RIGHT * 0.8, color=TEAL, stroke_width=4)
        self.play(Create(mat), Create(row), Create(col), run_time=1.4)
        note = self.ja_text("行・列で分解", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("メモリ削減", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("大規模LM向き", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"R_{i}\approx\mathbb{E}[G_{i:}^2],\ C_{j}\approx\mathbb{E}[G_{:j}^2]").scale(0.58)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
