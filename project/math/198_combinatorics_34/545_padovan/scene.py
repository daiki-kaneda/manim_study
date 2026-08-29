from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Padovan(PacedScene):
    """#545 パッドヴァン：P_n=P_{n-2}+P_{n-3}（約45秒）"""

    def construct(self):
        self.show_heading("パッドヴァン")
        self.draw_seq()
        self.recurrence()
        self.show_formula()
        self.read(1.4)

    def draw_seq(self):
        vals = ["1", "1", "1", "2", "2", "3", "4", "5", "7"]
        cells = VGroup(*[MathTex(v, font_size=32).shift(LEFT * 3.4 + RIGHT * i * 0.8 + UP * 0.6) for i, v in enumerate(vals)])
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.05), run_time=1.4)
        note = self.ja_text("数列", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def recurrence(self):
        cap = self.ja_text("2つ前＋3つ前", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("プラスチック数へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"P_n=P_{n-2}+P_{n-3}").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
