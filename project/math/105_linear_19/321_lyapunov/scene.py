from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class LyapunovEquation(PacedScene):
    """#321 リアプノフ方程式：安定性の二次形式（約45秒）"""

    def construct(self):
        self.show_heading("リアプノフ方程式")
        self.draw_flow()
        self.energy()
        self.show_formula()
        self.read(1.4)

    def draw_flow(self):
        self.O = LEFT * 0.6 + DOWN * 0.1
        arrows = VGroup(*[
            Arrow(self.O + r * np.array([np.cos(a), np.sin(a), 0]), self.O + 0.55 * r * np.array([np.cos(a), np.sin(a), 0]),
                  buff=0, color=BLUE, stroke_width=3)
            for a in np.linspace(0, 2 * np.pi, 8, endpoint=False)
            for r in [1.8]
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), run_time=1.5)
        note = self.ja_text("安定な流れ", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def energy(self):
        ell = Ellipse(width=3.6, height=2.2, color=ORANGE, stroke_width=4).move_to(self.O)
        cap = self.ja_text("エネルギー", font_size=24).move_to(self.note)
        self.play(Create(ell), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("減り続ける", font_size=24).move_to(self.note)
        self.play(ell.animate.scale(0.65), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"A^{\top}P+PA=-Q").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
