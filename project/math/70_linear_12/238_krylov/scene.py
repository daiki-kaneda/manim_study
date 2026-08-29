from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Krylov(PacedScene):
    """#238 クリロフは v, Av, A²v… の張り（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.8 + DOWN * 1.2
        self.show_heading("クリロフ部分空間")
        self.draw_seed()
        self.expand()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pt(self, xy):
        return self.origin + RIGHT * xy[0] + UP * xy[1]

    def draw_seed(self):
        ax = Line(self.origin + LEFT * 0.2, self.origin + RIGHT * 5.0, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.2, self.origin + UP * 3.3, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.7)
        self.v = np.array([1.6, 0.5])
        self.arr = Arrow(self.origin, self._pt(self.v), buff=0, color=YELLOW, stroke_width=5)
        self.play(GrowArrow(self.arr), run_time=1.0)
        note = self.ja_text("出発 v", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def expand(self):
        A = np.array([[0.6, -0.9], [1.1, 0.5]])
        Av = A @ self.v
        A2v = A @ Av
        a1 = Arrow(self.origin, self._pt(Av), buff=0, color=BLUE, stroke_width=5)
        a2 = Arrow(self.origin, self._pt(A2v * 0.55), buff=0, color=TEAL, stroke_width=5)
        cap = self.ja_text("Av", font_size=24).move_to(self.note)
        self.play(GrowArrow(a1), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        # parallelogram span
        span = Polygon(
            self.origin,
            self._pt(self.v),
            self._pt(self.v + Av * 0.7),
            self._pt(Av * 0.7),
            color=ORANGE,
            fill_opacity=0.25,
            stroke_width=2,
        )
        cap2 = self.ja_text("張り広がる", font_size=24).move_to(self.note)
        self.play(FadeIn(span), GrowArrow(a2), Transform(self.note, cap2), run_time=1.5)
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
        eq = MathTex(r"\mathcal{K}_k").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathcal{K}_k=\mathrm{span}\{v,Av,\ldots,A^{k-1}v\}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathcal{K}_k=\mathrm{span}\{v,Av,\ldots,A^{k-1}v\}").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
