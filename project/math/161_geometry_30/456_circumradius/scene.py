from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class Circumradius(PacedScene):
    """#456 外接円半径：R=abc/4S（約45秒）"""

    def construct(self):
        self.show_heading("外接円半径")
        self.draw_triangle()
        self.circle()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.5 + DOWN * 1.4
        self.C = RIGHT * 2.6 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def circle(self):
        O = (self.A + self.B + self.C) / 3 + DOWN * 0.15
        import numpy as np
        R = float(np.linalg.norm(self.A - O)) * 1.05
        circ = Circle(radius=R, color=ORANGE, stroke_width=3).move_to(O)
        cap = self.ja_text("外接円", font_size=24).move_to(self.note)
        self.play(Create(circ), FadeIn(Dot(O, color=RED, radius=0.09)), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("辺と面積で", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"R=\frac{abc}{4S}").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
