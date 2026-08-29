from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
import numpy as np
from manim_math import PacedScene


class AuxiliaryCircle(PacedScene):
    """#626 補助円：楕円のパラメータ化に使う円（約45秒）"""

    def construct(self):
        self.show_heading("補助円")
        self.draw_circle()
        self.project()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        circ = Circle(radius=1.8, color=ORANGE, stroke_width=3).shift(LEFT * 0.4 + UP * 0.15)
        ell = Ellipse(width=3.6, height=2.2, color=BLUE, stroke_width=3).move_to(circ)
        self.play(Create(circ), Create(ell), run_time=1.3)
        note = self.ja_text("主円・副円", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.circ = circ
        self.ell = ell

    def project(self):
        theta = PI / 3
        P = Dot(self.circ.point_at_angle(theta), color=YELLOW, radius=0.09)
        Q = Dot(self.ell.get_center() + np.array([1.8 * np.cos(theta), 1.1 * np.sin(theta), 0]), color=TEAL, radius=0.09)
        line = DashedLine(P.get_center(), Q.get_center(), color=GREY, stroke_width=2)
        cap = self.ja_text("縦に縮める", font_size=24).move_to(self.note)
        self.play(FadeIn(P), FadeIn(Q), Create(line), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("離心角 θ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x=a\cos\theta,\quad y=b\sin\theta").scale(0.8)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
