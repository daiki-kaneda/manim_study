from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Tribonacci(PacedScene):
    """#533 トリボナッチ：三つ前の和（約45秒）"""

    def construct(self):
        self.show_heading("トリボナッチ")
        self.draw_seq()
        self.recurrence()
        self.show_formula()
        self.read(1.4)

    def draw_seq(self):
        vals = ["0", "0", "1", "1", "2", "4", "7", "13"]
        cells = VGroup(*[MathTex(v, font_size=34).shift(LEFT * 3.3 + RIGHT * i * 0.9 + UP * 0.6) for i, v in enumerate(vals)])
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.06), run_time=1.4)
        note = self.ja_text("数列", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def recurrence(self):
        cap = self.ja_text("3 項の和", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("フィボの拡張", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"T_n=T_{n-1}+T_{n-2}+T_{n-3}").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
