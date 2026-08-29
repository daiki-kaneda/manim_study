from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class SpectralRadius(PacedScene):
    """#262 スペクトル半径は最大の |λ|（約45秒）"""

    def construct(self):
        self.O = LEFT * 0.8 + DOWN * 0.2
        self.show_heading("スペクトル半径")
        self.draw_eigenvalues()
        self.outer_circle()
        self.show_formula()
        self.read(1.4)

    def draw_eigenvalues(self):
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 2.2, self.O + UP * 2.2, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        pts = [
            self.O + RIGHT * 1.6 + UP * 0.7,
            self.O + LEFT * 0.9 + UP * 1.1,
            self.O + RIGHT * 0.4 + DOWN * 1.3,
        ]
        self.dots = VGroup(*[Dot(p, color=YELLOW, radius=0.1) for p in pts])
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in self.dots], lag_ratio=0.12), run_time=1.3)
        note = self.ja_text("固有値", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def outer_circle(self):
        # radius = max |λ|
        radii = [np.linalg.norm(d.get_center() - self.O) for d in self.dots]
        R = max(radii)
        circ = Circle(radius=R, color=ORANGE, stroke_width=4).move_to(self.O)
        cap = self.ja_text("一番外", font_size=24).move_to(self.note)
        self.play(Create(circ), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        # highlight farthest
        far = self.dots[int(np.argmax(radii))]
        self.play(Indicate(far, color=RED), run_time=0.9)
        cap2 = self.ja_text("スペクトル半径", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\rho(A)=\max_i|\lambda_i|").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
