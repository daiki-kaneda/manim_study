from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class EulerIdentity(JapaneseScene):
    """#91 オイラーの等式（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.3 + DOWN * 0.15
        self.r = 1.85
        self.show_heading("オイラーの等式")
        self.draw_circle()
        self.rotate_to_pi()
        self.show_formula()
        self.hold(1.2)

    def draw_circle(self):
        ax = Line(self.origin + LEFT * 2.4, self.origin + RIGHT * 2.5, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.2, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        circ = Circle(radius=self.r, color=WHITE, stroke_width=2).move_to(self.origin)
        self.play(Create(ax), Create(ay), Create(circ), run_time=0.7)
        one = Dot(self.origin + RIGHT * self.r, color=BLUE, radius=0.08)
        lab = MathTex("1", color=BLUE, font_size=32).next_to(one, RIGHT, buff=0.1)
        self.play(FadeIn(one), FadeIn(lab), run_time=0.4)
        self.hold(0.35)
        self.one = one

    def rotate_to_pi(self):
        arc = Arc(radius=self.r, start_angle=0, angle=PI, color=YELLOW, stroke_width=6, arc_center=self.origin)
        self.play(Create(arc), run_time=1.1)
        minus = Dot(self.origin + LEFT * self.r, color=YELLOW, radius=0.09)
        lab = MathTex("-1", color=YELLOW, font_size=32).next_to(minus, LEFT, buff=0.1)
        self.play(FadeIn(minus), FadeIn(lab), run_time=0.45)
        note = self.ja_text("半周で −1", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"e^{i\pi}+1=0").scale(1.25)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
