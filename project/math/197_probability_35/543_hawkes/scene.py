from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np



class HawkesProcess(PacedScene):
    """#543 ホーケス過程：点が自分を励起する（約45秒）"""

    def construct(self):
        self.show_heading("ホーケス過程")
        self.draw_intensity()
        self.spikes()
        self.show_formula()
        self.read(1.4)

    def draw_intensity(self):
        axes = Axes(x_range=[0, 6, 1], y_range=[0, 2.5, 1], x_length=6.5, y_length=2.5, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.4)
        base = axes.plot(lambda t: 0.4, x_range=[0, 6], color=GREY, stroke_width=2)
        bumps = axes.plot(
            lambda t: 0.4 + 1.2 * np.exp(-1.5 * max(t - 1.2, 0)) + 0.9 * np.exp(-1.5 * max(t - 3.0, 0)),
            x_range=[0, 6], color=BLUE, stroke_width=4,
        )
        self.play(Create(axes), Create(base), Create(bumps), run_time=1.5)
        note = self.ja_text("励起で跳ねる", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def spikes(self):
        dots = VGroup(*[Dot(self.axes.c2p(x, 0), color=YELLOW, radius=0.09) for x in [1.2, 3.0, 3.4, 5.1]])
        cap = self.ja_text("過去が未来を煽る", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("自己励起", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\lambda(t)=\mu+\sum_{t_i<t}\phi(t-t_i)").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
