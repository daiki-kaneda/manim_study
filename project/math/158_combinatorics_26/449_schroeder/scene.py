from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Schroeder(PacedScene):
    """#449 シュレーダー数：対角可のカタラン拡張（約45秒）"""

    def construct(self):
        self.show_heading("シュレーダー数")
        self.draw_path()
        self.steps()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[-0.2, 2.5, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35)
        pts = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 1), (5, 0), (6, 0)]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([axes.c2p(x, y) for x, y in pts])
        dots = VGroup(*[Dot(axes.c2p(x, y), color=ORANGE, radius=0.08) for x, y in pts])
        self.play(Create(axes), Create(path), FadeIn(dots), run_time=1.5)
        note = self.ja_text("斜めも許す", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def steps(self):
        steps = VGroup(
            MathTex(r"\nearrow", color=TEAL, font_size=34),
            MathTex(r"\rightarrow", color=YELLOW, font_size=34),
            MathTex(r"\searrow", color=ORANGE, font_size=34),
        ).arrange(RIGHT, buff=0.4).shift(DOWN * 0.85)
        cap = self.ja_text("3 種の歩み", font_size=24).move_to(self.note)
        self.play(FadeIn(steps), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("大シュレーダー", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"S_n=S_{n-1}+\sum_{k=0}^{n-2}S_k S_{n-2-k}").scale(0.78)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
