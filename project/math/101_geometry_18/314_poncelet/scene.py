from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Poncelet(PacedScene):
    """#314 ポンセレ：2 円に接する多角形が閉じる（約45秒）"""

    def construct(self):
        self.show_heading("ポンセレの定理")
        self.draw_circles()
        self.polygon()
        self.show_formula()
        self.read(1.4)

    def draw_circles(self):
        self.O = ORIGIN + DOWN * 0.1
        self.outer = Circle(radius=2.3, color=GREY, stroke_width=3).move_to(self.O)
        self.inner = Circle(radius=1.0, color=TEAL, stroke_width=3).move_to(self.O + LEFT * 0.15)
        self.play(Create(self.outer), Create(self.inner), run_time=1.3)
        note = self.ja_text("2 つの円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def polygon(self):
        angs = [0.2, 1.3, 2.4, 3.6, 4.8]
        pts = [self.O + 2.3 * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        poly = Polygon(*pts, color=ORANGE, stroke_width=3)
        cap = self.ja_text("外接・内接", font_size=24).move_to(self.note)
        self.play(Create(poly), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("閉じれば全部", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(poly, color=YELLOW), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("一つ閉じれば全て閉じる", font_size=30)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
