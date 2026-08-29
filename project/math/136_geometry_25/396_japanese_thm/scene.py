from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class JapaneseTheorem(PacedScene):
    """#396 日本の定理：円に内接する四角形の内心は長方形（約45秒）"""

    def construct(self):
        self.show_heading("日本の定理")
        self.draw_cyclic()
        self.incenters()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_cyclic(self):
        self.O = ORIGIN + DOWN * 0.05
        self.circ = Circle(radius=2.3, color=GREY, stroke_width=2).move_to(self.O)
        angs = [0.3, 1.5, 3.2, 5.0]
        self.verts = [self.O + 2.3 * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        self.quad = Polygon(*self.verts, color=BLUE, stroke_width=3)
        self.play(Create(self.circ), Create(self.quad), run_time=1.4)
        note = self.ja_text("円内接四角形", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def incenters(self):
        # schematic incenters forming a rectangle
        c = sum(self.verts) / 4
        w, h = 1.1, 0.75
        centers = [
            c + np.array([-w, h, 0]) / 2,
            c + np.array([w, h, 0]) / 2,
            c + np.array([w, -h, 0]) / 2,
            c + np.array([-w, -h, 0]) / 2,
        ]
        d1 = DashedLine(self.verts[0], self.verts[2], color=GREY, stroke_width=2)
        d2 = DashedLine(self.verts[1], self.verts[3], color=GREY, stroke_width=2)
        dots = VGroup(*[Dot(p, color=ORANGE, radius=0.1) for p in centers])
        rect = Polygon(*centers, color=RED, stroke_width=3)
        cap = self.ja_text("4 つの内心", font_size=24).move_to(self.note)
        self.play(Create(d1), Create(d2), Transform(self.note, cap), run_time=1.1)
        self.play(FadeIn(dots), run_time=0.8)
        self.read(0.2)
        cap2 = self.ja_text("長方形を作る", font_size=24).move_to(self.note)
        self.play(Create(rect), Transform(self.note, cap2), run_time=1.2)
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
        formula = self.ja_text("4 内心が長方形をなす", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
