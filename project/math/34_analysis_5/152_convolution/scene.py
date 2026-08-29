from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Convolution(PacedScene):
    """#152 畳み込みはずらしながら重ねる（約50秒）"""

    def construct(self):
        self.show_heading("畳み込み")
        self.draw_bumps()
        self.slide()
        self.show_formula()
        self.read(1.4)

    def draw_bumps(self):
        self.axes = Axes(
            x_range=[-4.2, 4.2, 1],
            y_range=[0, 1.5, 1],
            x_length=9.2,
            y_length=2.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.05)
        self.f = self.axes.plot(
            lambda x: max(0.0, 1.0 - abs(x)),
            x_range=[-1.05, 1.05],
            color=BLUE,
            stroke_width=5,
        )
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.f), run_time=1.4)
        note = self.ja_text("山をずらす", font_size=24)
        note.to_edge(RIGHT, buff=0.3).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def _g(self, shift):
        return self.axes.plot(
            lambda x, s=shift: 0.85 if abs(x - s) < 0.7 else 0.0,
            x_range=[shift - 0.72, shift + 0.72],
            color=YELLOW,
            stroke_width=5,
        )

    def _overlap(self, shift):
        xs = np.linspace(-1.0, 1.0, 28)
        tops, bots = [], []
        for x in xs:
            y = min(max(0.0, 1.0 - abs(x)), 0.85 if abs(x - shift) < 0.7 else 0.0)
            if y > 0.02:
                tops.append(self.axes.c2p(x, y))
                bots.append(self.axes.c2p(x, 0))
        if len(tops) < 2:
            z = self.axes.c2p(shift, 0)
            return Polygon(z, z + RIGHT * 0.02, z + UP * 0.02, fill_opacity=0, stroke_width=0)
        return Polygon(*tops, *reversed(bots), color=TEAL, fill_opacity=0.45, stroke_width=0)

    def slide(self):
        g = self._g(-2.4)
        ov = self._overlap(-2.4)
        self.play(Create(g), FadeIn(ov), run_time=1.2)
        self.read(0.3)
        for s, label in ((-0.9, "重なり始め"), (0.15, "ピーク"), (1.6, "離れていく")):
            ng = self._g(s)
            nov = self._overlap(s)
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            self.play(Transform(g, ng), Transform(ov, nov), Transform(self.note, cap), run_time=1.35)
            self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"(f*g)(t)=\int f(\tau)g(t-\tau)\,d\tau").scale(0.78)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=2.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
