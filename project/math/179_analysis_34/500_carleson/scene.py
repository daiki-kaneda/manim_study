from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np



class CarlesonTheorem(PacedScene):
    """#500 カールソンの定理：フーリエ級数は点収束（約45秒）"""

    def construct(self):
        self.show_heading("カールソンの定理")
        self.draw_series()
        self.almost()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_series(self):
        axes = Axes(
            x_range=[-3.2, 3.2, 1], y_range=[-1.4, 1.4, 1],
            x_length=7.0, y_length=2.8, tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.25)
        wave = axes.plot(lambda x: 0.7 * np.sin(2 * x) + 0.25 * np.sin(5 * x), x_range=[-3, 3], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(wave), run_time=1.4)
        note = self.ja_text("フーリエ級数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def almost(self):
        dots = VGroup(*[Dot(LEFT * 2.5 + RIGHT * i * 1.2 + DOWN * 1.0, color=YELLOW, radius=0.08) for i in range(5)])
        cap = self.ja_text("ほとんど至るところ", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("L2 で収束", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"S_N f(x)\to f(x)\ \text{a.e.}\ (f\in L^2)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S_N f(x)\to f(x)\ \text{a.e.}\ (f\in L^2)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S_N f(x)\to f(x)\ \text{a.e.}\ (f\in L^2)").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
