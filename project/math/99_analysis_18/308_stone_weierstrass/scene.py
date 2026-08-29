from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class StoneWeierstrass(PacedScene):
    """#308 ストーン・ワイエルシュトラス：代数で一様近似（約45秒）"""

    def construct(self):
        self.show_heading("ストーン・ワイエルシュトラス")
        self.draw_target()
        self.approximate()
        self.show_formula()
        self.read(1.4)

    def draw_target(self):
        self.axes = Axes(x_range=[0, 4.2, 1], y_range=[-0.5, 2.5, 1], x_length=6.5, y_length=3.0,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.2)
        import math
        f = self.axes.plot(lambda x: 1.2 + 0.6 * math.sin(1.7 * x), x_range=[0.2, 4.0], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(f), run_time=1.4)
        note = self.ja_text("連続関数", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def approximate(self):
        import math
        p = self.axes.plot(lambda x: 1.2 + 0.55 * math.sin(1.7 * x) + 0.08 * math.sin(5 * x), x_range=[0.2, 4.0], color=ORANGE, stroke_width=4)
        cap = self.ja_text("多項式で近似", font_size=24).move_to(self.note)
        self.play(Create(p), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("一様に近い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\overline{\mathcal{A}}=C(K)").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
