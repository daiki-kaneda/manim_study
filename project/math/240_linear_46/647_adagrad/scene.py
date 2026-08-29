from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AdaGrad(PacedScene):
    """#647 AdaGrad：座標ごとの学習率を累積勾配で調整（約45秒）"""

    def construct(self):
        self.show_heading("AdaGrad")
        self.draw_coords()
        self.adapt()
        self.show_formula()
        self.read(1.4)

    def draw_coords(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[-1.5, 1.5, 1], x_length=4.5, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.1)
        # elongated ellipse level set
        ell = Ellipse(width=3.5, height=1.2, color=BLUE, stroke_width=3).move_to(axes.c2p(0, 0))
        self.play(Create(axes), Create(ell), run_time=1.3)
        note = self.ja_text("座標ごとに調整", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def adapt(self):
        cap = self.ja_text("大きい勾配は縮小", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("疎な特徴向き", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x_{t+1}=x_t-\frac{\eta}{\sqrt{G_t+\varepsilon}}g_t").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
