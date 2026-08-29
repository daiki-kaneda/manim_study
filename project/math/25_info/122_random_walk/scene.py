from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class RandomWalk(JapaneseScene):
    """#122 ランダムウォーク（約90秒）"""

    def construct(self):
        self.origin = LEFT * 3.3 + DOWN * 0.2
        self.show_heading("ランダムウォーク")
        self.walk()
        self.show_formula()
        self.hold(1.2)

    def walk(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 6.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 2.0, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.4)
        rng = np.random.default_rng(3)
        steps = rng.choice([-1, 1], size=28)
        pts = [self.origin.copy()]
        y = 0.0
        for i, s in enumerate(steps):
            y += 0.18 * s
            pts.append(self.origin + RIGHT * (0.2 * (i + 1)) + UP * y)
        path = VMobject(color=YELLOW, stroke_width=4)
        path.set_points_as_corners(pts)
        self.play(Create(path), run_time=1.6)
        note = self.ja_text("広がりはゆるい", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.55)

    def show_formula(self):
        formula = MathTex(r"\mathbb{E}|S_n|\sim\sqrt{n}").scale(1.1)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
