from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class LawOfSines(PacedScene):
    """#422 正弦法則：a/sin A は一定（約45秒）"""

    def construct(self):
        self.show_heading("正弦法則")
        self.draw_triangle()
        self.ratios()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.15
        self.B = LEFT * 2.6 + DOWN * 1.45
        self.C = RIGHT * 2.7 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ratios(self):
        labs = VGroup(
            MathTex("a", font_size=32).next_to(Line(self.B, self.C), DOWN, buff=0.15),
            MathTex("A", font_size=32).next_to(self.A, UP, buff=0.12),
        )
        circ = Circle(radius=2.4, color=GREY, stroke_width=2).move_to((self.A + self.B + self.C) / 3 + DOWN * 0.1)
        # circumcircle schematic
        O = (self.A + self.B + self.C) / 3
        circ = Circle(radius=np.linalg.norm(self.A - O) * 0.95, color=GREY, stroke_width=2).move_to(O)
        cap = self.ja_text("辺と対角", font_size=24).move_to(self.note)
        self.play(FadeIn(labs), Create(circ), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("比は直径", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\frac{a}{\sin A}=2R").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
