from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EntringerNumbers(PacedScene):
    """#677 エントリンガー数：交替順列を端点で細分（約45秒）"""

    def construct(self):
        self.show_heading("エントリンガー数")
        self.draw()
        self.refine()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        grid = VGroup(*[
            RoundedRectangle(width=0.85, height=0.7, corner_radius=0.06, color=BLUE, stroke_width=2).shift(LEFT * 2.2 + RIGHT * i * 1.0 + UP * (0.6 - j * 0.9))
            for j in range(2) for i in range(5)
        ])
        self.play(LaggedStart(*[Create(g) for g in grid], lag_ratio=0.03), run_time=1.3)
        note = self.ja_text("三角形配列", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def refine(self):
        cap = self.ja_text("端の値が最大", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("E_n の細分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"E_{n,k}=E_{n,k-1}+E_{n-1,n-k}").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
