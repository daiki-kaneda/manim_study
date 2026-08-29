from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class NumericalRadius(PacedScene):
    """#359 数値半径：数値域の原点からの最大距離（約45秒）"""

    def construct(self):
        self.show_heading("数値半径")
        self.draw_field()
        self.radius()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_field(self):
        self.O = LEFT * 0.5 + DOWN * 0.15
        ax = Line(self.O + LEFT * 2.6, self.O + RIGHT * 2.8, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 2.0, self.O + UP * 2.0, color=GREY, stroke_width=2)
        region = Ellipse(width=3.4, height=2.2, color=BLUE, fill_opacity=0.25, stroke_width=3).move_to(self.O + RIGHT * 0.4 + UP * 0.2)
        self.play(Create(ax), Create(ay), FadeIn(region), run_time=1.4)
        note = self.ja_text("数値域", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.region = region

    def radius(self):
        # farthest point
        tip = self.O + RIGHT * 2.0 + UP * 0.9
        R = float(np.linalg.norm(tip - self.O))
        ray = DashedLine(self.O, tip, color=ORANGE, stroke_width=3)
        circ = Circle(radius=R, color=ORANGE, stroke_width=3).move_to(self.O)
        cap = self.ja_text("一番遠い点", font_size=24).move_to(self.note)
        self.play(Create(ray), FadeIn(Dot(tip, color=YELLOW, radius=0.1)), Transform(self.note, cap), run_time=1.3)
        self.play(Create(circ), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("数値半径", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"w(A)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"w(A)=\sup_{\|x\|=1}|x^{*}Ax|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"w(A)=\sup_{\|x\|=1}|x^{*}Ax|").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
