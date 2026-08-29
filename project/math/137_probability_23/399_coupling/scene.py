from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Coupling(PacedScene):
    """#399 結合法：同じ乱数で 2 過程を並べる（約45秒）"""

    def construct(self):
        self.show_heading("結合法")
        self.draw_paths()
        self.meet()
        self.show_formula()
        self.read(1.4)

    def draw_paths(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[0, 2.5, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35 + LEFT * 0.2)
        y1 = [0.4, 0.9, 1.3, 1.6, 1.8, 2.0, 2.05]
        y2 = [2.1, 1.7, 1.5, 1.7, 1.85, 2.0, 2.05]
        p1 = VMobject(color=BLUE, stroke_width=4)
        p1.set_points_as_corners([axes.c2p(i, y) for i, y in enumerate(y1)])
        p2 = VMobject(color=ORANGE, stroke_width=4)
        p2.set_points_as_corners([axes.c2p(i, y) for i, y in enumerate(y2)])
        self.play(Create(axes), Create(p1), Create(p2), run_time=1.6)
        note = self.ja_text("2 つの過程", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes
        self.meet_pt = axes.c2p(5, 2.0)

    def meet(self):
        meet = Dot(self.meet_pt, color=RED, radius=0.12)
        cap = self.ja_text("いつか出会う", font_size=24).move_to(self.note)
        self.play(FadeIn(meet, scale=0.5), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("法則が近づく", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|P_n-Q_n\|_{\mathrm{TV}}\le\mathbb{P}(X_n\neq Y_n)").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
