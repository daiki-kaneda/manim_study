from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Butterfly(PacedScene):
    """#182 バタフライ定理（約45秒）"""

    def construct(self):
        self.show_heading("バタフライ定理")
        self.draw_circle_chord()
        self.draw_wings()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circle_chord(self):
        self.O = LEFT * 0.6 + DOWN * 0.1
        self.R = 2.15
        circ = Circle(radius=self.R, color=GREY_B, stroke_width=2).move_to(self.O)
        # horizontal chord through M
        self.M = self.O + LEFT * 0.35 + DOWN * 0.25
        # chord PQ through M
        # direction horizontal
        d = np.array([1.0, 0.15, 0.0])
        d = d / np.linalg.norm(d)
        # intersect circle with line M + t d
        # |M-O + t d|^2 = R^2
        w = self.M - self.O
        a = np.dot(d, d)
        b = 2 * np.dot(w, d)
        c = np.dot(w, w) - self.R ** 2
        disc = b * b - 4 * a * c
        t1 = (-b - np.sqrt(disc)) / (2 * a)
        t2 = (-b + np.sqrt(disc)) / (2 * a)
        self.P = self.M + t1 * d
        self.Q = self.M + t2 * d
        self.play(Create(circ), run_time=1.2)
        chord = Line(self.P, self.Q, color=WHITE, stroke_width=4)
        self.play(Create(chord), FadeIn(Dot(self.M, color=ORANGE, radius=0.09)), run_time=1.2)
        mlab = MathTex("M", color=ORANGE, font_size=28).next_to(self.M, DOWN, buff=0.1)
        self.play(FadeIn(mlab), run_time=0.4)
        note = self.ja_text("弦の中点", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.circ = circ

    def _circle_hit(self, a, b):
        d = b - a
        w = a - self.O
        A = np.dot(d[:2], d[:2])
        B = 2 * np.dot(w[:2], d[:2])
        C = np.dot(w[:2], w[:2]) - self.R ** 2
        disc = B * B - 4 * A * C
        ts = [(-B - np.sqrt(disc)) / (2 * A), (-B + np.sqrt(disc)) / (2 * A)]
        return [a + t * d for t in ts]

    def draw_wings(self):
        # two other chords through M: AD and BC style
        # pick directions
        d1 = np.array([0.55, 1.0, 0.0]); d1 /= np.linalg.norm(d1)
        d2 = np.array([-0.7, 1.0, 0.0]); d2 /= np.linalg.norm(d2)
        A, C = self._circle_hit(self.M - d1, self.M + d1)
        B, D = self._circle_hit(self.M - d2, self.M + d2)
        wings = VGroup(
            Line(A, C, color=YELLOW, stroke_width=4),
            Line(B, D, color=TEAL, stroke_width=4),
        )
        cap = self.ja_text("羽", font_size=24).move_to(self.note)
        self.play(Create(wings[0]), Create(wings[1]), Transform(self.note, cap), run_time=1.6)
        self.read(0.3)
        # AB and CD intersect PQ at X,Y — for butterfly, AX=BY when M midpoint
        # Get AB ∩ PQ and CD ∩ PQ
        def hit(p, q, a, b):
            d1 = q - p
            d2 = b - a
            mat = np.array([[d1[0], -d2[0]], [d1[1], -d2[1]]])
            t = np.linalg.solve(mat, (a - p)[:2])[0]
            return p + t * d1

        X = hit(A, B, self.P, self.Q)
        Y = hit(C, D, self.P, self.Q)
        extras = VGroup(
            Line(A, B, color=GREY_B, stroke_width=2),
            Line(C, D, color=GREY_B, stroke_width=2),
        )
        self.play(Create(extras), run_time=1.0)
        self.play(FadeIn(Dot(X, color=YELLOW, radius=0.08)), FadeIn(Dot(Y, color=TEAL, radius=0.08)), run_time=0.7)
        # short markers along the chord instead of large braces
        mx = Line(self.M, X, color=YELLOW, stroke_width=8)
        my = Line(self.M, Y, color=TEAL, stroke_width=8)
        cap2 = self.ja_text("MX=MY", font_size=24).move_to(self.note)
        self.play(Create(mx), Create(my), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"MX").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"MX=MY").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"MX=MY").scale(1.2)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.5)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
