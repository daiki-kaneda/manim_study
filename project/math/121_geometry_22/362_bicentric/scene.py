from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class BicentricQuad(PacedScene):
    """#362 両心四角形：内接かつ外接（約45秒）"""

    def construct(self):
        self.show_heading("両心四角形")
        self.draw_both()
        self.condition()
        self.show_formula()
        self.read(1.4)

    def draw_both(self):
        self.O = ORIGIN + DOWN * 0.1
        self.outer = Circle(radius=2.2, color=GREY, stroke_width=2).move_to(self.O)
        self.inner = Circle(radius=0.95, color=TEAL, stroke_width=3).move_to(self.O)
        angs = [0.3, 1.6, 3.2, 4.9]
        self.pts = [self.O + 2.2 * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        self.quad = Polygon(*self.pts, color=BLUE, stroke_width=3)
        self.play(Create(self.outer), Create(self.inner), Create(self.quad), run_time=1.6)
        note = self.ja_text("内外とも円", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def condition(self):
        cap = self.ja_text("ピトー＋対角和", font_size=24).move_to(self.note)
        # highlight both conditions lightly
        box = SurroundingRectangle(self.quad, color=YELLOW, buff=0.15)
        self.play(Create(box), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("両方満たす", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"a+c=b+d,\ \angle A+\angle C=\pi").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
