from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class MeanValueProperty(PacedScene):
    """#246 調和関数は円周平均＝中心（約45秒）"""

    def construct(self):
        self.show_heading("平均値の性質")
        self.draw_disk()
        self.average_circle()
        self.show_formula()
        self.read(1.4)

    def draw_disk(self):
        self.O = LEFT * 0.4 + DOWN * 0.1
        self.R = 2.0
        disk = Circle(radius=self.R, color=BLUE, stroke_width=3, fill_opacity=0.15).move_to(self.O)
        self.play(Create(disk), run_time=1.2)
        self.center = Dot(self.O, color=YELLOW, radius=0.1)
        self.play(FadeIn(self.center), run_time=0.5)
        note = self.ja_text("中心の値", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def average_circle(self):
        samples = VGroup()
        for i in range(12):
            ang = i * TAU / 12
            p = self.O + self.R * np.array([np.cos(ang), np.sin(ang), 0])
            samples.add(Dot(p, radius=0.07, color=TEAL))
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in samples], lag_ratio=0.06), run_time=1.5)
        cap = self.ja_text("円周の平均", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.6)
        self.read(0.3)
        # arrows toward center
        arrows = VGroup()
        for d in samples[::3]:
            arrows.add(Arrow(d.get_center(), self.O, buff=0.12, color=ORANGE, stroke_width=3, max_tip_length_to_length_ratio=0.2))
        cap2 = self.ja_text("等しい", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.12), Transform(self.note, cap2), run_time=1.4)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"u(x)=\frac{1}{|\partial B|}\int_{\partial B}u").scale(0.78)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
