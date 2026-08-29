from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class Varignon(PacedScene):
    """#276 ヴァリニョン：中点を結ぶと平行四辺形（約45秒）"""

    def construct(self):
        self.show_heading("ヴァリニョンの定理")
        self.draw_quad()
        self.midpoints()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        self.pts = [
            LEFT * 2.6 + DOWN * 1.2,
            LEFT * 0.4 + UP * 1.6,
            RIGHT * 2.8 + UP * 0.8,
            RIGHT * 1.4 + DOWN * 1.5,
        ]
        self.quad = Polygon(*self.pts, color=GREY, stroke_width=3)
        self.play(Create(self.quad), run_time=1.3)
        note = self.ja_text("四角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def midpoints(self):
        mids = [(self.pts[i] + self.pts[(i + 1) % 4]) / 2 for i in range(4)]
        dots = VGroup(*[Dot(m, color=YELLOW, radius=0.08) for m in mids])
        para = Polygon(*mids, color=ORANGE, stroke_width=4)
        cap = self.ja_text("各辺の中点", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("平行四辺形", font_size=24).move_to(self.note)
        self.play(Create(para), Transform(self.note, cap2), run_time=1.4)
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
        eq = MathTex(r"\overrightarrow{M_1M_2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\overrightarrow{M_1M_2}=\overrightarrow{M_4M_3}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\overrightarrow{M_1M_2}=\overrightarrow{M_4M_3}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
