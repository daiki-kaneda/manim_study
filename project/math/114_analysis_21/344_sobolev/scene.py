from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SobolevInequality(PacedScene):
    """#344 ソボレフ：勾配で関数を押さえる（約45秒）"""

    def construct(self):
        self.show_heading("ソボレフの不等式")
        self.draw_bump()
        self.control()
        self.show_formula()
        self.read(1.4)

    def draw_bump(self):
        self.axes = Axes(x_range=[-0.2, 4.2, 1], y_range=[0, 2.2, 1], x_length=6.5, y_length=2.7,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.25)
        import math
        bump = self.axes.plot(lambda x: 1.6 * math.exp(-3.5 * (x - 2.0) ** 2), x_range=[0.3, 3.7], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(bump), run_time=1.4)
        note = self.ja_text("関数 u", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def control(self):
        # slope markers
        slopes = VGroup(
            Line(self.axes.c2p(1.3, 0.3), self.axes.c2p(1.7, 1.1), color=ORANGE, stroke_width=4),
            Line(self.axes.c2p(2.3, 1.1), self.axes.c2p(2.7, 0.3), color=ORANGE, stroke_width=4),
        )
        cap = self.ja_text("勾配を見る", font_size=24).move_to(self.note)
        self.play(Create(slopes[0]), Create(slopes[1]), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("ノルムで抑える", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\|u\|_{p^{*}}\le C\|\nabla u\|_p").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
