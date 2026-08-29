from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MoserNumber(PacedScene):
    """#593 モザー数：円を弦で分割する最大数（約45秒）"""

    def construct(self):
        self.show_heading("モザー数")
        self.draw_circle()
        self.chords()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        circ = Circle(radius=1.8, color=BLUE, stroke_width=3).shift(UP * 0.15)
        self.play(Create(circ), run_time=1.1)
        note = self.ja_text("円周上の点", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.circ = circ

    def chords(self):
        import numpy as np
        pts = [self.circ.point_from_proportion(t) for t in [0.05, 0.22, 0.4, 0.58, 0.75, 0.9]]
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in pts])
        chords = VGroup(*[
            Line(pts[i], pts[j], color=ORANGE, stroke_width=2)
            for i in range(len(pts)) for j in range(i + 1, len(pts))
        ])
        cap = self.ja_text("すべての弦", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), LaggedStart(*[Create(c) for c in chords], lag_ratio=0.02), Transform(self.note, cap), run_time=1.6)
        self.read(0.25)
        cap2 = self.ja_text("領域の最大数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M(n)=1+\binom{n}{2}+\binom{n}{4}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
