from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import odd_layer_cells


LAYER_COLORS = [BLUE, GREEN, YELLOW, ORANGE]


class OddSquares(JapaneseScene):
    """#4 奇数の和が平方数になる：L字タイル（約90秒）"""

    n = 4
    square_size = 0.55
    gap = 0.06

    def construct(self):
        self.show_title()
        self.build_layers()
        self.derive_formula()
        self.hold(1.2)

    def show_title(self):
        title = self.ja_text("奇数の和は平方数", font_size=40)
        self.play(FadeIn(title), run_time=0.8)
        self.hold(0.6)
        self.play(title.animate.scale(0.55).to_edge(UP), run_time=0.45)
        self.title = title

        series = MathTex(r"1+3+5+\cdots+(2n-1)").scale(1.05)
        series.next_to(self.title, DOWN, buff=0.28)
        self.play(Write(series), run_time=1.1)
        self.hold(0.7)
        self.series = series

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
        return origin + RIGHT * col * step + UP * row * step

    def build_layers(self):
        origin = LEFT * 4.6 + DOWN * 2.2
        self.origin = origin
        self.odd_labels = VGroup()

        for k in range(1, self.n + 1):
            color = LAYER_COLORS[(k - 1) % len(LAYER_COLORS)]
            group = VGroup()
            for col, row in odd_layer_cells(k):
                sq = self._square(color)
                sq.move_to(self._cell_center(col, row, origin))
                group.add(sq)
            self.play(FadeIn(group, scale=0.7), run_time=0.7)

            odd = 2 * k - 1
            label = MathTex(str(odd), color=color, font_size=34)
            label.to_edge(RIGHT, buff=1.0)
            label.shift(DOWN * (0.35 + 0.55 * (k - 1)))
            self.play(FadeIn(label), run_time=0.35)
            self.odd_labels.add(label)
            self.hold(0.7)

        outline = Square(
            side_length=self.n * (self.square_size + self.gap) - self.gap,
            color=WHITE,
            stroke_width=3,
        )
        outline.move_to(
            self._cell_center((self.n - 1) / 2, (self.n - 1) / 2, origin)
        )
        self.play(Create(outline), run_time=0.9)
        n_label = MathTex("n\\times n").next_to(outline, DOWN, buff=0.25)
        self.play(FadeIn(n_label), run_time=0.45)
        self.hold(1.0)
        self.outline = outline
        self.n_label = n_label

    def derive_formula(self):
        formula = MathTex(r"1+3+5+\cdots+(2n-1)=n^2").scale(1.1)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.2)
        self.play(Indicate(formula, color=BLUE), run_time=0.8)
        self.hold(1.1)

        example = MathTex(r"1+3+5+7=16=4^2").scale(0.9)
        example.next_to(formula, UP, buff=0.22)
        self.play(FadeIn(example), run_time=0.55)
        self.hold(1.4)
