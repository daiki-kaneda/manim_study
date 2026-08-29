from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Substitution(PacedScene):
    """#138 置換積分は合成の逆（約50秒）"""

    def construct(self):
        self.show_heading("置換積分")
        self.draw_chirp()
        self.mark_inner()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_chirp(self):
        self.axes = Axes(
            x_range=[0, 2.55, 1],
            y_range=[-1.35, 1.35, 1],
            x_length=7.2,
            y_length=3.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.12 + LEFT * 0.45)
        self.curve = self.axes.plot(
            lambda x: np.sin(x * x),
            x_range=[0.05, 2.35],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.9)
        self.play(Create(self.curve), run_time=2.4)
        note = self.ja_text("だんだん密", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note

    def mark_inner(self):
        dots = VGroup()
        for x in (0.7, 1.15, 1.5, 1.8, 2.05):
            dots.add(Dot(self.axes.c2p(x, np.sin(x * x)), radius=0.06, color=YELLOW))
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.18), run_time=1.8)
        cap = self.ja_text("内側は二乗", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.8)
        self.read(0.4)
        inner = MathTex(r"u=x^{2}", font_size=36, color=YELLOW)
        inner.next_to(self.axes, UP, buff=0.08).shift(RIGHT * 1.6)
        self.play(FadeIn(inner, shift=UP * 0.15), run_time=0.7)
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
        eq = MathTex(r"\int f(g(x))g'(x)\,dx").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\int f(g(x))g'(x)\,dx=f(g(x))+C").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\int f(g(x))g'(x)\,dx=f(g(x))+C").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.1)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
