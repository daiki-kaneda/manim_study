from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class AmplitudeOperator(PacedScene):
    """#559 振幅作用素：振動積分の振幅評価（約45秒）"""

    def construct(self):
        self.show_heading("振幅作用素")
        self.draw_wave()
        self.amp()
        self.show_formula()
        self.read(1.4)

    def draw_wave(self):
        axes = Axes(x_range=[0, 6, 1], y_range=[-1.5, 1.5, 1], x_length=6.5, y_length=2.5, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.3)
        import numpy as np
        w = axes.plot(lambda t: np.sin(3 * t) * np.exp(-0.15 * t), x_range=[0, 6], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(w), run_time=1.4)
        note = self.ja_text("振動積分", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def amp(self):
        cap = self.ja_text("振幅で抑える", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("Lp 有界へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Tf(x)=\int e^{i\lambda\phi(x,y)}a(x,y)f(y)\,dy").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
