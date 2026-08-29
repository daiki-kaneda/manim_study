from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class Morley(PacedScene):
    """#386 モルレー：角の三等分線が正三角形を作る（約45秒）"""

    def construct(self):
        self.show_heading("モルレーの定理")
        self.draw_triangle()
        self.trisectors()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.2 + LEFT * 0.15
        self.B = LEFT * 2.8 + DOWN * 1.5
        self.C = RIGHT * 2.9 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def trisectors(self):
        # schematic equilateral formed by adjacent trisectors
        center = (self.A + self.B + self.C) / 3
        r = 0.85
        angs = [np.pi / 2, np.pi / 2 + 2 * np.pi / 3, np.pi / 2 + 4 * np.pi / 3]
        D, E, F = [center + r * np.array([np.cos(a), np.sin(a), 0]) for a in angs]

        rays = VGroup(
            Line(self.A, D, color=YELLOW, stroke_width=2.5),
            Line(self.A, E, color=YELLOW, stroke_width=2.5),
            Line(self.B, D, color=TEAL, stroke_width=2.5),
            Line(self.B, F, color=TEAL, stroke_width=2.5),
            Line(self.C, E, color=ORANGE, stroke_width=2.5),
            Line(self.C, F, color=ORANGE, stroke_width=2.5),
        )
        cap = self.ja_text("角の三等分", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(r) for r in rays], lag_ratio=0.08), Transform(self.note, cap), run_time=1.8)
        self.read(0.2)
        eq = Polygon(D, E, F, color=RED, stroke_width=4)
        cap2 = self.ja_text("正三角形", font_size=24).move_to(self.note)
        self.play(Create(eq), Transform(self.note, cap2), run_time=1.2)
        self.play(Indicate(eq, color=YELLOW), run_time=0.7)
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
        formula = self.ja_text("三等分線が正三角形を作る", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
