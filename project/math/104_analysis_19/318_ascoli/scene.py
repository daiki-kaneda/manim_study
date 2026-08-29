from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AscoliArzela(PacedScene):
    """#318 アスコリ・アルツェラ：同程度連続＋有界なら相対コンパクト（約45秒）"""

    def construct(self):
        self.show_heading("アスコリ・アルツェラ")
        self.draw_family()
        self.equicont()
        self.show_formula()
        self.read(1.4)

    def draw_family(self):
        self.axes = Axes(x_range=[0, 4, 1], y_range=[0, 2.4, 1], x_length=6.2, y_length=2.8,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.2)
        import math
        curves = VGroup(*[
            self.axes.plot(lambda x, a=a: 1.0 + a * math.sin(2 * x + a), x_range=[0.2, 3.8], color=c, stroke_width=3)
            for a, c in [(0.4, BLUE), (0.25, TEAL), (0.35, GREY), (0.2, BLUE)]
        ])
        self.play(Create(self.axes), run_time=0.7)
        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("関数族", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def equicont(self):
        # small window showing similar slopes
        box = SurroundingRectangle(Dot(self.axes.c2p(2.0, 1.0)), color=ORANGE, buff=0.55)
        cap = self.ja_text("同程度連続", font_size=24).move_to(self.note)
        self.play(Create(box), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("収束部分列", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("相対コンパクト", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
