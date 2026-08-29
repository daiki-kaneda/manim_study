from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class LawOfLargeNumbers(JapaneseScene):
    """#39 大数の法則（約90秒）"""

    def construct(self):
        self.show_heading("大数の法則")
        self.draw_axes()
        self.grow_average()
        self.show_formula()
        self.hold(1.2)

    def draw_axes(self):
        self.axes = Axes(
            x_range=[0, 22, 5],
            y_range=[0, 1.15, 0.5],
            x_length=8.4,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        half = DashedLine(
            self.axes.c2p(0, 0.5),
            self.axes.c2p(22, 0.5),
            color=YELLOW,
            stroke_width=2,
        )
        half_lab = MathTex(r"1/2", color=YELLOW, font_size=28).next_to(half, LEFT, buff=0.12)
        self.play(Create(self.axes), run_time=0.55)
        self.play(Create(half), FadeIn(half_lab), run_time=0.45)
        note = self.ja_text("コインの表の割合", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.4)
        self.note = note

    def grow_average(self):
        # 決定的な系列：序盤は振れ、後半 1/2 へ
        flips = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]
        pts = []
        heads = 0
        dots = VGroup()
        for n, f in enumerate(flips, start=1):
            heads += f
            y = heads / n
            pts.append(self.axes.c2p(n, y))
            dots.add(Dot(pts[-1], radius=0.045, color=BLUE))
        path = VMobject(color=BLUE, stroke_width=3)
        path.set_points_as_corners(pts)
        self.play(Create(path), FadeIn(dots), run_time=2.2)
        cap = self.ja_text("回数を増やすと 1/2 へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"\bar X_n \to E[X]").scale(1.15)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
