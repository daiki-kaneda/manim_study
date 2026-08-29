from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LRSchedule(PacedScene):
    """#670 学習率スケジュール：訓練中に η を変化させる（約45秒）"""

    def construct(self):
        self.show_heading("学習率スケジュール")
        self.draw()
        self.kinds()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.2, y_length=2.3,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.2 + UP * 0.15)
        cosine = axes.plot(lambda t: 0.3 + 1.2 * (0.5 * (1 + (2.5 ** (-0.01))) * abs(__import__('math').cos(0.9 * t))), x_range=[0.05, 3.8], color=BLUE, stroke_width=3)
        # simpler cosine decay
        import math
        cosine = axes.plot(lambda t: 0.25 + 1.3 * (0.5 * (1 + math.cos(math.pi * t / 3.8))), x_range=[0.05, 3.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(cosine), run_time=1.4)
        note = self.ja_text("η(t) の形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def kinds(self):
        cap = self.ja_text("cosine / step", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("収束を助ける", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\eta_t=\eta_{\min}+\tfrac12(\eta_{\max}-\eta_{\min})(1+\cos\pi t/T)").scale(0.52)
        formula.to_edge(DOWN, buff=0.18)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
