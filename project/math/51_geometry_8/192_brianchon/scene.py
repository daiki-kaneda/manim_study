from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Brianchon(PacedScene):
    """#192 ブリアンション：接線六角形の対角は一点（約45秒）"""

    def construct(self):
        self.show_heading("ブリアンションの定理")
        self.draw_hexagon()
        self.draw_diagonals()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_hexagon(self):
        self.O = ORIGIN + DOWN * 0.15
        r = 1.35
        R = 2.55
        self.circle = Circle(radius=r, color=GREY, stroke_width=2).move_to(self.O)
        # vertices of tangential hexagon (regular for clarity)
        self.verts = [
            self.O + R * np.array([np.cos(i * PI / 3 + PI / 6), np.sin(i * PI / 3 + PI / 6), 0])
            for i in range(6)
        ]
        self.hex = Polygon(*self.verts, color=BLUE, stroke_width=3)
        self.play(Create(self.circle), run_time=1.0)
        self.play(Create(self.hex), run_time=1.5)
        note = self.ja_text("内接円", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def draw_diagonals(self):
        cols = [YELLOW, ORANGE, TEAL]
        diags = VGroup()
        for i, col in enumerate(cols):
            d = Line(self.verts[i], self.verts[i + 3], color=col, stroke_width=4)
            diags.add(d)
        cap = self.ja_text("対角", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(d) for d in diags], lag_ratio=0.2), Transform(self.note, cap), run_time=1.8)
        self.read(0.3)
        meet = Dot(self.O, color=RED, radius=0.11)
        cap2 = self.ja_text("一点で交わる", font_size=24).move_to(self.note)
        self.play(FadeIn(meet, scale=0.5), Transform(self.note, cap2), run_time=1.2)
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
        formula = self.ja_text("接線六角形の対角は共点", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(FadeIn(formula), run_time=1.2)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
