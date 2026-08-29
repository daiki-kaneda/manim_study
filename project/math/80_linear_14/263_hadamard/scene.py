from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class HadamardInequality(PacedScene):
    """#263 アダマール：|det| ≤ 列ノルムの積（約45秒）"""

    def construct(self):
        self.O = LEFT * 2.6 + DOWN * 1.3
        self.show_heading("アダマールの不等式")
        self.draw_parallelogram()
        self.compare_box()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.O + RIGHT * xy[0] + UP * xy[1]

    def draw_parallelogram(self):
        self.v = np.array([2.6, 0.4])
        self.w = np.array([0.9, 2.2])
        para = Polygon(
            self._pt([0, 0]),
            self._pt(self.v),
            self._pt(self.v + self.w),
            self._pt(self.w),
            color=BLUE,
            stroke_width=3,
            fill_opacity=0.25,
        )
        a1 = Arrow(self._pt([0, 0]), self._pt(self.v), buff=0, color=YELLOW, stroke_width=4)
        a2 = Arrow(self._pt([0, 0]), self._pt(self.w), buff=0, color=TEAL, stroke_width=4)
        self.play(Create(para), GrowArrow(a1), GrowArrow(a2), run_time=1.6)
        note = self.ja_text("列ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def compare_box(self):
        # axis-aligned box with same side lengths
        lv = np.linalg.norm(self.v)
        lw = np.linalg.norm(self.w)
        box = Rectangle(width=lv, height=lw, color=ORANGE, stroke_width=3)
        box.move_to(RIGHT * 2.3 + UP * 0.2)
        cap = self.ja_text("辺の積", font_size=24).move_to(self.note)
        self.play(Create(box), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("面積はそれ以下", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
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
        eq = MathTex(r"|\det A|\le\prod_j\|a_j\|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|\det A|\le\prod_j\|a_j\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|\det A|\le\prod_j\|a_j\|").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
