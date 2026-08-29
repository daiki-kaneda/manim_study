from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class PoissonProcess(PacedScene):
    """#255 ポアソン過程は一定強度の点過程（約45秒）"""

    def construct(self):
        self.show_heading("ポアソン過程")
        self.draw_axis()
        self.place_events()
        self.show_formula()
        self.read(1.4)

    def draw_axis(self):
        self.axis = NumberLine(x_range=[0, 10, 1], length=9.0, include_numbers=False, stroke_width=3)
        self.axis.shift(DOWN * 0.2)
        self.play(Create(self.axis), run_time=1.0)
        note = self.ja_text("時間", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def place_events(self):
        rng = np.random.default_rng(8)
        times = np.cumsum(rng.exponential(1.1, size=8))
        times = times[times < 9.5]
        dots = VGroup()
        for t in times:
            d = Dot(self.axis.n2p(float(t)), color=ORANGE, radius=0.1)
            dots.add(d)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.12), run_time=1.8)
        cap = self.ja_text("出来事", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.3)
        # highlight a window
        a, b = 2.0, 5.0
        band = Line(self.axis.n2p(a), self.axis.n2p(b), color=TEAL, stroke_width=8)
        band.set_opacity(0.5)
        cap2 = self.ja_text("区間の個数", font_size=24).move_to(self.note)
        self.play(Create(band), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"N(t)\sim\mathrm{Poisson}(\lambda t)").scale(0.9)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
