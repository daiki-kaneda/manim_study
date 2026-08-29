from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class CyclicDiagonals(PacedScene):
    """#446 円内接四角形：対角の和は 180°（約45秒）"""

    def construct(self):
        self.show_heading("円内接の対角")
        self.draw_cyclic()
        self.angles()
        self.show_formula()
        self.read(1.4)

    def draw_cyclic(self):
        import numpy as np
        self.O = ORIGIN + DOWN * 0.05
        self.circ = Circle(radius=2.2, color=GREY, stroke_width=2).move_to(self.O)
        angs = [0.4, 1.6, 3.3, 5.1]
        self.verts = [self.O + 2.2 * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        self.quad = Polygon(*self.verts, color=BLUE, stroke_width=3)
        self.play(Create(self.circ), Create(self.quad), run_time=1.4)
        note = self.ja_text("円に内接", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def angles(self):
        a1 = Angle(Line(self.verts[0], self.verts[1]), Line(self.verts[0], self.verts[3]), radius=0.4, color=ORANGE)
        a2 = Angle(Line(self.verts[2], self.verts[1]), Line(self.verts[2], self.verts[3]), radius=0.4, color=TEAL)
        cap = self.ja_text("対角", font_size=24).move_to(self.note)
        self.play(Create(a1), Create(a2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("和は 180°", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A+C=B+D=180^\circ").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
