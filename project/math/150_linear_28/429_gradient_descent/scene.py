from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class GradientDescent(PacedScene):
    """#429 勾配降下：負勾配方向に進む（約45秒）"""

    def construct(self):
        self.show_heading("勾配降下")
        self.draw_surface()
        self.steps()
        self.show_formula()
        self.read(1.4)

    def draw_surface(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[0, 2.2, 1], x_length=6.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25)
        curve = axes.plot(lambda x: 0.35 * x * x + 0.4, x_range=[-1.8, 1.8], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(curve), run_time=1.3)
        note = self.ja_text("目的関数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def steps(self):
        xs = [1.5, 1.0, 0.55, 0.25, 0.08]
        dots = VGroup(*[Dot(self.axes.c2p(x, 0.35 * x * x + 0.4), color=ORANGE, radius=0.09) for x in xs])
        path = VMobject(color=ORANGE, stroke_width=3)
        path.set_points_as_corners([d.get_center() for d in dots])
        cap = self.ja_text("勾配と逆向き", font_size=24).move_to(self.note)
        self.play(Create(path), FadeIn(dots), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("最小へ近づく", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x_{k+1}=x_k-\eta\nabla f(x_k)").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
