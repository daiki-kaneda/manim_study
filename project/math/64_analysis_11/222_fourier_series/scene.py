from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class FourierSeries(PacedScene):
    """#222 フーリエ級数は正弦の重ね合わせ（約45秒）"""

    def construct(self):
        self.show_heading("フーリエ級数")
        self.draw_target()
        self.add_harmonics()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_target(self):
        self.axes = Axes(
            x_range=[-0.2, 6.5, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=8.2,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.1)

        def square(x):
            t = x % (2 * math.pi)
            return 1.0 if t < math.pi else -1.0

        self.target = self.axes.plot(square, x_range=[0.05, 6.2], color=GREY_B, stroke_width=3)
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(self.target), run_time=1.3)
        note = self.ja_text("矩形波", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def add_harmonics(self):
        def partial(n_terms):
            def f(x):
                s = 0.0
                for k in range(n_terms):
                    n = 2 * k + 1
                    s += (4 / (math.pi * n)) * math.sin(n * x)
                return s
            return f

        curve = None
        for n_terms, label, col in ((1, "1 項", BLUE), (3, "3 項", TEAL), (8, "近づく", YELLOW)):
            new = self.axes.plot(partial(n_terms), x_range=[0.05, 6.2], color=col, stroke_width=4)
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            if curve is None:
                self.play(Create(new), Transform(self.note, cap), run_time=1.3)
                curve = new
            else:
                self.play(Transform(curve, new), Transform(self.note, cap), run_time=1.35)
            self.read(0.25)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"f(x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"f(x)=\sum_n (a_n\cos nx+b_n\sin nx)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"f(x)=\sum_n (a_n\cos nx+b_n\sin nx)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
