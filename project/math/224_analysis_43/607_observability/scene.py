from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Observability(PacedScene):
    """#607 可観測性：出力から初期状態を復元（約45秒）"""

    def construct(self):
        self.show_heading("可観測性")
        self.draw_output()
        self.recover()
        self.show_formula()
        self.read(1.4)

    def draw_output(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[-1.5, 1.5, 1], x_length=5.5, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.15)
        import math
        curve = axes.plot(lambda t: 1.1 * math.exp(-0.45 * t) * math.sin(3.2 * t),
                          x_range=[0.05, 3.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(curve), run_time=1.4)
        note = self.ja_text("出力の履歴", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def recover(self):
        cap = self.ja_text("初期状態を復元", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("可制御の双対", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathrm{rank}\,[C^\top\ A^\top C^\top\ \cdots]=n").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
