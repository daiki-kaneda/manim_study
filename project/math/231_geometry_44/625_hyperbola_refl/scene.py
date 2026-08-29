from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
import numpy as np
from manim_math import PacedScene


class HyperbolaReflection(PacedScene):
    """#625 双曲線の反射：一方の焦点差が一定な反射法則（約45秒）"""

    def construct(self):
        self.show_heading("双曲線の反射")
        self.draw_hyp()
        self.rays()
        self.show_formula()
        self.read(1.4)

    def draw_hyp(self):
        # two branches as parametric
        left_pts = [np.array([-1.2 - 0.35 * (t ** 2), t, 0]) for t in [-1.6 + i * 0.1 for i in range(33)]]
        right_pts = [np.array([1.2 + 0.35 * (t ** 2), t, 0]) for t in [-1.6 + i * 0.1 for i in range(33)]]
        left = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(left_pts).shift(UP * 0.1)
        right = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(right_pts).shift(UP * 0.1)
        f1 = Dot(LEFT * 1.8 + UP * 0.1, color=YELLOW, radius=0.1)
        f2 = Dot(RIGHT * 1.8 + UP * 0.1, color=YELLOW, radius=0.1)
        self.play(Create(left), Create(right), FadeIn(f1), FadeIn(f2), run_time=1.4)
        note = self.ja_text("二焦点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.f1, self.f2, self.right = f1, f2, right

    def rays(self):
        hit = self.right.get_points()[20]
        incoming = Arrow(LEFT * 3.5 + UP * 1.2, hit, buff=0.02, color=ORANGE, stroke_width=3)
        to_f = Arrow(hit, self.f2.get_center(), buff=0.05, color=TEAL, stroke_width=3)
        other = DashedLine(hit, self.f1.get_center(), color=GREY, stroke_width=2)
        cap = self.ja_text("外向き反射", font_size=24).move_to(self.note)
        self.play(GrowArrow(incoming), GrowArrow(to_f), Create(other), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("焦点差が一定", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"||PF_1|-|PF_2||=2a").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
