from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class IntegrationByParts(PacedScene):
    """#198 部分積分は積の微分の逆（約45秒）"""

    def construct(self):
        self.show_heading("部分積分")
        self.draw_product()
        self.trade_areas()
        self.show_formula()
        self.read(1.4)

    def draw_product(self):
        self.axes = Axes(
            x_range=[-0.2, 3.4, 1],
            y_range=[-0.2, 2.4, 1],
            x_length=7.6,
            y_length=3.15,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.3)
        self.u = self.axes.plot(lambda x: 0.35 * x + 0.4, x_range=[0.1, 3.1], color=BLUE, stroke_width=4)
        self.v = self.axes.plot(lambda x: 1.8 - 0.25 * x, x_range=[0.1, 3.1], color=YELLOW, stroke_width=4)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.u), Create(self.v), run_time=1.5)
        ul = MathTex("u", color=BLUE, font_size=28).next_to(self.u, UP, buff=0.08).shift(RIGHT * 1.2)
        vl = MathTex("v", color=YELLOW, font_size=28).next_to(self.v, UP, buff=0.08).shift(LEFT * 0.8)
        self.play(FadeIn(ul), FadeIn(vl), run_time=0.5)
        note = self.ja_text("積", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def trade_areas(self):
        a, b = 0.6, 2.6
        area_uv = self.axes.get_area(
            self.axes.plot(lambda x: (0.35 * x + 0.4) * (1.8 - 0.25 * x) / 1.4, x_range=[a, b], color=TEAL),
            x_range=[a, b],
            color=TEAL,
            opacity=0.45,
        )
        # simpler: show uv at endpoints as braces conceptually via verticals
        la = DashedLine(self.axes.c2p(a, 0), self.axes.c2p(a, 2.0), color=GREY_B, stroke_width=2)
        lb = DashedLine(self.axes.c2p(b, 0), self.axes.c2p(b, 2.0), color=GREY_B, stroke_width=2)
        self.play(Create(la), Create(lb), run_time=0.9)
        cap = self.ja_text("端の積", font_size=24).move_to(self.note)
        self.play(FadeIn(area_uv), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("差し引き", font_size=24).move_to(self.note)
        arrow = Arrow(LEFT * 0.2 + UP * 0.8, RIGHT * 1.2 + DOWN * 0.2, color=ORANGE, stroke_width=4, buff=0).shift(RIGHT * 2.2)
        self.play(GrowArrow(arrow), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\int u\,dv=uv-\int v\,du").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
