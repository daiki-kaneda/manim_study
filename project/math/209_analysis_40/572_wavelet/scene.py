from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Wavelet(PacedScene):
    """#572 ウェーブレット：拡縮と平行移動の基底（約45秒）"""

    def construct(self):
        self.show_heading("ウェーブレット")
        self.draw_mother()
        self.dilate()
        self.show_formula()
        self.read(1.4)

    def draw_mother(self):
        axes = Axes(x_range=[-3, 3, 1], y_range=[-1.2, 1.2, 1], x_length=6.5, y_length=2.4, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35)
        import numpy as np
        psi = axes.plot(lambda x: np.exp(-x * x) * (1 - 2 * x * x), x_range=[-2.8, 2.8], color=BLUE, stroke_width=4)
        self.play(Create(axes), Create(psi), run_time=1.4)
        note = self.ja_text("母ウェーブレット", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def dilate(self):
        import numpy as np
        psi2 = self.axes.plot(lambda x: np.exp(-(2 * x) ** 2) * (1 - 2 * (2 * x) ** 2) * np.sqrt(2),
                              x_range=[-1.5, 1.5], color=ORANGE, stroke_width=3)
        cap = self.ja_text("拡縮・平行移動", font_size=24).move_to(self.note)
        self.play(Create(psi2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("多重解像度", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\psi_{j,k}(x)=2^{j/2}\psi(2^j x-k)").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
