from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np

class PoissonPointProcess(PacedScene):
    """#448 ポアソン点過程：独立な点の雲（約45秒）"""

    def construct(self):
        self.show_heading("ポアソン点過程")
        self.draw_points()
        self.intensity()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        import numpy as np
        rng = np.random.default_rng(11)
        box = Rectangle(width=6.5, height=3.2, color=GREY, stroke_width=2).shift(UP * 0.2)
        pts = VGroup(*[
            Dot(LEFT * 2.8 + RIGHT * rng.random() * 5.6 + DOWN * 1.2 + UP * rng.random() * 2.8,
                color=ORANGE, radius=0.07)
            for _ in range(18)
        ])
        self.play(Create(box), LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.04), run_time=1.6)
        note = self.ja_text("ランダムな点", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def intensity(self):
        cap = self.ja_text("強度 λ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("領域は独立", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"N(A)\sim\mathrm{Poisson}(\lambda|A|)").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
