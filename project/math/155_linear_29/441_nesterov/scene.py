from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class Nesterov(PacedScene):
    """#441 ネステロフ：運動量で加速する勾配法（約45秒）"""

    def construct(self):
        self.show_heading("ネステロフ加速")
        self.draw_path()
        self.momentum()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[0, 2.2, 1], x_length=6.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25)
        curve = axes.plot(lambda x: 0.35 * x * x + 0.35, x_range=[-1.8, 1.8], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(curve), run_time=1.3)
        note = self.ja_text("目的関数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def momentum(self):
        xs = [1.6, 0.9, 0.2, -0.15, 0.05]
        dots = VGroup(*[Dot(self.axes.c2p(x, 0.35 * x * x + 0.35), color=ORANGE, radius=0.09) for x in xs])
        path = VMobject(color=ORANGE, stroke_width=3)
        path.set_points_as_corners([d.get_center() for d in dots])
        cap = self.ja_text("先読みして進む", font_size=24).move_to(self.note)
        self.play(Create(path), FadeIn(dots), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("加速収束", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"y_k=x_k+\beta(x_k-x_{k-1})").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
