from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Antisimilarity(PacedScene):
    """#373 反相似：向きを反転する相似（約45秒）"""

    def construct(self):
        self.show_heading("反相似")
        self.draw_pair()
        self.flip()
        self.show_formula()
        self.read(1.4)

    def draw_pair(self):
        self.t1 = Polygon(LEFT * 3.0 + UP * 0.8, LEFT * 1.5 + UP * 1.6, LEFT * 1.2 + DOWN * 0.2, color=BLUE, stroke_width=3)
        self.play(Create(self.t1), run_time=1.2)
        note = self.ja_text("図形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def flip(self):
        # mirrored & scaled copy
        t2 = Polygon(RIGHT * 1.0 + UP * 0.5, RIGHT * 2.8 + DOWN * 0.3, RIGHT * 2.2 + UP * 1.5, color=ORANGE, stroke_width=3)
        arrow = Arrow(ORIGIN + LEFT * 0.3, ORIGIN + RIGHT * 0.5, buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("向きを反転", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.1)
        self.play(Create(t2), run_time=1.1)
        self.read(0.25)
        # mark orientation with small arcs
        a1 = Arc(radius=0.35, start_angle=0.2, angle=1.2, color=TEAL).move_arc_center_to(LEFT * 2.0 + UP * 0.6)
        a2 = Arc(radius=0.35, start_angle=2.0, angle=-1.2, color=TEAL).move_arc_center_to(RIGHT * 2.0 + UP * 0.5)
        cap2 = self.ja_text("相似＋鏡映", font_size=24).move_to(self.note)
        self.play(Create(a1), Create(a2), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("向きを逆にする相似", font_size=30)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
