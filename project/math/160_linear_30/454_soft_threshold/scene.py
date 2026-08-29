from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class SoftThreshold(PacedScene):
    """#454 ソフト閾値：小さい係数を縮める（約45秒）"""

    def construct(self):
        self.show_heading("ソフト閾値")
        self.draw_line()
        self.shrink()
        self.show_formula()
        self.read(1.4)

    def draw_line(self):
        axes = Axes(x_range=[-2.5, 2.5, 1], y_range=[-2.0, 2.0, 1], x_length=6.0, y_length=3.2,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.1)
        identity = axes.plot(lambda x: x, x_range=[-2.2, 2.2], color=GREY, stroke_width=2)
        self.play(Create(axes), Create(identity), run_time=1.2)
        note = self.ja_text("恒等写像", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def shrink(self):
        # soft threshold piecewise
        left = self.axes.plot(lambda x: x + 0.6, x_range=[-2.2, -0.6], color=ORANGE, stroke_width=4)
        mid = DashedLine(self.axes.c2p(-0.6, 0), self.axes.c2p(0.6, 0), color=ORANGE, stroke_width=4)
        right = self.axes.plot(lambda x: x - 0.6, x_range=[0.6, 2.2], color=ORANGE, stroke_width=4)
        cap = self.ja_text("中央を 0 に", font_size=24).move_to(self.note)
        self.play(Create(left), Create(mid), Create(right), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("疎へ誘導", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"S_\lambda(x)=\mathrm{sign}(x)(|x|-\lambda)_+").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
