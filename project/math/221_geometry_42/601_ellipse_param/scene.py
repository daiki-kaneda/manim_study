from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class EllipseParam(PacedScene):
    """#601 楕円のパラメータ：離心角で点を表す（約45秒）"""

    def construct(self):
        self.show_heading("楕円のパラメータ")
        self.draw_ellipse()
        self.angle()
        self.show_formula()
        self.read(1.4)

    def draw_ellipse(self):
        ell = Ellipse(width=5.0, height=2.8, color=BLUE, stroke_width=3).shift(UP * 0.15)
        aux = Circle(radius=2.5, color=GREY, stroke_width=2).shift(UP * 0.15)
        self.play(Create(aux), Create(ell), run_time=1.3)
        note = self.ja_text("補助円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.ell = ell

    def angle(self):
        import numpy as np
        P = UP * 0.15 + RIGHT * 2.5 * np.cos(0.8) + UP * 1.4 * np.sin(0.8)
        Q = UP * 0.15 + RIGHT * 2.5 * np.cos(0.8) + UP * 2.5 * np.sin(0.8)
        self.play(FadeIn(Dot(P, color=YELLOW)), FadeIn(Dot(Q, color=ORANGE)),
                  Create(DashedLine(Q, P, color=GREY)), run_time=1.2)
        cap = self.ja_text("離心角 θ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("パラメータ表示", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x=a\cos\theta,\ y=b\sin\theta").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
