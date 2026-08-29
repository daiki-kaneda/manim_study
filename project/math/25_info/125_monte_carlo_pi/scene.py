from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class MonteCarloPi(JapaneseScene):
    """#125 モンテカルロで π（約90秒）"""

    def construct(self):
        self.show_heading("モンテカルロの π")
        self.draw_square()
        self.throw()
        self.show_formula()
        self.hold(1.2)

    def draw_square(self):
        self.o = LEFT * 2.4 + DOWN * 1.35
        self.s = 3.1
        sq = Square(side_length=self.s, color=WHITE, stroke_width=3)
        sq.move_to(self.o + RIGHT * (self.s / 2) + UP * (self.s / 2))
        circ = Circle(radius=self.s / 2, color=BLUE, stroke_width=3)
        circ.move_to(sq.get_center())
        self.play(Create(sq), Create(circ), run_time=0.75)
        self.center = sq.get_center()
        self.hold(0.35)

    def throw(self):
        rng = np.random.default_rng(7)
        n = 40
        pts = rng.uniform(-1, 1, size=(n, 2))
        dots = VGroup()
        inside = 0
        for x, y in pts:
            p = self.center + RIGHT * (x * self.s / 2) + UP * (y * self.s / 2)
            ok = x * x + y * y <= 1
            inside += int(ok)
            dots.add(Dot(p, radius=0.045, color=YELLOW if ok else GREY))
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.03), run_time=1.4)
        note = self.ja_text("円の中の割合", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.55)
        self.inside = inside

    def show_formula(self):
        formula = MathTex(r"\pi\approx 4\cdot\frac{\#\mathrm{in}}{n}").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
