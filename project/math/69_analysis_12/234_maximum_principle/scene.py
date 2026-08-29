from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class MaximumPrinciple(PacedScene):
    """#234 最大値原理：最大は境界（約45秒）"""

    def construct(self):
        self.show_heading("最大値原理")
        self.draw_domain()
        self.show_max_on_boundary()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_domain(self):
        self.axes = Axes(
            x_range=[-0.2, 3.4, 1],
            y_range=[-0.2, 2.2, 1],
            x_length=7.6,
            y_length=3.1,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.25)
        # harmonic-like bump lower inside than ends
        self.curve = self.axes.plot(
            lambda x: 0.55 + 0.9 * math.sin(math.pi * (x - 0.3) / 2.8) * 0.55 + 0.15 * (x - 1.7) ** 2 / 2,
            x_range=[0.3, 3.1],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.curve), run_time=1.5)
        note = self.ja_text("領域内", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def show_max_on_boundary(self):
        a = Dot(self.axes.c2p(0.3, 0.55 + 0.15 * (0.3 - 1.7) ** 2 / 2), color=YELLOW, radius=0.1)
        # recompute endpoint values from same formula
        def f(x):
            return 0.55 + 0.9 * math.sin(math.pi * (x - 0.3) / 2.8) * 0.55 + 0.15 * (x - 1.7) ** 2 / 2

        a = Dot(self.axes.c2p(0.3, f(0.3)), color=ORANGE, radius=0.1)
        b = Dot(self.axes.c2p(3.1, f(3.1)), color=ORANGE, radius=0.1)
        # interior point lower
        mid = Dot(self.axes.c2p(1.7, f(1.7)), color=GREY_B, radius=0.08)
        cap = self.ja_text("端で大きい", font_size=24).move_to(self.note)
        self.play(FadeIn(a), FadeIn(b), FadeIn(mid), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        self.play(Indicate(a, color=YELLOW), Indicate(b, color=YELLOW), run_time=1.0)
        cap2 = self.ja_text("最大は境界", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
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
        eq = MathTex(r"\max_{\overline{\Omega}}u").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\max_{\overline{\Omega}}u=\max_{\partial\Omega}u").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\max_{\overline{\Omega}}u=\max_{\partial\Omega}u").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
