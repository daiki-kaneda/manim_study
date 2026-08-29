from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class PoissonEquation(PacedScene):
    """#247 ポアソン：源がラプラスを決める（約45秒）"""

    def construct(self):
        self.show_heading("ポアソン方程式")
        self.draw_source()
        self.potential()
        self.show_formula()
        self.read(1.4)

    def draw_source(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[-0.2, 2.2, 1],
            x_length=8.0,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.15)
        rho = self.axes.plot(
            lambda x: 1.4 * math.exp(-8 * (x - 2.0) ** 2),
            x_range=[0.1, 4.0],
            color=RED,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.8)
        self.play(Create(rho), run_time=1.4)
        note = self.ja_text("源 ρ", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def potential(self):
        # smoother wider bump as potential
        u = self.axes.plot(
            lambda x: 1.5 * math.exp(-0.55 * (x - 2.0) ** 2),
            x_range=[0.1, 4.0],
            color=TEAL,
            stroke_width=5,
        )
        cap = self.ja_text("電位 u", font_size=24).move_to(self.note)
        self.play(Create(u), Transform(self.note, cap), run_time=1.6)
        self.read(0.3)
        cap2 = self.ja_text("広がってなだらか", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"-\Delta u=\rho").scale(1.2)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
