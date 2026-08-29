from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SpringerNumbers(PacedScene):
    """#713 スプリンガー数：型Bの交替順列を数える（約45秒）"""

    def construct(self):
        self.show_heading("スプリンガー数")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        vals = VGroup(*[
            MathTex(str(v), font_size=32).shift(LEFT * 2.4 + RIGHT * i * 1.2 + UP * 0.3)
            for i, v in enumerate([1, 1, 5, 61, 1385])
        ])
        self.play(LaggedStart(*[FadeIn(v) for v in vals], lag_ratio=0.1), run_time=1.3)

        note = self.ja_text("型Bの交替", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("符号付き順列", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("生成関数あり", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\sum S_n\frac{x^n}{n!}=\frac{1}{\cos x-\sin x}").scale(0.6)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
