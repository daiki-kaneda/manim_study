from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class CauchySchwarz(JapaneseScene):
    """#76 コーシー・シュワルツ（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.35
        self.show_heading("コーシー・シュワルツ")
        self.draw_vectors()
        self.project()
        self.show_formula()
        self.hold(1.2)

    def draw_vectors(self):
        axes_x = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 5.2, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.4, color=GREY, stroke_width=2)
        self.play(Create(axes_x), Create(axes_y), run_time=0.45)
        self.u = np.array([2.15, 2.35, 0.0])
        self.v = np.array([3.6, 0.55, 0.0])
        au = Arrow(self.origin, self.origin + self.u, buff=0, color=BLUE, stroke_width=4)
        av = Arrow(self.origin, self.origin + self.v, buff=0, color=GREEN, stroke_width=4)
        lu = MathTex("u", color=BLUE, font_size=32).next_to(au.get_end(), UL, buff=0.08)
        lv = MathTex("v", color=GREEN, font_size=32).next_to(av.get_end(), DOWN, buff=0.1)
        self.play(GrowArrow(au), FadeIn(lu), run_time=0.5)
        self.play(GrowArrow(av), FadeIn(lv), run_time=0.5)
        self.hold(0.4)

    def project(self):
        scale = np.dot(self.u, self.v) / np.dot(self.v, self.v)
        proj = scale * self.v
        foot = self.origin + proj
        drop = DashedLine(self.origin + self.u, foot, color=YELLOW, stroke_width=3)
        ap = Arrow(self.origin, foot, buff=0, color=YELLOW, stroke_width=5)
        lab = MathTex(r"\mathrm{proj}_v u", color=YELLOW, font_size=28)
        lab.next_to(ap.get_center(), DOWN, buff=0.12)
        self.play(Create(drop), GrowArrow(ap), FadeIn(lab), run_time=0.85)
        note = self.ja_text("射影は短い", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"|u\cdot v|\le|u||v|").scale(1.15)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
