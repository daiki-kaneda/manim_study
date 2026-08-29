from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class SpectralMeasure(PacedScene):
    """#402 スペクトル測度：射影値測度で作用素を積分（約45秒）"""

    def construct(self):
        self.show_heading("スペクトル測度")
        self.draw_line()
        self.projections()
        self.show_formula()
        self.read(1.4)

    def draw_line(self):
        self.O = LEFT * 0.2 + DOWN * 0.1
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        band = Line(self.O + RIGHT * (-1.5), self.O + RIGHT * 2.2, color=ORANGE, stroke_width=10)
        self.play(Create(ax), Create(band), run_time=1.3)
        note = self.ja_text("スペクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.band = band
        self.O = self.O

    def projections(self):
        boxes = VGroup(*[
            Square(side_length=0.7, color=BLUE, stroke_width=2).shift(LEFT * 2.0 + RIGHT * i * 1.0 + UP * 1.2)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"E", font_size=26).move_to(b) for b in boxes])
        cap = self.ja_text("射影の族", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("積分で作用素", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A=\int \lambda\,dE(\lambda)").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
