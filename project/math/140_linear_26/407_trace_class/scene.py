from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class TraceClass(PacedScene):
    """#407 トレースクラス：特異値の和が有限（約45秒）"""

    def construct(self):
        self.show_heading("トレースクラス")
        self.draw_sigmas()
        self.summable()
        self.show_formula()
        self.read(1.4)

    def draw_sigmas(self):
        axes = Axes(x_range=[0, 7, 1], y_range=[0, 1.4, 1], x_length=6.5, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.5)
        vals = [1.2, 0.7, 0.4, 0.22, 0.12, 0.06]
        dots = VGroup(*[Dot(axes.c2p(i + 1, v), color=ORANGE, radius=0.09) for i, v in enumerate(vals)])
        path = VMobject(color=ORANGE, stroke_width=3)
        path.set_points_as_corners([d.get_center() for d in dots])
        self.play(Create(axes), Create(path), FadeIn(dots), run_time=1.5)
        note = self.ja_text("特異値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def summable(self):
        brace = MathTex(r"\sum_i\sigma_i<\infty", font_size=36).shift(DOWN * 0.7)
        brace = MathTex(r"\sum_i\sigma_i<\infty", font_size=40).shift(DOWN * 0.75)
        cap = self.ja_text("和が有限", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("トレース定義可", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|T\|_1=\sum\sigma_i(T)<\infty").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
