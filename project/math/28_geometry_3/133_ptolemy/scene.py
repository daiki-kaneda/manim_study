from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Ptolemy(PacedScene):
    """#133 トレミーの定理（約45秒）"""

    def construct(self):
        self.show_heading("トレミーの定理")
        self.draw_cyclic()
        self.draw_diagonals()
        self.show_formula()
        self.read(1.4)

    def draw_cyclic(self):
        o = LEFT * 1.7 + DOWN * 0.15
        r = 2.05
        circ = Circle(radius=r, color=GREY, stroke_width=2).move_to(o)
        angs = [20, 115, 195, 310]
        self.pts = [o + np.array([r * np.cos(a * DEGREES), r * np.sin(a * DEGREES), 0]) for a in angs]
        quad = Polygon(*self.pts, color=WHITE, stroke_width=3)
        self.play(Create(circ), run_time=1.1)
        self.play(Create(quad), run_time=1.4)
        labs = VGroup(*[
            MathTex(name, font_size=28).next_to(p, d, buff=0.08)
            for name, p, d in zip("ABCD", self.pts, (UR, UL, DL, DR))
        ])
        self.play(FadeIn(labs), run_time=0.7)
        self.read(0.4)

    def draw_diagonals(self):
        ac = Line(self.pts[0], self.pts[2], color=YELLOW, stroke_width=4)
        bd = Line(self.pts[1], self.pts[3], color=ORANGE, stroke_width=4)
        self.play(Create(ac), run_time=0.9)
        self.play(Create(bd), run_time=0.9)
        note = self.ja_text("対角線の積", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.5)

    def show_formula(self):
        formula = MathTex(r"AB\cdot CD+AD\cdot BC=AC\cdot BD").scale(0.78)
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
