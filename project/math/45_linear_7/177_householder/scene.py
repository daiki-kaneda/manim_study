from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Householder(PacedScene):
    """#177 ハウスホルダーは鏡映で零を作る（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 1.35
        self.show_heading("ハウスホルダー")
        self.draw_vector()
        self.reflect()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_vector(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 5.8, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.6, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.v = np.array([3.4, 2.4])
        self.arr = Arrow(self.origin, self._pt(self.v), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.arr), run_time=1.2)
        note = self.ja_text("ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def reflect(self):
        # mirror: angle bisector between v and e1*|v|
        target = np.array([np.linalg.norm(self.v), 0.0])
        u = self.v - target
        u = u / np.linalg.norm(u)
        # mirror line perpendicular to u through origin? Householder reflects across plane normal to u
        # 2D: line through origin with normal u
        # direction of mirror line is perpendicular to u
        d = np.array([-u[1], u[0]])
        mirror = Line(self._pt(-2.2 * d), self._pt(2.8 * d), color=GREY_B, stroke_width=3)
        cap = self.ja_text("鏡", font_size=24).move_to(self.note)
        self.play(Create(mirror), Transform(self.note, cap), run_time=1.2)
        self.read(0.3)
        # reflected vector = target direction
        new = Arrow(self.origin, self._pt(target), buff=0, color=BLUE, stroke_width=5)
        cap2 = self.ja_text("軸へ移す", font_size=24).move_to(self.note)
        self.play(Transform(self.arr, new), Transform(self.note, cap2), run_time=1.7)
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
        eq = MathTex(r"H").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"H=I-2\frac{uu^{\mathsf T}}{u^{\mathsf T}u}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"H=I-2\frac{uu^{\mathsf T}}{u^{\mathsf T}u}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
