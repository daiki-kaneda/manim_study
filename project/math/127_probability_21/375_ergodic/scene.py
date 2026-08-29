from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ErgodicTheorem(PacedScene):
    """#375 エルゴード：時間平均＝空間平均（約45秒）"""

    def construct(self):
        self.show_heading("エルゴード定理")
        self.draw_path()
        self.averages()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        self.axes = Axes(x_range=[0, 6.2, 1], y_range=[0, 2.2, 1], x_length=7.0, y_length=2.6,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.45 + LEFT * 0.15)
        ys = [0.6, 1.2, 0.9, 1.5, 1.1, 1.4, 1.25]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(ys)])
        self.play(Create(self.axes), Create(path), run_time=1.5)
        note = self.ja_text("時間軌道", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def averages(self):
        mean_y = 1.2
        tline = DashedLine(self.axes.c2p(0, mean_y), self.axes.c2p(6, mean_y), color=ORANGE, stroke_width=3)
        cap = self.ja_text("時間平均", font_size=24).move_to(self.note)
        self.play(Create(tline), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("空間平均と一致", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\frac1n\sum_{k=0}^{n-1}f(T^kx)\to\int f\,d\mu").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
