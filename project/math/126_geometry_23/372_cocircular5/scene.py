from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class CocircularFive(PacedScene):
    """#372 共円五点：5 点が同一円上（約45秒）"""

    def construct(self):
        self.show_heading("共円五点")
        self.draw_circle()
        self.points()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        self.O = ORIGIN + DOWN * 0.1
        self.circ = Circle(radius=2.2, color=GREY, stroke_width=3).move_to(self.O)
        self.play(Create(self.circ), run_time=1.2)
        note = self.ja_text("一つの円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def points(self):
        angs = [0.2, 1.3, 2.5, 3.8, 5.2]
        pts = [self.O + 2.2 * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        dots = VGroup(*[Dot(p, color=ORANGE, radius=0.1) for p in pts])
        poly = Polygon(*pts, color=BLUE, stroke_width=2)
        cap = self.ja_text("5 点を置く", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.play(Create(poly), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("すべて共円", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(self.circ, color=YELLOW), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("5 点が同一円上", font_size=30)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
