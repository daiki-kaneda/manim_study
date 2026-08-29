from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CrandallLions(PacedScene):
    """#644 クランダル・ライオンズ：粘性解の基礎理論（約45秒）"""

    def construct(self):
        self.show_heading("クランダル・ライオンズ")
        self.draw_framework()
        self.results()
        self.show_formula()
        self.read(1.4)

    def draw_framework(self):
        boxes = VGroup(*[
            RoundedRectangle(width=2.2, height=1.1, corner_radius=0.1, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT * 2.5 + UP * 0.3), (ORANGE, ORIGIN + UP * 0.3), (TEAL, RIGHT * 2.5 + UP * 0.3)]
        ])
        labs = VGroup(
            MathTex(r"F=0", font_size=28).move_to(boxes[0]),
            MathTex(r"\mathrm{visc.}", font_size=26).move_to(boxes[1]),
            MathTex(r"\exists!", font_size=30).move_to(boxes[2]),
        )
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("粘性解理論", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def results(self):
        cap = self.ja_text("存在と一意", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("比較原理を使う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"u^\varepsilon\to u\ \mathrm{(viscosity)}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
