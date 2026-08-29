from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class PowerIteration(PacedScene):
    """#239 冪乗法は主固有ベクトルへ寄る（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 1.15
        self.show_heading("冪乗法")
        self.draw_start()
        self.iterate()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_start(self):
        ax = Line(self.origin + LEFT * 0.2, self.origin + RIGHT * 5.0, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.2, self.origin + UP * 3.4, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.7)
        self.v = np.array([1.0, 1.4])
        self.arr = Arrow(self.origin, self._pt(self.v / np.linalg.norm(self.v) * 2.3), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.arr), run_time=1.0)
        note = self.ja_text("初期", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def iterate(self):
        A = np.array([[3.0, 0.4], [0.4, 1.2]])
        v = self.v.astype(float)
        trail = VGroup()
        for i, col in enumerate((BLUE, TEAL, ORANGE)):
            v = A @ v
            v = v / np.linalg.norm(v)
            tip = self._pt(v * 2.3)
            trail.add(Dot(tip, radius=0.05, color=GREY_B))
            new = Arrow(self.origin, tip, buff=0, color=col, stroke_width=5)
            self.play(Transform(self.arr, new), FadeIn(trail[-1]), run_time=0.9)
        cap = self.ja_text("主方向へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"v_{k+1}=\frac{Av_k}{\|Av_k\|}").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
