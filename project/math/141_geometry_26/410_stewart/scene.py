from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class StewartTheorem(PacedScene):
    """#410 スチュワート：チェビアンの長さの公式（約45秒）"""

    def construct(self):
        self.show_heading("スチュワートの定理")
        self.draw_triangle()
        self.lengths()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.2
        self.B = LEFT * 2.8 + DOWN * 1.5
        self.C = RIGHT * 2.8 + DOWN * 1.5
        self.D = 0.4 * self.B + 0.6 * self.C
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        cev = Line(self.A, self.D, color=ORANGE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.1)
        self.play(Create(cev), FadeIn(Dot(self.D, color=YELLOW, radius=0.09)), run_time=0.9)
        note = self.ja_text("チェビアン", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def lengths(self):
        labs = VGroup(
            MathTex("a", font_size=30).next_to(Line(self.B, self.C), DOWN, buff=0.15),
            MathTex("d", font_size=30).next_to(Line(self.A, self.D), RIGHT, buff=0.1),
            MathTex("m", font_size=28).next_to(Line(self.B, self.D), DOWN, buff=0.35),
            MathTex("n", font_size=28).next_to(Line(self.D, self.C), DOWN, buff=0.35),
        )
        cap = self.ja_text("辺の長さ", font_size=24).move_to(self.note)
        self.play(FadeIn(labs), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("関係式へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"b^{2}m+c^{2}n=a(d^{2}+mn)").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
