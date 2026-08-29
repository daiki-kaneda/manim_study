from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np



class GaussianMeasure(PacedScene):
    """#520 ガウス測度：無限次元の正規分布（約45秒）"""

    def construct(self):
        self.show_heading("ガウス測度")
        self.draw_ball()
        self.cylinder()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ball(self):
        circ = Circle(radius=1.5, color=BLUE, stroke_width=3).shift(LEFT * 2.0 + UP * 0.2)
        cloud = VGroup(*[
            Dot(LEFT * 2.0 + np.array([np.cos(a) * r, np.sin(a) * r + 0.2, 0]), color=YELLOW, radius=0.05)
            for a in [0.3, 1.0, 1.7, 2.4, 3.2, 4.0, 4.8, 5.5]
            for r in [0.4, 0.9, 1.2]
        ])
        self.play(Create(circ), FadeIn(cloud), run_time=1.4)
        note = self.ja_text("ヒルベルト上", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cylinder(self):
        cyl = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.3 + UP * 0.2)
        cap = self.ja_text("円柱集合", font_size=24).move_to(self.note)
        self.play(Create(cyl), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("有限次元周辺は正規", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\mu").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mu=\mathcal{N}(0,C)\ \text{on }H").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mu=\mathcal{N}(0,C)\ \text{on }H").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
