from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BennettInequality(PacedScene):
    """#327 ベネット：分散も使う集中不等式（約45秒）"""

    def construct(self):
        self.show_heading("ベネットの不等式")
        self.draw_tail()
        self.compare()
        self.show_formula()
        self.read(1.4)

    def draw_tail(self):
        self.axes = Axes(x_range=[-0.2, 5, 1], y_range=[0, 1.2, 1], x_length=7.0, y_length=2.5,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.45 + LEFT * 0.2)
        import math
        dens = self.axes.plot(lambda x: 0.9 * math.exp(-2.5 * (x - 2.2) ** 2), x_range=[0.2, 4.5], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(dens), run_time=1.4)
        note = self.ja_text("有界な和", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare(self):
        line = DashedLine(self.axes.c2p(3.4, 0), self.axes.c2p(3.4, 1.05), color=ORANGE, stroke_width=3)
        cap = self.ja_text("尾確率", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        better = MathTex(r"h(u)", color=YELLOW, font_size=36).shift(RIGHT * 2.8 + UP * 0.9)
        cap2 = self.ja_text("分散で改良", font_size=24).move_to(self.note)
        self.play(FadeIn(better), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"P(S-\mathbb{E}S\ge t)\le\exp(-\frac{\sigma^{2}}{M^{2}}h(\tfrac{Mt}{\sigma^{2}}))").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
