from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Entropy(JapaneseScene):
    """#123 エントロピー（約90秒）"""

    def construct(self):
        self.show_heading("エントロピー")
        self.draw_coins()
        self.show_formula()
        self.hold(1.2)

    def _bars(self, heights, colors, origin):
        g = VGroup()
        for i, (h, c) in enumerate(zip(heights, colors)):
            bar = Rectangle(width=0.7, height=h, color=c, fill_opacity=0.85, stroke_width=1)
            bar.move_to(origin + RIGHT * (i * 1.0) + UP * (h / 2))
            g.add(bar)
        return g

    def draw_coins(self):
        left = LEFT * 5.2 + DOWN * 1.4
        right = RIGHT * 0.3 + DOWN * 1.4
        fair = self._bars([2.4, 2.4], [BLUE, GREEN], left)
        biased = self._bars([3.6, 0.7], [BLUE, GREEN], right)
        self.play(FadeIn(fair), run_time=0.6)
        lf = self.ja_text("公平", font_size=24).next_to(fair, UP, buff=0.3)
        self.play(FadeIn(lf), run_time=0.3)
        self.hold(0.4)
        self.play(FadeIn(biased), run_time=0.6)
        lb = self.ja_text("偏ると小さい", font_size=24).next_to(biased, UP, buff=0.3)
        self.play(FadeIn(lb), run_time=0.3)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"H=-\sum p_i\log p_i").scale(1.1)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
