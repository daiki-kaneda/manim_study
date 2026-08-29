from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class Moments(PacedScene):
    """#172 モーメントは形の要約（約45秒）"""

    def construct(self):
        self.show_heading("モーメント")
        self.draw_density()
        self.mark_moments()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_density(self):
        self.axes = Axes(
            x_range=[-3.5, 4.2, 1],
            y_range=[0, 0.55, 0.5],
            x_length=9.0,
            y_length=2.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.05)
        # slightly skewed density
        self.curve = self.axes.plot(
            lambda x: 0.45 * math.exp(-0.5 * ((x - 0.2) ** 2) / 0.9) * (1 + 0.35 * math.tanh(x)),
            x_range=[-3.0, 3.6],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), run_time=1.8)
        note = self.ja_text("分布の形", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def mark_moments(self):
        mu = self.axes.c2p(0.35, 0)
        mean = DashedLine(mu, self.axes.c2p(0.35, 0.48), color=YELLOW, stroke_width=3)
        cap = self.ja_text("平均", font_size=24).move_to(self.note)
        self.play(Create(mean), Transform(self.note, cap), run_time=1.1)
        self.read(0.3)
        # variance band
        left = self.axes.c2p(-0.7, 0)
        right = self.axes.c2p(1.4, 0)
        band = Rectangle(
            width=abs(right[0] - left[0]),
            height=abs(self.axes.c2p(0, 0.48)[1] - self.axes.c2p(0, 0)[1]),
            color=ORANGE,
            fill_opacity=0.18,
            stroke_width=2,
        )
        band.move_to([(left[0] + right[0]) / 2, (self.axes.c2p(0, 0)[1] + self.axes.c2p(0, 0.48)[1]) / 2, 0])
        cap2 = self.ja_text("広がり", font_size=24).move_to(self.note)
        self.play(FadeIn(band), Transform(self.note, cap2), run_time=1.2)
        self.read(0.3)
        # skew arrow
        skew = Arrow(self.axes.c2p(1.5, 0.2), self.axes.c2p(2.9, 0.08), buff=0, color=TEAL, stroke_width=4)
        cap3 = self.ja_text("歪み", font_size=24).move_to(self.note)
        self.play(Create(skew), Transform(self.note, cap3), run_time=1.2)
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
        eq = MathTex(r"m_k").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"m_k=\mathbb{E}[X^{k}]").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"m_k=\mathbb{E}[X^{k}]").scale(1.05)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
