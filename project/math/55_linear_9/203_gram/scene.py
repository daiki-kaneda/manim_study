from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class GramMatrix(PacedScene):
    """#203 グラム行列は内積の表（約45秒）"""

    def construct(self):
        self.origin = LEFT * 3.2 + DOWN * 1.3
        self.show_heading("グラム行列")
        self.draw_vectors()
        self.build_table()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_vectors(self):
        ax = Line(self.origin + LEFT * 0.2, self.origin + RIGHT * 4.2, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.2, self.origin + UP * 3.2, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.7)
        self.v1 = np.array([2.4, 0.7])
        self.v2 = np.array([1.1, 2.2])
        a1 = Arrow(self.origin, self._pt(self.v1), buff=0, color=BLUE, stroke_width=5)
        a2 = Arrow(self.origin, self._pt(self.v2), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=1.3)
        note = self.ja_text("ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def build_table(self):
        g11 = float(self.v1 @ self.v1)
        g12 = float(self.v1 @ self.v2)
        g22 = float(self.v2 @ self.v2)
        mat = Matrix(
            [[f"{g11:.1f}", f"{g12:.1f}"], [f"{g12:.1f}", f"{g22:.1f}"]],
            h_buff=1.0,
            v_buff=0.7,
        ).scale(0.75)
        mat.to_edge(RIGHT, buff=0.55).shift(DOWN * 0.2)
        cap = self.ja_text("内積の表", font_size=24).move_to(self.note)
        self.play(FadeIn(mat), Transform(self.note, cap), run_time=1.5)
        self.read(0.35)
        # highlight off-diagonal
        off = SurroundingRectangle(mat.get_entries()[1], color=ORANGE, buff=0.12)
        cap2 = self.ja_text("なす角", font_size=24).move_to(self.note)
        self.play(Create(off), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"G=A^{\mathsf T}A").scale(1.15)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
