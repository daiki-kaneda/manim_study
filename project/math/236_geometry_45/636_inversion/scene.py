from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CircleInversion(PacedScene):
    """#636 円の反転：半径の二乗で距離を写す（約45秒）"""

    def construct(self):
        self.show_heading("円の反転")
        self.draw_circle()
        self.map_point()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        circ = Circle(radius=1.6, color=BLUE, stroke_width=3).shift(LEFT * 0.5 + UP * 0.1)
        O = Dot(circ.get_center(), color=YELLOW, radius=0.09)
        self.play(Create(circ), FadeIn(O), FadeIn(MathTex(r"O", font_size=24).next_to(O, DOWN, buff=0.1)), run_time=1.2)
        note = self.ja_text("反転円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.circ = circ
        self.O = O

    def map_point(self):
        P = Dot(self.circ.get_center() + RIGHT * 0.9 + UP * 0.5, color=ORANGE, radius=0.09)
        # P' farther on same ray
        v = P.get_center() - self.O.get_center()
        import numpy as np
        u = v / np.linalg.norm(v)
        Pp = Dot(self.O.get_center() + u * (1.6 ** 2 / np.linalg.norm(v)), color=TEAL, radius=0.09)
        ray = Line(self.O.get_center(), Pp.get_center() + u * 0.3, color=GREY, stroke_width=2)
        cap = self.ja_text("同一半直線上", font_size=24).move_to(self.note)
        self.play(Create(ray), FadeIn(P), FadeIn(Pp),
                  FadeIn(MathTex(r"P", font_size=24).next_to(P, UP, buff=0.08)),
                  FadeIn(MathTex(r"P'", font_size=24).next_to(Pp, UP, buff=0.08)),
                  Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("円・直線を保つ", font_size=24).move_to(self.note)
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
        eq = MathTex(r"OP\cdot OP'").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"OP\cdot OP'=R^2").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"OP\cdot OP'=R^2").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
