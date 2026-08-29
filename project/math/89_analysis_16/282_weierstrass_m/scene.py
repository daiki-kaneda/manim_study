from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class WeierstrassMTest(PacedScene):
    """#282 ワイエルシュトラスの M 判定（約45秒）"""

    def construct(self):
        self.show_heading("ワイエルシュトラスの M 判定")
        self.draw_terms()
        self.dominate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_terms(self):
        self.waves = VGroup()
        for i, (amp, col) in enumerate([(1.1, BLUE), (0.65, TEAL), (0.35, GREY)]):
            axs = Axes(
                x_range=[0, 4, 1],
                y_range=[-1.4, 1.4, 1],
                x_length=5.2,
                y_length=1.35,
                tips=False,
                axis_config={"stroke_width": 1, "include_ticks": False},
            )
            axs.shift(UP * (1.35 - i * 1.05) + LEFT * 0.7)
            a = amp
            wave = axs.plot(
                lambda x, a=a: a * np.sin(2.5 * x) / (1 + 0.3 * x),
                x_range=[0.1, 3.9],
                color=col,
                stroke_width=3,
            )
            self.waves.add(VGroup(axs, wave))
        self.play(LaggedStart(*[Create(w[1]) for w in self.waves], lag_ratio=0.15), run_time=1.6)
        note = self.ja_text("各項の波", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def dominate(self):
        caps = VGroup(*[
            MathTex(rf"M_{{{i+1}}}", color=ORANGE, font_size=30).next_to(self.waves[i], RIGHT, buff=0.12)
            for i in range(3)
        ])
        cap = self.ja_text("上から抑える", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(c) for c in caps], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("一様収束", font_size=24).move_to(self.note)
        box = SurroundingRectangle(self.waves, color=YELLOW, buff=0.12)
        self.play(Create(box), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"|f_n|\le M_n,\ \sum M_n<\infty").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"|f_n|\le M_n,\ \sum M_n<\infty").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"|f_n|\le M_n,\ \sum M_n<\infty").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
