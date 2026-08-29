from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class StoppingTime(PacedScene):
    """#244 停止時刻は今までの情報で決まる（約45秒）"""

    def construct(self):
        self.show_heading("停止時刻")
        self.draw_walk()
        self.hit_barrier()
        self.show_formula()
        self.read(1.4)

    def draw_walk(self):
        self.axes = Axes(
            x_range=[0, 10.5, 1],
            y_range=[-2.2, 2.5, 1],
            x_length=8.2,
            y_length=3.2,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.1 + LEFT * 0.1)
        self.play(Create(self.axes), run_time=0.8)
        rng = np.random.default_rng(4)
        y = 0.0
        pts = [self.axes.c2p(0, 0)]
        self.path_y = [0.0]
        for t in range(1, 11):
            y += rng.choice([-0.55, 0.45, 0.35, -0.4])
            y = float(np.clip(y, -1.8, 2.0))
            self.path_y.append(y)
            pts.append(self.axes.c2p(t, y))
        self.walk = VMobject(color=BLUE, stroke_width=4)
        self.walk.set_points_as_corners(pts)
        self.play(Create(self.walk), run_time=1.8)
        note = self.ja_text("経路", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def hit_barrier(self):
        barrier = DashedLine(self.axes.c2p(0, 1.2), self.axes.c2p(10, 1.2), color=ORANGE, stroke_width=3)
        self.play(Create(barrier), run_time=0.8)
        # find first hit
        tau = None
        for t, y in enumerate(self.path_y):
            if y >= 1.2:
                tau = t
                break
        if tau is None:
            tau = len(self.path_y) - 1
        hit = Dot(self.axes.c2p(tau, self.path_y[tau]), color=RED, radius=0.11)
        cap = self.ja_text("当たって停止", font_size=24).move_to(self.note)
        self.play(FadeIn(hit, scale=0.5), Transform(self.note, cap), run_time=1.2)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"\{\tau\le n\}\in\mathcal{F}_n").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
