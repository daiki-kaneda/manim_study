from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Covariance(PacedScene):
    """#195 共分散は一緒に動く度合い（約45秒）"""

    def construct(self):
        self.show_heading("共分散")
        self.draw_scatter()
        self.show_ellipse()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_scatter(self):
        self.axes = Axes(
            x_range=[-0.3, 4.2, 1],
            y_range=[-0.3, 3.2, 1],
            x_length=7.2,
            y_length=3.3,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.1 + LEFT * 0.35)
        self.play(Create(self.axes), run_time=0.85)
        rng = np.random.default_rng(7)
        pts = []
        for _ in range(28):
            x = rng.normal(2.0, 0.7)
            y = 0.55 * x + 0.7 + rng.normal(0, 0.35)
            x = float(np.clip(x, 0.3, 3.9))
            y = float(np.clip(y, 0.3, 2.9))
            pts.append(Dot(self.axes.c2p(x, y), radius=0.055, color=BLUE))
        self.dots = VGroup(*pts)
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.dots], lag_ratio=0.04), run_time=1.8)
        note = self.ja_text("散布", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def show_ellipse(self):
        ell = Ellipse(width=3.6, height=1.55, color=ORANGE, stroke_width=4)
        ell.rotate(0.45)
        ell.move_to(self.axes.c2p(2.0, 1.75))
        cap = self.ja_text("一緒に動く", font_size=24).move_to(self.note)
        self.play(Create(ell), Transform(self.note, cap), run_time=1.5)
        self.read(0.35)
        # mean cross
        mx = DashedLine(self.axes.c2p(2.0, 0.2), self.axes.c2p(2.0, 2.9), color=GREY_B, stroke_width=2)
        my = DashedLine(self.axes.c2p(0.3, 1.75), self.axes.c2p(3.9, 1.75), color=GREY_B, stroke_width=2)
        cap2 = self.ja_text("正の相関", font_size=24).move_to(self.note)
        self.play(Create(mx), Create(my), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"\mathrm{Cov}(X,Y)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{Cov}(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{Cov}(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
