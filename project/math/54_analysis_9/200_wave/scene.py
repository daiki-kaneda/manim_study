from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class WaveEquation(PacedScene):
    """#200 波は左右に分かれて進む（約45秒）"""

    def construct(self):
        self.show_heading("波動方程式")
        self.draw_initial()
        self.propagate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def _pulse(self, center, amp=1.2, width=0.35):
        def f(x):
            return amp * math.exp(-((x - center) ** 2) / (2 * width * width)) + 0.35

        return f

    def draw_initial(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[-0.1, 2.2, 1],
            x_length=8.0,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.15)
        f0 = self._pulse(2.0)
        self.curve = self.axes.plot(f0, x_range=[0.05, 4.05], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), run_time=1.5)
        note = self.ja_text("初期", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def propagate(self):
        # d'Alembert: half left + half right
        for t, label in ((0.55, "分かれる"), (1.15, "進む")):
            def f(x, tt=t):
                return 0.5 * self._pulse(2.0 - tt, amp=1.2)(x) + 0.5 * self._pulse(2.0 + tt, amp=1.2)(x)

            new = self.axes.plot(f, x_range=[0.05, 4.05], color=TEAL if t < 1 else YELLOW, stroke_width=5)
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            self.play(Transform(self.curve, new), Transform(self.note, cap), run_time=1.55)
            self.read(0.3)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"u_{tt}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"u_{tt}=c^{2}u_{xx}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"u_{tt}=c^{2}u_{xx}").scale(1.1)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
