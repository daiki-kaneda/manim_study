from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class Barycentric(PacedScene):
    """#253 重心座標は重みつき平均（約45秒）"""

    def construct(self):
        self.show_heading("重心座標")
        self.draw_triangle()
        self.move_point()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 2.9 + DOWN * 1.5
        self.B = RIGHT * 2.9 + DOWN * 1.5
        self.C = ORIGIN + UP * 2.1
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        labs = VGroup(
            MathTex("A", font_size=28).next_to(self.A, DL, buff=0.08),
            MathTex("B", font_size=28).next_to(self.B, DR, buff=0.08),
            MathTex("C", font_size=28).next_to(self.C, UP, buff=0.08),
        )
        self.play(Create(self.tri), FadeIn(labs), run_time=1.4)
        note = self.ja_text("頂点の重み", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def move_point(self):
        configs = [
            ((0.5, 0.3, 0.2), "偏る"),
            ((1 / 3, 1 / 3, 1 / 3), "重心"),
            ((0.2, 0.2, 0.6), "C 寄り"),
        ]
        p = None
        for (a, b, c), label in configs:
            pos = a * self.A + b * self.B + c * self.C
            d = Dot(pos, color=ORANGE, radius=0.11)
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            if p is None:
                self.play(FadeIn(d), Transform(self.note, cap), run_time=1.1)
                p = d
            else:
                self.play(p.animate.move_to(pos), Transform(self.note, cap), run_time=1.1)
            self.read(0.2)

    def show_formula(self):
        formula = MathTex(r"P=\alpha A+\beta B+\gamma C,\ \alpha+\beta+\gamma=1").scale(0.72)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
