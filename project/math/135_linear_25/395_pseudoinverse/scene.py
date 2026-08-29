from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Pseudoinverse(PacedScene):
    """#395 擬逆：最小二乗の解 A^+b（約45秒）"""

    def construct(self):
        self.show_heading("擬逆行列")
        self.draw_system()
        self.least_squares()
        self.show_formula()
        self.read(1.4)

    def draw_system(self):
        axes = Axes(x_range=[-0.5, 3.5, 1], y_range=[-0.5, 2.5, 1], x_length=5.5, y_length=3.0,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.15)
        # overdetermined: points not on one line
        pts = [(0.5, 0.4), (1.2, 1.1), (2.0, 1.3), (2.8, 2.0)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=BLUE, radius=0.09) for x, y in pts])
        self.play(Create(axes), FadeIn(dots), run_time=1.3)
        note = self.ja_text("過剰決定", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes
        self.dots = dots

    def least_squares(self):
        line = self.axes.plot(lambda x: 0.55 * x + 0.25, x_range=[0.2, 3.2], color=ORANGE, stroke_width=4)
        # residuals
        res = VGroup(*[
            DashedLine(self.axes.c2p(x, y), self.axes.c2p(x, 0.55 * x + 0.25), color=TEAL, stroke_width=2)
            for x, y in [(0.5, 0.4), (1.2, 1.1), (2.0, 1.3), (2.8, 2.0)]
        ])
        cap = self.ja_text("最小二乗", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.2)
        self.play(LaggedStart(*[Create(r) for r in res], lag_ratio=0.1), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("擬逆で解く", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x=A^{+}b,\quad A^{+}=(A^{*}A)^{-1}A^{*}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
