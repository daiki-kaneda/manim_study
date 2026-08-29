from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HeavyBall(PacedScene):
    """#645 ヘビーボール：慣性付き勾配法（約45秒）"""

    def construct(self):
        self.show_heading("ヘビーボール")
        self.draw_path()
        self.inertia()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[-0.5, 4, 1], y_range=[0, 2, 1], x_length=5.5, y_length=2.3,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.2 + UP * 0.15)
        pts = [axes.c2p(0.2, 1.7), axes.c2p(1.0, 1.1), axes.c2p(1.8, 0.9), axes.c2p(2.6, 0.45), axes.c2p(3.4, 0.25)]
        path = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(pts)
        self.play(Create(axes), Create(path), FadeIn(VGroup(*[Dot(p, radius=0.07, color=YELLOW) for p in pts])), run_time=1.4)
        note = self.ja_text("慣性で加速", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def inertia(self):
        cap = self.ja_text("前ステップを混ぜる", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("Polyak運動量", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x_{k+1}=x_k-\alpha\nabla f_k+\beta(x_k-x_{k-1})").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
