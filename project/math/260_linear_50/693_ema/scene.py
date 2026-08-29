from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EMA(PacedScene):
    """#693 EMA：指数移動平均で平滑化（約45秒）"""

    def construct(self):
        self.show_heading("EMA")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.2, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.2 + UP * 0.15)
        noisy = axes.plot(lambda t: 1.0 + 0.35 * (1 if int(3 * t) % 2 == 0 else -1) * (0.5), x_range=[0.1, 3.8], color=GREY, stroke_width=2)
        smooth = axes.plot(lambda t: 1.0 + 0.15 * (2.0 ** (-0.3 * t)), x_range=[0.1, 3.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(noisy), Create(smooth), run_time=1.4)

        note = self.ja_text("時系列を平滑", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("減衰係数 β", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("最適化でも使う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"m_t=\beta m_{t-1}+(1-\beta)x_t").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
