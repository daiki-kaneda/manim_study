from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class NormEquivalence(PacedScene):
    """#251 有限次元ではノルムは同値（約45秒）"""

    def construct(self):
        self.O = LEFT * 2.2 + DOWN * 0.2
        self.show_heading("ノルムの同値")
        self.draw_balls()
        self.sandwich()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_balls(self):
        # l2 circle and l1 diamond and linf square
        circ = Circle(radius=1.5, color=BLUE, stroke_width=3).move_to(self.O)
        diamond = Polygon(
            self.O + UP * 1.5,
            self.O + RIGHT * 1.5,
            self.O + DOWN * 1.5,
            self.O + LEFT * 1.5,
            color=TEAL,
            stroke_width=3,
        )
        square = Square(side_length=2.4, color=YELLOW, stroke_width=3).move_to(self.O)
        self.play(Create(circ), run_time=1.0)
        self.play(Create(diamond), run_time=1.0)
        self.play(Create(square), run_time=1.0)
        note = self.ja_text("単位球", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sandwich(self):
        # show scaled circle containing diamond
        outer = Circle(radius=2.1, color=ORANGE, stroke_width=2).move_to(self.O)
        inner = Circle(radius=1.05, color=ORANGE, stroke_width=2).move_to(self.O)
        cap = self.ja_text("定数倍で挟む", font_size=24).move_to(self.note)
        self.play(Create(outer), Create(inner), Transform(self.note, cap), run_time=1.5)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"c\|x\|_a\le\|x\|_b\le C\|x\|_a").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"c\|x\|_a\le\|x\|_b\le C\|x\|_a").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"c\|x\|_a\le\|x\|_b\le C\|x\|_a").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
