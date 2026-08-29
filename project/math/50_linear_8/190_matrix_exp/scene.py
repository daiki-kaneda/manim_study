from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class MatrixExponential(PacedScene):
    """#190 行列指数は流れを時刻 t まで進める（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 1.2
        self.show_heading("行列の指数関数")
        self.draw_flow()
        self.advance()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_flow(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 5.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.5, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        # start vector
        self.v0 = np.array([2.2, 0.6])
        self.arr = Arrow(self.origin, self._pt(self.v0), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.arr), run_time=1.2)
        note = self.ja_text("出発", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def advance(self):
        # rotation-scaling: e^{tA} with A = [[0,-1],[1,0]] scaled + slight growth
        path_dots = VGroup()
        for t in (0.4, 0.8, 1.2, 1.6):
            c, s = np.cos(t), np.sin(t)
            scale = 1.0 + 0.18 * t
            v = scale * np.array([c * self.v0[0] - s * self.v0[1], s * self.v0[0] + c * self.v0[1]])
            path_dots.add(Dot(self._pt(v), radius=0.05, color=GREY_B))
        self.play(LaggedStart(*[FadeIn(d) for d in path_dots], lag_ratio=0.15), run_time=1.2)
        c, s = np.cos(1.6), np.sin(1.6)
        scale = 1.0 + 0.18 * 1.6
        v = scale * np.array([c * self.v0[0] - s * self.v0[1], s * self.v0[0] + c * self.v0[1]])
        new = Arrow(self.origin, self._pt(v), buff=0, color=BLUE, stroke_width=5)
        cap = self.ja_text("時刻 t", font_size=24).move_to(self.note)
        self.play(Transform(self.arr, new), Transform(self.note, cap), run_time=1.7)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"e^{tA}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"e^{tA}=\sum_{k=0}^{\infty}\frac{(tA)^k}{k!}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"e^{tA}=\sum_{k=0}^{\infty}\frac{(tA)^k}{k!}").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
