from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class BritishFlag(PacedScene):
    """#278 英国旗定理：直交で距離の二乗和が等しい（約45秒）"""

    def construct(self):
        self.show_heading("英国旗定理")
        self.draw_rect()
        self.point_inside()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_rect(self):
        self.A = LEFT * 2.6 + DOWN * 1.4
        self.B = RIGHT * 2.6 + DOWN * 1.4
        self.C = RIGHT * 2.6 + UP * 1.4
        self.D = LEFT * 2.6 + UP * 1.4
        self.rect = Polygon(self.A, self.B, self.C, self.D, color=BLUE, stroke_width=3)
        self.play(Create(self.rect), run_time=1.2)
        note = self.ja_text("長方形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def point_inside(self):
        P = ORIGIN + LEFT * 0.5 + UP * 0.3
        pdot = Dot(P, color=ORANGE, radius=0.1)
        segs = VGroup(
            Line(P, self.A, color=YELLOW, stroke_width=3),
            Line(P, self.B, color=TEAL, stroke_width=3),
            Line(P, self.C, color=YELLOW, stroke_width=3),
            Line(P, self.D, color=TEAL, stroke_width=3),
        )
        cap = self.ja_text("点 P", font_size=24).move_to(self.note)
        self.play(FadeIn(pdot), Transform(self.note, cap), run_time=0.8)
        self.play(LaggedStart(*[Create(s) for s in segs], lag_ratio=0.1), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("二乗和が等しい", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(segs[0], color=YELLOW), Indicate(segs[2], color=TEAL), run_time=1.2)
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
        eq = MathTex(r"PA^{2}+PC^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"PA^{2}+PC^{2}=PB^{2}+PD^{2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"PA^{2}+PC^{2}=PB^{2}+PD^{2}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
