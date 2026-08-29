from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class RMSProp(PacedScene):
    """#453 RMSProp：勾配二乗平均で歩幅を調整（約45秒）"""

    def construct(self):
        self.show_heading("RMSProp")
        self.draw_grad()
        self.scale()
        self.show_formula()
        self.read(1.4)

    def draw_grad(self):
        axes = Axes(x_range=[0, 5.2, 1], y_range=[0, 1.4, 1], x_length=6.0, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.45)
        g = axes.plot(lambda t: 0.3 + 0.7 * abs(__import__("math").sin(1.7 * t)), x_range=[0.1, 5.0], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(g), run_time=1.4)
        note = self.ja_text("勾配の大きさ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def scale(self):
        smooth = self.axes.plot(lambda t: 0.55 + 0.15 * abs(__import__("math").sin(0.8 * t)), x_range=[0.1, 5.0], color=ORANGE, stroke_width=4)
        cap = self.ja_text("二乗平均で割る", font_size=24).move_to(self.note)
        self.play(Create(smooth), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("歩幅を安定化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x\leftarrow x-\eta g/\sqrt{v+\epsilon}").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
