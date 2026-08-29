from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MartingaleConvergence(PacedScene):
    """#376 マルチンゲール収束：有界なら収束する（約45秒）"""

    def construct(self):
        self.show_heading("マルチンゲール収束")
        self.draw_paths()
        self.converge()
        self.show_formula()
        self.read(1.4)

    def draw_paths(self):
        self.axes = Axes(x_range=[0, 6.2, 1], y_range=[-1.5, 2.5, 1], x_length=7.0, y_length=3.0,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.2 + LEFT * 0.15)
        series = [
            [0, 0.5, 0.2, 0.8, 0.6, 1.0, 0.9],
            [0, -0.3, 0.1, -0.2, 0.4, 0.3, 0.5],
            [0, 0.8, 1.2, 0.7, 1.1, 1.3, 1.25],
        ]
        cols = [BLUE, TEAL, GREY]
        self.paths = VGroup()
        for ys, col in zip(series, cols):
            p = VMobject(color=col, stroke_width=3)
            p.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(ys)])
            self.paths.add(p)
        self.play(Create(self.axes), run_time=0.7)
        self.play(LaggedStart(*[Create(p) for p in self.paths], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("公正な賭け", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def converge(self):
        # asymptotic levels
        levels = VGroup(*[
            DashedLine(self.axes.c2p(4.5, y), self.axes.c2p(6, y), color=ORANGE, stroke_width=3)
            for y in [0.9, 0.5, 1.25]
        ])
        cap = self.ja_text("やがて落ち着く", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in levels], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("ほぼ確実に収束", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\sup_n\mathbb{E}|M_n|<\infty\Rightarrow M_n\to M_\infty").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
