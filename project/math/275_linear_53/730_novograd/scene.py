from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class NovoGrad(PacedScene):
    """#730 NovoGrad：層ごとの2次ノルムで正規化（約45秒）"""

    def construct(self):
        self.show_heading("NovoGrad")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        layers = VGroup(*[
            RoundedRectangle(width=1.6, height=1.0, corner_radius=0.08, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT * 2.3 + UP * 0.3), (ORANGE, ORIGIN + UP * 0.3), (TEAL, RIGHT * 2.3 + UP * 0.3)]
        ])
        self.play(LaggedStart(*[Create(b) for b in layers], lag_ratio=0.1), run_time=1.3)

        note = self.ja_text("層ごと正規化", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("Adamより軽量", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("NLPでも有効", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"g\leftarrow g/\|g\|_2,\ v\leftarrow\beta v+(1-\beta)g^2").scale(0.58)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
