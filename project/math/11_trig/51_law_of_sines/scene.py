from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class LawOfSines(JapaneseScene):
    """#51 正弦定理（約90秒）"""

    def construct(self):
        self.show_heading("正弦定理")
        self.draw_triangle_and_circle()
        self.label_parts()
        self.show_formula()
        self.hold(1.2)

    def draw_triangle_and_circle(self):
        self.A = LEFT * 2.1 + UP * 1.55
        self.B = LEFT * 3.4 + DOWN * 1.35
        self.C = RIGHT * 0.55 + DOWN * 1.15
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.circ = Circle.from_three_points(self.A, self.B, self.C, color=GREY, stroke_width=2)
        self.play(Create(self.circ), run_time=0.7)
        self.play(Create(self.tri), run_time=0.7)
        self.hold(0.4)

    def label_parts(self):
        la = MathTex("A", font_size=30).next_to(self.A, UP, buff=0.1)
        lb = MathTex("B", font_size=30).next_to(self.B, DL, buff=0.08)
        lc = MathTex("C", font_size=30).next_to(self.C, DR, buff=0.08)
        a = MathTex("a", color=YELLOW, font_size=32).move_to((self.B + self.C) / 2 + DOWN * 0.32)
        b = MathTex("b", color=BLUE, font_size=32).move_to((self.A + self.C) / 2 + RIGHT * 0.28)
        c = MathTex("c", color=GREEN, font_size=32).move_to((self.A + self.B) / 2 + LEFT * 0.28)
        self.play(FadeIn(la), FadeIn(lb), FadeIn(lc), run_time=0.45)
        self.play(FadeIn(a), FadeIn(b), FadeIn(c), run_time=0.5)
        o = self.circ.get_center()
        r_line = Line(o, self.A, color=ORANGE, stroke_width=3)
        r_lab = MathTex("R", color=ORANGE, font_size=30).next_to(r_line.get_center(), RIGHT, buff=0.08)
        self.play(Create(r_line), FadeIn(r_lab), FadeIn(Dot(o, radius=0.05, color=ORANGE)), run_time=0.6)
        note = self.ja_text("外接円の半径 R", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\frac{a}{\sin A}=\frac{b}{\sin B}=\frac{c}{\sin C}=2R").scale(0.85)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
