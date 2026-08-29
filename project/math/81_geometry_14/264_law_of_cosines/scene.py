from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class LawOfCosines(PacedScene):
    """#264 余弦定理はピタゴラスの一般化（約45秒）"""

    def construct(self):
        self.show_heading("余弦定理")
        self.draw_triangle()
        self.mark_angle()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.6 + DOWN * 1.4
        self.B = RIGHT * 2.8 + DOWN * 1.4
        self.C = LEFT * 0.3 + UP * 1.9
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mark_angle(self):
        ang = Angle(Line(self.C, self.A), Line(self.C, self.B), radius=0.45, color=ORANGE)
        self.play(Create(ang), run_time=0.9)
        # highlight opposite side AB
        ab = Line(self.A, self.B, color=YELLOW, stroke_width=5)
        cap = self.ja_text("対辺 c", font_size=24).move_to(self.note)
        self.play(Create(ab), Transform(self.note, cap), run_time=1.2)
        self.read(0.3)
        cap2 = self.ja_text("角で補正", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
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
        eq = MathTex(r"c^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"c^{2}=a^{2}+b^{2}-2ab\cos C").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"c^{2}=a^{2}+b^{2}-2ab\cos C").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
