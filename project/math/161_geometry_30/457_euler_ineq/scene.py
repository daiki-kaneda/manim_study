from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class EulerInequality(PacedScene):
    """#457 オイラーの不等式：R≥2r（約45秒）"""

    def construct(self):
        self.show_heading("オイラーの不等式")
        self.draw_circles()
        self.compare()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circles(self):
        self.A = UP * 2.15
        self.B = LEFT * 2.6 + DOWN * 1.45
        self.C = RIGHT * 2.7 + DOWN * 1.35
        tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        O = (self.A + self.B + self.C) / 3
        I = O + DOWN * 0.15
        import numpy as np
        R = float(np.linalg.norm(self.A - O)) * 1.02
        circ_R = Circle(radius=R, color=ORANGE, stroke_width=3).move_to(O)
        circ_r = Circle(radius=0.55, color=TEAL, stroke_width=3).move_to(I)
        self.play(Create(tri), run_time=1.0)
        self.play(Create(circ_R), Create(circ_r), run_time=1.2)
        note = self.ja_text("外接と内接", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare(self):
        cap = self.ja_text("R と r を比べる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("R は 2r 以上", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"R\ge 2r").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"R\ge 2r").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"R\ge 2r").scale(1.05)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
