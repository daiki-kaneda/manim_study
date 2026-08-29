from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LQR(PacedScene):
    """#620 LQR：二次コストを最小にする状態フィードバック（約45秒）"""

    def construct(self):
        self.show_heading("LQR")
        self.draw_cost()
        self.riccati()
        self.show_formula()
        self.read(1.4)

    def draw_cost(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.2,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.2)
        cost = axes.plot(lambda t: 1.6 * (2.2 ** (-t)), x_range=[0.05, 3.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(cost), run_time=1.3)
        note = self.ja_text("二次コスト", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def riccati(self):
        cap = self.ja_text("リッカチ方程式", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("最適ゲイン K", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"J=\int_0^\infty(x^\top Qx+u^\top Ru)\,dt").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
