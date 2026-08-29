from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ModelSoup(PacedScene):
    """#695 モデルスープ：複数重みを混ぜて汎化（約45秒）"""

    def construct(self):
        self.show_heading("モデルスープ")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        bowls = VGroup(*[
            Circle(radius=0.55, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT*2.2+UP*0.3), (ORANGE, ORIGIN+UP*0.3), (TEAL, RIGHT*2.2+UP*0.3)]
        ])
        mix = Circle(radius=0.8, color=YELLOW, stroke_width=4).shift(DOWN*1.1)
        self.play(LaggedStart(*[Create(b) for b in bowls], lag_ratio=0.1), Create(mix), run_time=1.4)

        note = self.ja_text("複数モデル", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("重み空間で平均", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("安価なアンサンブル", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\theta=\sum_i \alpha_i\theta_i").scale(0.8)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
