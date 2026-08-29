from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class ArcLength(PacedScene):
    """#126 弧長は折れ線の極限（約45秒）"""

    def construct(self):
        self.show_heading("弧長")
        self.draw_curve()
        self.refine()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _f(self, x):
        return 0.45 * np.sin(1.35 * x) + 0.22 * x + 1.15

    def draw_curve(self):
        self.axes = Axes(
            x_range=[0, 4.4, 1],
            y_range=[0, 3.4, 1],
            x_length=7.4,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.45)
        self.curve = self.axes.plot(
            lambda x: 0.45 * np.sin(1.35 * x) + 0.22 * x + 1.15,
            x_range=[0.25, 4.1],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.9)
        self.play(Create(self.curve), run_time=2.2)
        self.read(0.45)

    def _poly(self, n, color=YELLOW):
        xs = np.linspace(0.35, 3.95, n + 1)
        pts = [self.axes.c2p(x, self._f(x)) for x in xs]
        line = VMobject(color=color, stroke_width=5)
        line.set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=0.055, color=color) for p in pts])
        return VGroup(line, dots)

    def refine(self):
        note = self.ja_text("折れ線", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        current = self._poly(2)
        self.play(Create(current[0]), FadeIn(current[1]), FadeIn(note), run_time=1.6)
        self.read(0.4)
        for n, label in ((4, "もっと細く"), (8, "曲線に近づく")):
            nxt = self._poly(n)
            cap = self.ja_text(label, font_size=24).move_to(note)
            self.play(Transform(current, nxt), Transform(note, cap), run_time=1.7)
            self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"L").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"L=\int_a^b\sqrt{1+(y')^2}\,dx").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"L=\int_a^b\sqrt{1+(y')^2}\,dx").scale(0.92)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.8)
