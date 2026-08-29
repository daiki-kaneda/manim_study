from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FeynmanKac(PacedScene):
    """#351 ファインマン・カッツ：期待値で PDE を解く（約45秒）"""

    def construct(self):
        self.show_heading("ファインマン・カッツ")
        self.draw_paths()
        self.expect()
        self.show_formula()
        self.read(1.4)

    def draw_paths(self):
        self.axes = Axes(x_range=[0, 5.2, 1], y_range=[-1.5, 2.5, 1], x_length=7.0, y_length=3.0,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.25 + LEFT * 0.15)
        paths = []
        series = [
            [0, 0.4, 0.2, 0.8, 1.1, 0.9],
            [0, -0.3, 0.1, -0.2, 0.5, 0.7],
            [0, 0.6, 1.0, 0.7, 0.3, 0.5],
        ]
        cols = [BLUE, TEAL, GREY]
        for ys, col in zip(series, cols):
            p = VMobject(color=col, stroke_width=3)
            p.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(ys)])
            paths.append(p)
        self.play(Create(self.axes), run_time=0.7)
        self.play(LaggedStart(*[Create(p) for p in paths], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("拡散の道", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def expect(self):
        brace = MathTex(r"\mathbb{E}", color=ORANGE, font_size=48).shift(RIGHT * 2.6 + DOWN * 0.2)
        cap = self.ja_text("期待値で書く", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.2)
        self.read(0.3)
        cap2 = self.ja_text("PDE と対応", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"u(t,x)=\mathbb{E}[f(X_T)\mid X_t=x]").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
