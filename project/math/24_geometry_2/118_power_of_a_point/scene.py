from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class PowerOfAPoint(JapaneseScene):
    """#118 方べきの定理（約90秒）"""

    def construct(self):
        self.show_heading("方べきの定理")
        self.draw_chords()
        self.show_formula()
        self.hold(1.2)

    def _hits(self, center, radius, point, direction):
        d = np.array(direction, dtype=float)
        d = d / np.linalg.norm(d)
        w = point - center
        b = 2 * np.dot(w, d)
        c = np.dot(w, w) - radius ** 2
        disc = b * b - 4 * c
        t1 = (-b - np.sqrt(disc)) / 2
        t2 = (-b + np.sqrt(disc)) / 2
        return point + t1 * d, point + t2 * d

    def draw_chords(self):
        o = np.array(LEFT * 1.6 + DOWN * 0.15)
        r = 2.15
        circ = Circle(radius=r, color=WHITE, stroke_width=2).move_to(o)
        P = o + np.array([-0.35, -0.15, 0.0])
        A, B = self._hits(o, r, P, np.array([1.6, -0.85, 0.0]))
        C, D = self._hits(o, r, P, np.array([0.55, 1.7, 0.0]))
        l1 = Line(A, B, color=YELLOW, stroke_width=4)
        l2 = Line(C, D, color=BLUE, stroke_width=4)
        self.play(Create(circ), run_time=0.55)
        self.play(Create(l1), Create(l2), run_time=0.7)
        dots = VGroup(*[Dot(p, radius=0.07, color=WHITE) for p in (P, A, B, C, D)])
        labs = VGroup(
            MathTex("P", font_size=26).next_to(P, DR, buff=0.08),
            MathTex("A", font_size=26).next_to(A, UL, buff=0.06),
            MathTex("B", font_size=26).next_to(B, DR, buff=0.06),
            MathTex("C", font_size=26).next_to(C, DL, buff=0.06),
            MathTex("D", font_size=26).next_to(D, UR, buff=0.06),
        )
        self.play(FadeIn(dots), FadeIn(labs), run_time=0.5)
        note = self.ja_text("積が等しい", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"PA\cdot PB=PC\cdot PD").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
