from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class Talbot(PacedScene):
    """#338 タルボット：円錐曲線に内接する六角形の対辺（約45秒）"""

    def construct(self):
        self.show_heading("タルボットの定理")
        self.draw_conic()
        self.hexagon()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_conic(self):
        self.O = ORIGIN + DOWN * 0.15
        self.ell = Ellipse(width=5.2, height=3.2, color=GREY, stroke_width=3).move_to(self.O)
        self.play(Create(self.ell), run_time=1.2)
        note = self.ja_text("円錐曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def hexagon(self):
        angs = np.linspace(0.2, 2 * np.pi + 0.2, 7)[:-1]
        pts = [self.O + np.array([2.5 * np.cos(a), 1.5 * np.sin(a), 0]) for a in angs]
        hexagon = Polygon(*pts, color=BLUE, stroke_width=3)
        # opposite sides highlighted
        opp = VGroup(
            Line(pts[0], pts[1], color=ORANGE, stroke_width=6),
            Line(pts[3], pts[4], color=ORANGE, stroke_width=6),
        )
        cap = self.ja_text("内接六角形", font_size=24).move_to(self.note)
        self.play(Create(hexagon), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("対辺が平行", font_size=24).move_to(self.note)
        self.play(Create(opp[0]), Create(opp[1]), Transform(self.note, cap2), run_time=1.3)
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
        formula = self.ja_text("対辺が平行", font_size=30)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
