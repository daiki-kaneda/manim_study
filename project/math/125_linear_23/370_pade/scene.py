from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PadeApproximation(PacedScene):
    """#370 パデ近似：有理関数で級数を合わせる（約45秒）"""

    def construct(self):
        self.show_heading("パデ近似")
        self.draw_series()
        self.rational()
        self.show_formula()
        self.read(1.4)

    def draw_series(self):
        self.axes = Axes(x_range=[-0.2, 3.5, 1], y_range=[-0.5, 3.0, 1], x_length=5.5, y_length=3.0,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.8 + UP * 0.15)
        import math
        f = self.axes.plot(lambda x: math.exp(0.7 * x) - 0.3, x_range=[0.1, 2.8], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(f), run_time=1.4)
        note = self.ja_text("級数の関数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def rational(self):
        import math
        # simple rational-looking curve nearby
        r = self.axes.plot(lambda x: (1 + 0.9 * x) / (1 - 0.15 * x), x_range=[0.1, 2.5], color=ORANGE, stroke_width=4)
        frac = MathTex(r"\frac{P_m}{Q_n}", color=ORANGE, font_size=40).shift(RIGHT * 2.8 + UP * 0.8)
        cap = self.ja_text("有理近似", font_size=24).move_to(self.note)
        self.play(Create(r), FadeIn(frac), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("係数を合わせる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"f(x)-\frac{P_m(x)}{Q_n(x)}=O(x^{m+n+1})").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
