from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class SineArea(PacedScene):
    """#434 正弦面積：S=(1/2)ab sin C（約45秒）"""

    def construct(self):
        self.show_heading("正弦面積")
        self.draw_triangle()
        self.area()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.6 + DOWN * 1.4
        self.C = RIGHT * 2.7 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("2 辺と挟角", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def area(self):
        ang = Angle(Line(self.C, self.B), Line(self.C, self.A), radius=0.45, color=ORANGE)
        fill = Polygon(self.A, self.B, self.C, color=TEAL, fill_opacity=0.35, stroke_width=0)
        cap = self.ja_text("sin で高さ", font_size=24).move_to(self.note)
        self.play(Create(ang), FadeIn(fill), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("面積へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"S=\tfrac12 ab\sin C").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
