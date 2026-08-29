from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class KLDivergence(PacedScene):
    """#292 KL：分布の距離としての相対エントロピー（約45秒）"""

    def construct(self):
        self.show_heading("KL ダイバージェンス")
        self.draw_dists()
        self.compare()
        self.show_formula()
        self.read(1.4)

    def draw_dists(self):
        self.axes = Axes(
            x_range=[-0.2, 5.2, 1],
            y_range=[0, 1.2, 1],
            x_length=7.2,
            y_length=2.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.5 + LEFT * 0.2)
        import math
        p = self.axes.plot(lambda x: 0.95 * math.exp(-3.2 * (x - 1.8) ** 2), x_range=[0.3, 4.5], color=BLUE, stroke_width=4)
        q = self.axes.plot(lambda x: 0.85 * math.exp(-2.2 * (x - 3.0) ** 2), x_range=[0.5, 4.8], color=TEAL, stroke_width=4)
        self.play(Create(self.axes), run_time=0.7)
        self.play(Create(p), Create(q), run_time=1.4)
        note = self.ja_text("2 つの分布", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare(self):
        # gap markers
        gap = DoubleArrow(
            self.axes.c2p(1.8, 1.05),
            self.axes.c2p(3.0, 1.05),
            buff=0.05,
            color=ORANGE,
            stroke_width=4,
        )
        cap = self.ja_text("ずれを測る", font_size=24).move_to(self.note)
        self.play(Create(gap), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("情報の差", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.9)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"D_{\mathrm{KL}}(P\|Q)=\sum p\log\frac{p}{q}").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
