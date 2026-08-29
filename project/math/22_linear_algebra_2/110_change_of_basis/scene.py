from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class ChangeOfBasis(JapaneseScene):
    """#110 基底を変えると数字が変わる（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.35
        self.show_heading("基底の取りかえ")
        self.draw_grids()
        self.show_formula()
        self.hold(1.2)

    def _grid(self, e1, e2, color, n=4):
        lines = VGroup()
        for i in range(-1, n):
            p0 = self.origin + i * np.array([*e1, 0]) - 1.2 * np.array([*e2, 0])
            p1 = self.origin + i * np.array([*e1, 0]) + 2.6 * np.array([*e2, 0])
            lines.add(Line(p0, p1, color=color, stroke_width=1.5, stroke_opacity=0.7))
        for j in range(-1, n):
            p0 = self.origin + j * np.array([*e2, 0]) - 0.4 * np.array([*e1, 0])
            p1 = self.origin + j * np.array([*e2, 0]) + 3.4 * np.array([*e1, 0])
            lines.add(Line(p0, p1, color=color, stroke_width=1.5, stroke_opacity=0.7))
        return lines

    def draw_grids(self):
        g1 = self._grid((1.15, 0), (0, 1.15), GREY)
        self.play(FadeIn(g1), run_time=0.6)
        p = self.origin + RIGHT * 2.3 + UP * 1.15
        self.play(FadeIn(Dot(p, color=YELLOW, radius=0.1)), run_time=0.35)
        lab = MathTex(r"(2,1)", color=YELLOW, font_size=28).next_to(p, UR, buff=0.08)
        self.play(FadeIn(lab), run_time=0.3)
        self.hold(0.4)
        g2 = self._grid((1.25, 0.35), (0.45, 1.1), BLUE)
        self.play(FadeIn(g2), run_time=0.7)
        lab2 = MathTex(r"(1,1)", color=BLUE, font_size=28).next_to(p, DL, buff=0.1)
        self.play(FadeIn(lab2), run_time=0.35)
        note = self.ja_text("点は同じ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.6)

    def show_formula(self):
        formula = MathTex(r"x=P[x]_B").scale(1.15)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=0.95)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
