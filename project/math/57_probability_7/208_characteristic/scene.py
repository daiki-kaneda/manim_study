from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class CharacteristicFunction(PacedScene):
    """#208 特性関数は密度のフーリエ（約45秒）"""

    def construct(self):
        self.show_heading("特性関数")
        self.draw_density()
        self.show_transform()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_density(self):
        self.axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[0, 0.55, 0.5],
            x_length=7.2,
            y_length=2.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.55 + LEFT * 0.25)
        self.pdf = self.axes.plot(
            lambda x: 0.4 * math.exp(-0.5 * x * x),
            x_range=[-3.0, 3.0],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.pdf), run_time=1.5)
        note = self.ja_text("密度", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def show_transform(self):
        # characteristic of N(0,1) is e^{-t^2/2}
        ax2 = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[0, 1.15, 1],
            x_length=7.2,
            y_length=1.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 1.55 + LEFT * 0.25)
        phi = ax2.plot(lambda t: math.exp(-0.5 * t * t), x_range=[-3.0, 3.0], color=YELLOW, stroke_width=5)
        self.play(Create(ax2), run_time=0.7)
        cap = self.ja_text("振幅", font_size=24).move_to(self.note)
        self.play(Create(phi), Transform(self.note, cap), run_time=1.6)
        self.read(0.35)
        # oscillating overlay hint
        wave = self.axes.plot(
            lambda x: 0.4 * math.exp(-0.5 * x * x) * (0.5 + 0.5 * math.cos(3.5 * x)),
            x_range=[-3.0, 3.0],
            color=ORANGE,
            stroke_width=3,
        )
        cap2 = self.ja_text("振動して積分", font_size=24).move_to(self.note)
        self.play(Create(wave), Transform(self.note, cap2), run_time=1.4)
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
        eq = MathTex(r"\varphi(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\varphi(t)=\mathbb{E}[e^{itX}]").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\varphi(t)=\mathbb{E}[e^{itX}]").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
