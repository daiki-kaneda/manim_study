from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class MiquelFive(PacedScene):
    """#384 五点ミケル：5 円が順に交わるなら共点（約45秒）"""

    def construct(self):
        self.show_heading("五点ミケル")
        self.draw_circles()
        self.show_point()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circles(self):
        self.O = ORIGIN + DOWN * 0.15
        # five overlapping circles whose common concurrency is near O
        centers = [
            self.O + 1.15 * np.array([np.cos(a), np.sin(a), 0])
            for a in np.linspace(0.15, 2 * np.pi + 0.15, 6)[:-1]
        ]
        colors = [BLUE, TEAL, GREEN, ORANGE, PURPLE]
        self.circs = VGroup(*[
            Circle(radius=1.55, color=c, stroke_width=2.5).move_to(ctr)
            for ctr, c in zip(centers, colors)
        ])
        self.play(LaggedStart(*[Create(c) for c in self.circs], lag_ratio=0.12), run_time=2.0)
        note = self.ja_text("5 つの円", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def show_point(self):
        # consecutive intersection dots around the common point
        pts = VGroup(*[
            Dot(self.O + 0.55 * np.array([np.cos(a), np.sin(a), 0]), color=YELLOW, radius=0.07)
            for a in np.linspace(0.4, 2 * np.pi + 0.4, 6)[:-1]
        ])
        m = Dot(self.O, color=RED, radius=0.12)
        cap = self.ja_text("隣どうし交わる", font_size=24).move_to(self.note)
        self.play(FadeIn(pts), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("一点で会う", font_size=24).move_to(self.note)
        self.play(FadeIn(m, scale=0.5), Transform(self.note, cap2), run_time=1.1)
        self.play(Indicate(m, color=YELLOW), run_time=0.7)
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
        formula = self.ja_text("5 円の交点は共点", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
