from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SeidelNumbers(PacedScene):
    """#689 セイデル数：交替順列を三角形で数える（約45秒）"""

    def construct(self):
        self.show_heading("セイデル数")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = VGroup(*[
            MathTex(str((i+j) % 7), font_size=26).shift(LEFT * 2.0 + RIGHT * j * 0.7 + UP * (1.0 - i * 0.55))
            for i in range(4) for j in range(i + 1)
        ])
        self.play(FadeIn(tri), run_time=1.3)

        note = self.ja_text("交替順列と同数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("三角形規則", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("エントリンガーと結ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"S_n=E_n").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
