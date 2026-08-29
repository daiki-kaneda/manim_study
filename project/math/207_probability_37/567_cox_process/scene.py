from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CoxProcess(PacedScene):
    """#567 コックス過程：ランダム強度のポアソン（約45秒）"""

    def construct(self):
        self.show_heading("コックス過程")
        self.draw_random_lambda()
        self.cond()
        self.show_formula()
        self.read(1.4)

    def draw_random_lambda(self):
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 2.2, 1], x_length=6.5, y_length=2.4, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.4)
        import numpy as np
        lam = axes.plot(lambda t: 0.7 + 0.5 * np.sin(1.2 * t) + 0.2 * t / 5, x_range=[0, 5], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(lam), run_time=1.4)
        note = self.ja_text("強度も確率的", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cond(self):
        cap = self.ja_text("条件付きでポアソン", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("二重確率的", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"N\mid\Lambda\sim\mathrm{Poisson}(\Lambda)").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
