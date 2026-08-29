from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Apollonius(PacedScene):
    """#194 アポロニウス：距離比一定は円（約45秒）"""

    def construct(self):
        self.show_heading("アポロニウスの円")
        self.draw_foci()
        self.trace_locus()
        self.show_formula()
        self.read(1.4)

    def draw_foci(self):
        self.A = LEFT * 2.8 + DOWN * 0.2
        self.B = RIGHT * 1.6 + DOWN * 0.2
        da = Dot(self.A, color=YELLOW, radius=0.1)
        db = Dot(self.B, color=YELLOW, radius=0.1)
        la = MathTex("A", font_size=30).next_to(self.A, DOWN, buff=0.15)
        lb = MathTex("B", font_size=30).next_to(self.B, DOWN, buff=0.15)
        self.play(FadeIn(da), FadeIn(db), FadeIn(la), FadeIn(lb), run_time=1.2)
        note = self.ja_text("2 定点", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def trace_locus(self):
        # |PA|/|PB| = 2 → circle with center on AB line
        # For foci A,B distance d, ratio k=2:
        # center divides AB externally/internally
        k = 2.0
        A = self.A
        B = self.B
        # internal center of similitude: (k B - A)/(k-1)? For Apollonius circle of ratio k:
        # center C = (k^2 B - A)/(k^2 - 1), radius = k * |B-A| / |k^2 - 1|
        C = (k ** 2 * B - A) / (k ** 2 - 1)
        R = k * np.linalg.norm(B - A) / abs(k ** 2 - 1)
        # sample points on circle and draw segments to A,B for a few
        angles = [0.4, 1.3, 2.2, 3.5, 4.6]
        dots = VGroup()
        for ang in angles:
            p = C + R * np.array([np.cos(ang), np.sin(ang), 0])
            # keep on screen roughly
            if abs(p[1]) > 2.6 or abs(p[0]) > 5.5:
                continue
            d = Dot(p, radius=0.07, color=BLUE)
            dots.add(d)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.12), run_time=1.5)
        # show ratio for one point
        p0 = dots[0].get_center()
        la = DashedLine(p0, self.A, color=GREY_B, stroke_width=2)
        lb = DashedLine(p0, self.B, color=GREY_B, stroke_width=2)
        cap = self.ja_text("比が一定", font_size=24).move_to(self.note)
        self.play(Create(la), Create(lb), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        circ = Circle(radius=R, color=TEAL, stroke_width=4).move_to(C)
        cap2 = self.ja_text("軌跡は円", font_size=24).move_to(self.note)
        self.play(Create(circ), Transform(self.note, cap2), run_time=1.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\frac{PA}{PB}=k").scale(1.1)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
