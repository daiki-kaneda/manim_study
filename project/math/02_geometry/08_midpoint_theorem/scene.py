from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class MidpointTheorem(JapaneseScene):
    """#8 中点連結定理（約90秒）"""

    def construct(self):
        self.show_heading("中点連結定理")
        self.draw_triangle()
        self.mark_midpoints()
        self.show_parallel_and_half()
        self.hold(1.2)

    def draw_triangle(self):
        self.A = UP * 2.15
        self.B = LEFT * 3.3 + DOWN * 1.7
        self.C = RIGHT * 3.3 + DOWN * 1.7
        self.triangle = Polygon(
            self.A, self.B, self.C, color=WHITE, fill_opacity=0.08, stroke_width=2
        )
        labs = VGroup(
            MathTex("A", font_size=30).next_to(self.A, UP, buff=0.12),
            MathTex("B", font_size=30).next_to(self.B, DL, buff=0.12),
            MathTex("C", font_size=30).next_to(self.C, DR, buff=0.12),
        )
        self.play(Create(self.triangle), FadeIn(labs), run_time=1.0)
        self.hold(0.5)

    def mark_midpoints(self):
        self.M = (self.A + self.B) / 2
        self.N = (self.A + self.C) / 2
        m_dot = Dot(self.M, color=BLUE, radius=0.07)
        n_dot = Dot(self.N, color=BLUE, radius=0.07)
        lab_m = MathTex("M", color=BLUE, font_size=30).next_to(self.M, LEFT, buff=0.14)
        lab_n = MathTex("N", color=BLUE, font_size=30).next_to(self.N, RIGHT, buff=0.14)
        note = self.ja_text("AB, AC の中点", font_size=24).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(m_dot), FadeIn(n_dot), FadeIn(lab_m), FadeIn(lab_n), run_time=0.7)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.8)
        self.play(FadeOut(note), run_time=0.3)
        self.mn = Line(self.M, self.N, color=BLUE, stroke_width=4)
        self.play(Create(self.mn), run_time=0.7)
        self.hold(0.6)

    def show_parallel_and_half(self):
        bc = Line(self.B, self.C, color=ORANGE, stroke_width=4)
        self.play(Create(bc), run_time=0.6)
        para = MathTex(r"MN \parallel BC", font_size=40)
        para.to_edge(RIGHT, buff=0.6).shift(UP * 1.4)
        self.play(Write(para), run_time=0.8)
        self.hold(0.9)

        brace_mn = Brace(self.mn, DOWN, buff=0.12)
        brace_bc = Brace(bc, DOWN, buff=0.12)
        half = MathTex(r"MN = \dfrac{1}{2} BC", font_size=40)
        half.next_to(para, DOWN, aligned_edge=RIGHT, buff=0.4)
        self.play(GrowFromCenter(brace_mn), GrowFromCenter(brace_bc), run_time=0.6)
        self.play(Write(half), run_time=0.9)
        self.play(Indicate(half, color=BLUE), run_time=0.8)
        self.hold(1.3)
