from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class GramSchmidt(PacedScene):
    """#142 グラム・シュミットは射影を引く（約50秒）"""

    def construct(self):
        self.origin = LEFT * 3.3 + DOWN * 1.55
        self.show_heading("直交化")
        self.draw_vectors()
        self.project()
        self.subtract()
        self.show_formula()
        self.read(1.4)

    def _v(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_vectors(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 6.4, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 4.0, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        self.v1 = np.array([4.4, 0.55, 0.0])
        self.v2 = np.array([2.15, 2.85, 0.0])
        self.a1 = Arrow(self.origin, self._v(self.v1), buff=0, color=BLUE, stroke_width=5)
        self.a2 = Arrow(self.origin, self._v(self.v2), buff=0, color=YELLOW, stroke_width=5)
        l1 = MathTex(r"v_1", color=BLUE, font_size=32).next_to(self.a1.get_end(), DOWN, buff=0.1)
        l2 = MathTex(r"v_2", color=YELLOW, font_size=32).next_to(self.a2.get_end(), LEFT, buff=0.1)
        self.play(GrowArrow(self.a1), FadeIn(l1), run_time=1.1)
        self.play(GrowArrow(self.a2), FadeIn(l2), run_time=1.1)
        self.read(0.4)

    def project(self):
        t = np.dot(self.v2[:2], self.v1[:2]) / np.dot(self.v1[:2], self.v1[:2])
        self.proj = t * self.v1
        foot = self._v(self.proj)
        dashed = DashedLine(self._v(self.v2), foot, color=ORANGE, stroke_width=3)
        self.ap = Arrow(self.origin, foot, buff=0, color=ORANGE, stroke_width=4)
        note = self.ja_text("射影", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(Create(dashed), GrowArrow(self.ap), FadeIn(note), run_time=1.6)
        self.read(0.4)
        self.note = note
        self.foot = foot

    def subtract(self):
        u2 = self.v2 - self.proj
        au = Arrow(self.foot, self._v(self.v2), buff=0, color=GREEN, stroke_width=6)
        cap = self.ja_text("引く", font_size=24).move_to(self.note)
        self.play(GrowArrow(au), Transform(self.note, cap), run_time=1.3)
        self.read(0.35)
        moved = Arrow(self.origin, self.origin + (self._v(self.v2) - self.foot), buff=0, color=GREEN, stroke_width=6)
        self.play(Transform(au, moved), run_time=1.2)
        cap2 = self.ja_text("直角", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"u_2=v_2-\mathrm{proj}_{v_1}v_2").scale(0.92)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
