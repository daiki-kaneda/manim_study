from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class MatrixNorm(PacedScene):
    """#202 行列ノルムは単位円の最大伸び（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.6 + DOWN * 1.1
        self.show_heading("行列ノルム")
        self.draw_unit()
        self.stretch()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_unit(self):
        self.R = 1.35
        circ = Circle(radius=self.R, color=GREY, stroke_width=2).move_to(self.origin)
        self.play(Create(circ), run_time=1.1)
        note = self.ja_text("単位円", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def stretch(self):
        # A = [[2.2, 0.6],[0.4, 1.1]] applied to unit circle → ellipse
        A = np.array([[2.2, 0.55], [0.35, 1.15]])
        pts = []
        for i in range(64):
            th = 2 * np.pi * i / 64
            v = np.array([np.cos(th), np.sin(th)])
            w = A @ v
            pts.append(self._pt(w))
        ell = Polygon(*pts, color=BLUE, stroke_width=4)
        cap = self.ja_text("写す", font_size=24).move_to(self.note)
        self.play(Create(ell), Transform(self.note, cap), run_time=1.7)
        self.read(0.3)
        # max stretch arrow
        # approx singular vector
        tip = self._pt(A @ np.array([1.0, 0.15]) / np.linalg.norm(A @ np.array([1.0, 0.15])) * np.linalg.norm(A @ np.array([1.0, 0.0])))
        # simpler: longest radius visually along first column-ish
        v = A @ np.array([1.0, 0.0])
        arr = Arrow(self.origin, self._pt(v), buff=0, color=ORANGE, stroke_width=5)
        cap2 = self.ja_text("最大伸び", font_size=24).move_to(self.note)
        self.play(GrowArrow(arr), Transform(self.note, cap2), run_time=1.4)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\|A\|").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|A\|=\sup_{\|x\|=1}\|Ax\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|A\|=\sup_{\|x\|=1}\|Ax\|").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
