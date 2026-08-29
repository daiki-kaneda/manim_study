from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class BinomialSquare(JapaneseScene):
    """#12 (a+b)² の展開：正方形の分割（約90秒）"""

    def construct(self):
        self.a = 2.3
        self.b = 1.25
        self.origin = LEFT * 4.3 + DOWN * 2.0
        self.show_heading("(a+b)² の展開")
        self.draw_square()
        self.split_regions()
        self.show_formula()
        self.hold(1.2)

    def _corner(self, x, y):
        return self.origin + RIGHT * x + UP * y

    def draw_square(self):
        side = self.a + self.b
        square = Square(side_length=side, color=WHITE, stroke_width=2)
        square.move_to(self._corner(side / 2, side / 2))
        brace_b = Brace(Line(self._corner(0, 0), self._corner(self.a, 0)), DOWN, buff=0.12)
        brace_s = Brace(Line(self._corner(self.a, 0), self._corner(side, 0)), DOWN, buff=0.12)
        lab_a = MathTex("a").next_to(brace_b, DOWN, buff=0.08)
        lab_b = MathTex("b").next_to(brace_s, DOWN, buff=0.08)
        self.play(Create(square), run_time=0.8)
        self.play(GrowFromCenter(brace_b), GrowFromCenter(brace_s), FadeIn(lab_a), FadeIn(lab_b), run_time=0.7)
        edge = MathTex(r"a+b", font_size=32).next_to(square, LEFT, buff=0.2)
        self.play(FadeIn(edge), run_time=0.4)
        self.hold(0.7)
        self.square = square
        self.side = side

    def split_regions(self):
        a, b, s = self.a, self.b, self.side
        a2 = Rectangle(width=a, height=a, color=BLUE, fill_opacity=0.7, stroke_width=1)
        a2.move_to(self._corner(a / 2, a / 2))
        b2 = Rectangle(width=b, height=b, color=ORANGE, fill_opacity=0.7, stroke_width=1)
        b2.move_to(self._corner(a + b / 2, a + b / 2))
        ab1 = Rectangle(width=a, height=b, color=GREEN, fill_opacity=0.7, stroke_width=1)
        ab1.move_to(self._corner(a / 2, a + b / 2))
        ab2 = Rectangle(width=b, height=a, color=GREEN, fill_opacity=0.7, stroke_width=1)
        ab2.move_to(self._corner(a + b / 2, a / 2))
        self.play(FadeIn(a2), run_time=0.45)
        lab_a2 = MathTex("a^2", font_size=32).move_to(a2)
        self.play(FadeIn(lab_a2), run_time=0.3)
        self.hold(0.45)
        self.play(FadeIn(b2), run_time=0.45)
        lab_b2 = MathTex("b^2", font_size=28).move_to(b2)
        self.play(FadeIn(lab_b2), run_time=0.3)
        self.hold(0.45)
        self.play(FadeIn(ab1), FadeIn(ab2), run_time=0.55)
        lab_ab = MathTex("ab", font_size=30).move_to(ab1)
        lab_ab2 = MathTex("ab", font_size=30).move_to(ab2)
        self.play(FadeIn(lab_ab), FadeIn(lab_ab2), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"(a+b)^2=a^2+2ab+b^2").scale(1.15)
        formula.to_edge(RIGHT, buff=0.45).shift(UP * 0.2)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=BLUE), run_time=0.8)
        self.hold(1.3)
