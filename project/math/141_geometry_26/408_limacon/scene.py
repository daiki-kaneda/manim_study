from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class Limacon(PacedScene):
    """#408 パスカルの蝸牛線：r=a+b cosθ（約45秒）"""

    def construct(self):
        self.show_heading("パスカルの蝸牛線")
        self.draw_curve()
        self.param()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        a, b = 1.2, 0.9
        def pt(t):
            r = a + b * np.cos(t)
            return np.array([r * np.cos(t), r * np.sin(t), 0]) + LEFT * 0.4 + UP * 0.1
        curve = ParametricFunction(pt, t_range=[0, TAU], color=BLUE, stroke_width=4)
        self.play(Create(curve), run_time=1.6)
        note = self.ja_text("蝸牛線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.curve = curve

    def param(self):
        # radius sample
        O = LEFT * 0.4 + UP * 0.1
        ray = Arrow(O, O + RIGHT * 2.0 + UP * 0.6, buff=0, color=ORANGE, stroke_width=3)
        cap = self.ja_text("動径が変化", font_size=24).move_to(self.note)
        self.play(GrowArrow(ray), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("円の変形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"r=a+b\cos\theta").scale(1.0)
        formula = MathTex(r"r=a+b\cos	heta").scale(1.05)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
