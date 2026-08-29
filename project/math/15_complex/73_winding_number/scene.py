from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import polar


class WindingNumber(JapaneseScene):
    """#73 回転数（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.3 + DOWN * 0.05
        self.show_heading("回転数")
        self.draw_around()
        self.draw_not_around()
        self.show_formula()
        self.hold(1.2)

    def draw_around(self):
        z0 = Dot(self.origin, color=YELLOW, radius=0.08)
        lab0 = MathTex("0", color=YELLOW, font_size=26).next_to(z0, DL, buff=0.08)
        curve = Circle(radius=1.35, color=BLUE, stroke_width=4).move_to(self.origin)
        self.play(FadeIn(z0), FadeIn(lab0), Create(curve), run_time=0.8)
        n1 = MathTex(r"n=1", color=BLUE, font_size=32).to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(n1), run_time=0.35)
        self.hold(0.6)
        self.curve, self.n1, self.z0 = curve, n1, z0

    def draw_not_around(self):
        other = Circle(radius=0.85, color=ORANGE, stroke_width=4).move_to(self.origin + RIGHT * 3.15 + UP * 0.4)
        self.play(Create(other), run_time=0.7)
        n0 = MathTex(r"n=0", color=ORANGE, font_size=32).next_to(self.n1, DOWN, aligned_edge=RIGHT, buff=0.25)
        self.play(FadeIn(n0), run_time=0.35)
        note = self.ja_text("原点を何回囲むか", font_size=24)
        note.next_to(n0, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"n(\gamma,0)=\frac{1}{2\pi i}\oint\frac{dz}{z}").scale(0.9)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
