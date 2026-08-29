from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class SoddyCircles(PacedScene):
    """#409 ソディ：3 円に接する第 4 円（約45秒）"""

    def construct(self):
        self.show_heading("ソディの円")
        self.draw_three()
        self.fourth()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_three(self):
        centers = [LEFT * 1.3 + DOWN * 0.3, RIGHT * 1.3 + DOWN * 0.3, UP * 1.5]
        self.circs = VGroup(*[
            Circle(radius=1.15, color=c, stroke_width=3).move_to(p)
            for p, c in zip(centers, [BLUE, TEAL, GREEN])
        ])
        self.play(LaggedStart(*[Create(c) for c in self.circs], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("3 円が接する", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def fourth(self):
        inner = Circle(radius=0.45, color=ORANGE, stroke_width=4).move_to(UP * 0.35)
        outer = Circle(radius=2.6, color=YELLOW, stroke_width=2).move_to(UP * 0.2)
        cap = self.ja_text("内側の解", font_size=24).move_to(self.note)
        self.play(Create(inner), Transform(self.note, cap), run_time=1.2)
        self.read(0.2)
        cap2 = self.ja_text("外側の解も", font_size=24).move_to(self.note)
        self.play(Create(outer), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"k_4").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"k_4=k_1+k_2+k_3\pm 2\sqrt{k_1k_2+k_2k_3+k_3k_1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"k_4=k_1+k_2+k_3\pm 2\sqrt{k_1k_2+k_2k_3+k_3k_1}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
