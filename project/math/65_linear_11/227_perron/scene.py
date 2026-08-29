from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class PerronFrobenius(PacedScene):
    """#227 ペロン：正行列は正の主固有ベクトル（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.3
        self.show_heading("ペロン・フロベニウス")
        self.draw_positive()
        self.iterate()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_positive(self):
        mat = Matrix([["2", "1"], ["1", "2"]], h_buff=0.8, v_buff=0.65).scale(0.85)
        mat.to_edge(RIGHT, buff=0.7).shift(UP * 0.5)
        self.play(FadeIn(mat), run_time=1.1)
        note = self.ja_text("正の行列", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        ax = Line(self.origin + LEFT * 0.2, self.origin + RIGHT * 4.5, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.2, self.origin + UP * 3.3, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.6)

    def iterate(self):
        A = np.array([[2.0, 1.0], [1.0, 2.0]])
        v = np.array([1.0, 0.2])
        arr = Arrow(self.origin, self._pt(v / np.linalg.norm(v) * 2.2), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(arr), run_time=0.9)
        for _ in range(3):
            v = A @ v
            v = v / np.linalg.norm(v)
            new = Arrow(self.origin, self._pt(v * 2.2), buff=0, color=TEAL, stroke_width=5)
            self.play(Transform(arr, new), run_time=0.85)
        cap = self.ja_text("正の方向へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"Av=\lambda v,\quad v>0").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
