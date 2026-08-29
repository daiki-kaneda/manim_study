from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import staircase_cells


class ArithmeticSum(JapaneseScene):
    """#3 等差数列の和：階段を2つ合わせて長方形にする（約90秒）"""

    n = 5
    square_size = 0.42
    gap = 0.06

    def construct(self):
        self.show_title()
        self.show_question()
        self.build_staircase()
        self.complete_rectangle()
        self.derive_formula()
        self.hold(1.2)

    def show_title(self):
        title = self.ja_text("等差数列の和", font_size=42)
        self.play(FadeIn(title), run_time=0.8)
        self.hold(0.6)
        self.play(title.animate.scale(0.55).to_edge(UP), run_time=0.45)
        self.title = title

    def show_question(self):
        question = MathTex(r"1+2+\cdots+n = \ ?").scale(1.15)
        question.next_to(self.title, DOWN, buff=0.3)
        self.play(Write(question), run_time=1.1)
        self.hold(0.9)
        self.question = question

    def _square(self, color):
        return Square(
            side_length=self.square_size,
            color=color,
            fill_opacity=0.85,
            stroke_width=1.5,
            stroke_color=WHITE,
        )

    def _cell_center(self, col: int, row: int, origin):
        step = self.square_size + self.gap
        return origin + RIGHT * col * step + DOWN * row * step

    def build_staircase(self):
        origin = LEFT * 3.2 + UP * 1.6
        self.origin = origin
        self.blue_squares = VGroup()
        animations = []
        for col, row in staircase_cells(self.n):
            sq = self._square(BLUE)
            sq.move_to(self._cell_center(col, row, origin))
            self.blue_squares.add(sq)
            animations.append(FadeIn(sq, scale=0.6))
        self.play(LaggedStart(*animations, lag_ratio=0.08), run_time=2.4)
        self.hold(0.8)

        counts = VGroup(
            *[
                MathTex(str(row + 1), font_size=28).next_to(
                    self._cell_center(row, row, origin), RIGHT, buff=0.18
                )
                for row in range(self.n)
            ]
        )
        self.play(FadeIn(counts), run_time=0.5)
        self.hold(1.0)
        self.play(FadeOut(counts), run_time=0.35)

    def complete_rectangle(self):
        origin = self.origin
        orange_squares = VGroup()
        animations = []
        for row in range(self.n):
            for col in range(row + 1, self.n + 1):
                sq = self._square(ORANGE)
                sq.move_to(self._cell_center(col, row, origin))
                orange_squares.add(sq)
                animations.append(FadeIn(sq, scale=0.6))
        self.play(LaggedStart(*animations, lag_ratio=0.05), run_time=2.0)
        self.hold(0.8)
        self.orange_squares = orange_squares

        brace_bottom = Brace(VGroup(self.blue_squares, orange_squares), DOWN, buff=0.15)
        label_cols = MathTex(r"n+1").next_to(brace_bottom, DOWN, buff=0.1)
        brace_left = Brace(self.blue_squares, LEFT, buff=0.15)
        label_rows = MathTex("n").next_to(brace_left, LEFT, buff=0.1)
        self.play(
            GrowFromCenter(brace_bottom),
            GrowFromCenter(brace_left),
            FadeIn(label_cols),
            FadeIn(label_rows),
            run_time=0.9,
        )
        self.hold(1.3)
        self.rect_labels = VGroup(brace_bottom, brace_left, label_cols, label_rows)

    def derive_formula(self):
        two_copies = MathTex(r"2S = n(n+1)").scale(1.15)
        two_copies.next_to(self.question, DOWN, buff=0.35).to_edge(RIGHT, buff=0.7)
        self.play(Write(two_copies), run_time=1.0)
        self.hold(1.1)

        formula = MathTex(r"S = \frac{n(n+1)}{2}").scale(1.35)
        formula.next_to(two_copies, DOWN, buff=0.35).align_to(two_copies, RIGHT)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=BLUE), run_time=0.8)
        self.hold(1.3)

        example = MathTex(r"n=100 \ \Rightarrow\ 5050").scale(0.9)
        example.next_to(formula, DOWN, buff=0.3).align_to(formula, RIGHT)
        self.play(FadeIn(example), run_time=0.6)
        self.hold(1.5)
