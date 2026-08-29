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
        self.derive()
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

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"x").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x=a\cos\theta,\quad y=b\sin\theta").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x=a\cos\theta,\quad y=b\sin\theta").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
