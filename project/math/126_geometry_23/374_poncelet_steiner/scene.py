from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class PonceletSteiner(PacedScene):
    """#374 ポンスレ・スタイナー：定規のみで作図できる範囲（約45秒）"""

    def construct(self):
        self.show_heading("ポンスレ・スタイナー")
        self.draw_given()
        self.ruler()
        self.show_formula()
        self.read(1.4)

    def draw_given(self):
        self.O = LEFT * 1.5 + DOWN * 0.2
        self.circ = Circle(radius=1.5, color=TEAL, stroke_width=3).move_to(self.O)
        center = Dot(self.O, color=YELLOW, radius=0.1)
        self.play(Create(self.circ), FadeIn(center), run_time=1.3)
        note = self.ja_text("円と中心", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ruler(self):
        # straightedge lines constructing a point
        lines = VGroup(
            Line(LEFT * 3.5 + UP * 1.5, RIGHT * 2.5 + DOWN * 1.8, color=BLUE, stroke_width=3),
            Line(LEFT * 3.2 + DOWN * 1.6, RIGHT * 2.8 + UP * 1.2, color=BLUE, stroke_width=3),
            Line(LEFT * 0.2 + UP * 2.0, RIGHT * 3.0 + UP * 0.2, color=ORANGE, stroke_width=3),
        )
        cap = self.ja_text("定規だけで", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.12), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        pt = Dot(RIGHT * 1.8 + DOWN * 0.3, color=RED, radius=0.11)
        cap2 = self.ja_text("作図できる", font_size=24).move_to(self.note)
        self.play(FadeIn(pt, scale=0.5), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("定規だけで作図可", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
