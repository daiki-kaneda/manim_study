from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Stokes2D(PacedScene):
    """#211 平面ストークスは回転＝周回（約45秒）"""

    def construct(self):
        self.show_heading("平面のストークス")
        self.draw_field()
        self.boundary()
        self.show_formula()
        self.read(1.4)

    def draw_field(self):
        self.center = ORIGIN + DOWN * 0.1
        arrows = VGroup()
        for r in (0.7, 1.3, 1.9):
            for t in np.linspace(0, TAU, 8, endpoint=False):
                p = self.center + r * np.array([np.cos(t), np.sin(t), 0])
                tang = np.array([-np.sin(t), np.cos(t), 0]) * 0.4
                arrows.add(Arrow(p - 0.15 * tang, p + 0.25 * tang, buff=0, color=BLUE, stroke_width=3, max_tip_length_to_length_ratio=0.3))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.03), run_time=1.8)
        note = self.ja_text("回転", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def boundary(self):
        circ = Circle(radius=2.15, color=YELLOW, stroke_width=4).move_to(self.center)
        self.play(Create(circ), run_time=1.3)
        # circulating arrow on boundary
        tip = self.center + 2.15 * RIGHT
        arr = Arrow(tip + DOWN * 0.35, tip + UP * 0.55, buff=0, color=ORANGE, stroke_width=5)
        cap = self.ja_text("周回積分", font_size=24).move_to(self.note)
        self.play(GrowArrow(arr), Transform(self.note, cap), run_time=1.3)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"\iint_D(\partial_x Q-\partial_y P)=\oint_{\partial D}P\,dx+Q\,dy").scale(0.58)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
