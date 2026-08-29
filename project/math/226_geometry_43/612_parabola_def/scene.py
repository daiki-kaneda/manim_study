from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ParabolaDefinition(PacedScene):
    """#612 放物線の定義：焦点と準線から等距離（約45秒）"""

    def construct(self):
        self.show_heading("放物線の定義")
        self.draw_focus_directrix()
        self.equal()
        self.show_formula()
        self.read(1.4)

    def draw_focus_directrix(self):
        axes = Axes(x_range=[-0.5, 3, 1], y_range=[-2, 2, 1], x_length=4.5, y_length=3.2,
                    tips=False, axis_config={"stroke_width": 1, "include_ticks": False}).shift(LEFT * 0.8 + UP * 0.1)
        focus = Dot(axes.c2p(0.8, 0), color=YELLOW, radius=0.1)
        dline = Line(axes.c2p(-0.3, -1.8), axes.c2p(-0.3, 1.8), color=ORANGE, stroke_width=3)
        pts = [axes.c2p(0.5 * (t ** 2) / 0.8, t) for t in [-1.7 + i * 0.1 for i in range(35)]]
        para = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(pts)
        self.play(Create(axes), Create(dline), FadeIn(focus), Create(para), run_time=1.5)
        note = self.ja_text("焦点と準線", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.focus = focus
        self.dline = dline
        self.axes = axes

    def equal(self):
        P = Dot(self.axes.c2p(0.5 * 1.0 / 0.8, 1.0), color=TEAL, radius=0.08)
        to_f = DashedLine(P.get_center(), self.focus.get_center(), color=TEAL, stroke_width=2)
        foot = Dot(self.axes.c2p(-0.3, 1.0), color=ORANGE, radius=0.06)
        to_d = DashedLine(P.get_center(), foot.get_center(), color=ORANGE, stroke_width=2)
        cap = self.ja_text("距離が等しい", font_size=24).move_to(self.note)
        self.play(FadeIn(P), Create(to_f), Create(to_d), FadeIn(foot), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("e=1 の軌跡", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"|PF|=\mathrm{dist}(P,\ell)").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
