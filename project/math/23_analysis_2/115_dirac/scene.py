from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class DiracDelta(JapaneseScene):
    """#115 デルタ関数（約90秒）"""

    def construct(self):
        self.show_heading("デルタ関数")
        self.narrow()
        self.show_formula()
        self.hold(1.2)

    def narrow(self):
        self.axes = Axes(
            x_range=[-3.2, 3.2, 1],
            y_range=[0, 3.4, 1],
            x_length=8.4,
            y_length=3.5,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15)
        self.play(Create(self.axes), run_time=0.4)
        note = self.ja_text("幅が広い", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        current = None
        for n, cap in ((1.0, "幅が広い"), (2.2, "細くなる"), (4.5, "面積は 1")):
            graph = self.axes.plot(
                lambda x, k=n: k * math.exp(-k * k * x * x) / math.sqrt(math.pi),
                x_range=[-3.0, 3.0],
                color=YELLOW,
                stroke_width=5,
            )
            nxt = self.ja_text(cap, font_size=24).move_to(note)
            if current is None:
                self.play(Create(graph), FadeIn(note), run_time=0.75)
                current = graph
            else:
                self.play(Transform(current, graph), Transform(note, nxt), run_time=0.75)
            self.hold(0.4)

    def show_formula(self):
        formula = MathTex(r"\int_{-\infty}^{\infty}\delta(x)\,dx=1").scale(0.95)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
