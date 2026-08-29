from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class FermatPoint(PacedScene):
    """#204 フェルマー点で角は 120°（約45秒）"""

    def construct(self):
        self.show_heading("フェルマー点")
        self.draw_triangle()
        self.mark_point()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.8 + DOWN * 1.4
        self.B = RIGHT * 2.9 + DOWN * 1.5
        self.C = LEFT * 0.3 + UP * 2.05
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.3)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mark_point(self):
        # Approximate Fermat-Torricelli for acute triangle: minimize total distance
        # Use geometric construction: outward equilateral on BC, then line to A
        # For simplicity, iterate a few gradient steps from centroid
        P = (self.A + self.B + self.C) / 3
        for _ in range(40):
            dirs = []
            for Q in (self.A, self.B, self.C):
                v = Q - P
                n = np.linalg.norm(v)
                if n > 1e-6:
                    dirs.append(v / n)
            P = P + 0.08 * sum(dirs)
        lines = VGroup(
            Line(P, self.A, color=BLUE, stroke_width=3),
            Line(P, self.B, color=TEAL, stroke_width=3),
            Line(P, self.C, color=YELLOW, stroke_width=3),
        )
        cap = self.ja_text("最短合計", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.15), Transform(self.note, cap), run_time=1.7)
        self.read(0.3)
        dot = Dot(P, color=RED, radius=0.11)
        ang = Angle(Line(P, self.A), Line(P, self.B), radius=0.4, color=ORANGE)
        lab = MathTex(r"120^\circ", color=ORANGE, font_size=28).next_to(ang, DOWN, buff=0.08)
        cap2 = self.ja_text("どれも 120°", font_size=24).move_to(self.note)
        self.play(FadeIn(dot), Create(ang), FadeIn(lab), Transform(self.note, cap2), run_time=1.5)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("距離の和が最小", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
