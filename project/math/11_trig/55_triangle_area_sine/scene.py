from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class TriangleAreaSine(JapaneseScene):
    """#55 三角形の面積 ½ab sin C（約90秒）"""

    def construct(self):
        self.show_heading("面積と正弦")
        self.draw_sides()
        self.complete_parallelogram()
        self.show_formula()
        self.hold(1.2)

    def draw_sides(self):
        self.C = LEFT * 3.2 + DOWN * 1.45
        a_len, b_len = 3.4, 2.6
        self.B = self.C + RIGHT * a_len
        self.A = self.C + 0.72 * RIGHT * b_len + 0.69 * UP * b_len
        side_a = Line(self.C, self.B, color=BLUE, stroke_width=4)
        side_b = Line(self.C, self.A, color=GREEN, stroke_width=4)
        self.play(Create(side_a), Create(side_b), run_time=0.7)
        la = MathTex("a", color=BLUE, font_size=32).next_to(side_a, DOWN, buff=0.12)
        lb = MathTex("b", color=GREEN, font_size=32).next_to(side_b, LEFT, buff=0.12)
        ang = Angle.from_three_points(self.A, self.C, self.B, radius=0.4, color=ORANGE)
        g = MathTex("C", color=ORANGE, font_size=30).next_to(ang, UR, buff=0.08)
        self.play(FadeIn(la), FadeIn(lb), Create(ang), FadeIn(g), run_time=0.6)
        self.hold(0.5)
        self.side_a, self.side_b = side_a, side_b

    def complete_parallelogram(self):
        D = self.A + (self.B - self.C)
        para = Polygon(self.C, self.B, D, self.A, color=YELLOW, fill_opacity=0.25, stroke_width=2)
        tri = Polygon(self.C, self.B, self.A, color=TEAL, fill_opacity=0.55, stroke_width=2)
        self.play(FadeIn(para), run_time=0.6)
        note = self.ja_text("平行四辺形の半分", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.6)
        self.play(FadeIn(note), run_time=0.35)
        self.play(FadeIn(tri), run_time=0.55)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"S=\frac12 ab\sin C").scale(1.15)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
