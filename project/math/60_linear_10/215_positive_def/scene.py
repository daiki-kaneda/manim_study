from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class PositiveDefinite(PacedScene):
    """#215 正定値はどの方向も x^T A x > 0（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 1.0
        self.show_heading("正定値")
        self.draw_ellipse()
        self.check_directions()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_ellipse(self):
        # level set x^T A x = 1 for A=diag(0.35, 0.9) → ellipse
        ell = Ellipse(width=4.2, height=2.4, color=BLUE, stroke_width=4).move_to(self.origin)
        self.play(Create(ell), run_time=1.4)
        note = self.ja_text("二次形式", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.ell = ell

    def check_directions(self):
        checks = VGroup()
        for ang, col in ((0.2, YELLOW), (1.0, TEAL), (2.0, ORANGE)):
            tip = self.origin + 1.5 * np.array([np.cos(ang), np.sin(ang), 0])
            arr = Arrow(self.origin, tip, buff=0, color=col, stroke_width=4)
            checks.add(arr)
        cap = self.ja_text("どの方向も正", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in checks], lag_ratio=0.2), Transform(self.note, cap), run_time=1.8)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"x^{\mathsf T}Ax>0\quad(x\neq 0)").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
