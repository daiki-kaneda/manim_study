from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Ceva(PacedScene):
    """#131 チェバの定理（約45秒）"""

    def construct(self):
        self.show_heading("チェバの定理")
        self.draw_triangle()
        self.draw_cevians()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.4 + UP * 2.05
        self.B = LEFT * 3.5 + DOWN * 1.55
        self.C = RIGHT * 1.55 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        labs = VGroup(
            MathTex("A", font_size=30).next_to(self.A, UP, buff=0.1),
            MathTex("B", font_size=30).next_to(self.B, DL, buff=0.08),
            MathTex("C", font_size=30).next_to(self.C, DR, buff=0.08),
        )
        self.play(FadeIn(labs), run_time=0.7)
        self.read(0.4)

    def _hit(self, p, q, a, b):
        """Intersection of lines p-q and a-b."""
        d1 = q - p
        d2 = b - a
        mat = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
        t = np.linalg.solve(mat, (a - p)[:2])[0]
        return p + t * d1

    def draw_cevians(self):
        P = 0.38 * self.A + 0.32 * self.B + 0.30 * self.C
        D = self._hit(self.A, P, self.B, self.C)
        E = self._hit(self.B, P, self.C, self.A)
        F = self._hit(self.C, P, self.A, self.B)
        lines = VGroup(
            Line(self.A, D, color=YELLOW, stroke_width=4),
            Line(self.B, E, color=BLUE, stroke_width=4),
            Line(self.C, F, color=GREEN, stroke_width=4),
        )
        self.play(LaggedStart(*[Create(ln) for ln in lines], lag_ratio=0.22), run_time=2.4)
        self.play(FadeIn(Dot(P, color=ORANGE, radius=0.08)), run_time=0.5)
        note = self.ja_text("一点で会う", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.55)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.8)
