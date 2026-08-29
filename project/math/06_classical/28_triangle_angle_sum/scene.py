from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class TriangleAngleSum(JapaneseScene):
    """#28 三角形の内角の和は 180°（約90秒）"""

    def construct(self):
        self.show_heading("内角の和")
        self.draw_triangle()
        self.draw_parallel()
        self.show_formula()
        self.hold(1.2)

    def draw_triangle(self):
        a = LEFT * 2.8 + DOWN * 1.5
        b = RIGHT * 1.6 + DOWN * 1.5
        c = LEFT * 0.5 + UP * 1.55
        tri = Polygon(a, b, c, color=WHITE, stroke_width=3)
        self.play(Create(tri), run_time=0.8)
        # 内角の弧
        ang_a = Angle.from_three_points(b, a, c, radius=0.38, color=BLUE)
        ang_b = Angle.from_three_points(c, b, a, radius=0.38, color=GREEN)
        ang_c = Angle.from_three_points(a, c, b, radius=0.42, color=ORANGE)
        la = MathTex(r"\alpha", color=BLUE, font_size=32).next_to(ang_a, UR, buff=0.08)
        lb = MathTex(r"\beta", color=GREEN, font_size=32).next_to(ang_b, UL, buff=0.08)
        lc = MathTex(r"\gamma", color=ORANGE, font_size=32).next_to(ang_c, DOWN, buff=0.12)
        self.play(Create(ang_a), Create(ang_b), Create(ang_c), FadeIn(la), FadeIn(lb), FadeIn(lc), run_time=0.9)
        self.hold(0.6)
        self.a, self.b, self.c = a, b, c
        self.la, self.lb, self.lc = la, lb, lc

    def draw_parallel(self):
        # C を通り AB に平行な直線
        direction = self.b - self.a
        direction = direction / np.linalg.norm(direction)
        p1 = self.c - direction * 2.6
        p2 = self.c + direction * 2.4
        para = Line(p1, p2, color=GREY, stroke_width=2)
        self.play(Create(para), run_time=0.7)
        note = self.ja_text("頂点を通り底辺に平行", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.5)

        # 錯角: 左に α、右に β
        left_ang = Angle.from_three_points(p1, self.c, self.a, radius=0.4, color=BLUE)
        right_ang = Angle.from_three_points(self.b, self.c, p2, radius=0.4, color=GREEN)
        la2 = MathTex(r"\alpha", color=BLUE, font_size=30).next_to(left_ang, LEFT, buff=0.1)
        lb2 = MathTex(r"\beta", color=GREEN, font_size=30).next_to(right_ang, RIGHT, buff=0.1)
        self.play(Create(left_ang), FadeIn(la2), run_time=0.55)
        alt = self.ja_text("錯角", font_size=24).next_to(note, DOWN, buff=0.3)
        self.play(FadeIn(alt), run_time=0.35)
        self.hold(0.45)
        self.play(Create(right_ang), FadeIn(lb2), run_time=0.55)
        self.hold(0.7)
        straight = self.ja_text("一直線上に α+γ+β", font_size=26)
        straight.next_to(alt, DOWN, buff=0.3)
        self.play(FadeIn(straight), run_time=0.45)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"\alpha+\beta+\gamma=180^\circ").scale(1.15)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
        self.hold(1.2)
