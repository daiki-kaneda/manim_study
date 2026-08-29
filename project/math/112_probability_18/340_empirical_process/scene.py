from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EmpiricalProcess(PacedScene):
    """#340 経験過程：√n (F_n−F) のゆらぎ（約45秒）"""

    def construct(self):
        self.show_heading("経験過程")
        self.draw_center()
        self.fluctuate()
        self.show_formula()
        self.read(1.4)

    def draw_center(self):
        self.axes = Axes(x_range=[-0.2, 4.2, 1], y_range=[-1.6, 1.6, 1], x_length=6.8, y_length=3.0,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25 + LEFT * 0.2)
        zero = self.axes.plot(lambda x: 0, x_range=[0.2, 4.0], color=GREY, stroke_width=2)
        self.play(Create(self.axes), Create(zero), run_time=1.1)
        note = self.ja_text("中心化", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def fluctuate(self):
        import math
        # brownian-bridge-ish wiggles
        w1 = self.axes.plot(lambda x: 0.55 * math.sin(2.2 * x) * math.exp(-0.08 * x), x_range=[0.2, 4.0], color=BLUE, stroke_width=4)
        w2 = self.axes.plot(lambda x: 0.4 * math.sin(3.1 * x + 1.0) * math.exp(-0.05 * x), x_range=[0.2, 4.0], color=TEAL, stroke_width=3)
        cap = self.ja_text("ゆらぎ", font_size=24).move_to(self.note)
        self.play(Create(w1), Create(w2), Transform(self.note, cap), run_time=1.6)
        self.read(0.3)
        cap2 = self.ja_text("√n で拡大", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\mathbb{G}_n=\sqrt{n}(F_n-F)").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
