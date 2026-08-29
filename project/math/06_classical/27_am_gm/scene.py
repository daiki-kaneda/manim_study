from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene


class AMGM(JapaneseScene):
    """#27 相加相乗平均（半円、約90秒）"""

    def construct(self):
        self.a = 2.5
        self.b = 1.15
        self.origin = LEFT * 3.3 + DOWN * 1.35
        self.show_heading("相加・相乗平均")
        self.draw_semicircle()
        self.compare_lengths()
        self.show_formula()
        self.hold(1.2)

    def draw_semicircle(self):
        a, b = self.a, self.b
        left = self.origin
        mid = self.origin + RIGHT * a
        right = self.origin + RIGHT * (a + b)
        diameter = Line(left, right, color=WHITE, stroke_width=3)
        center = (left + right) / 2
        R = (a + b) / 2
        arc = Arc(radius=R, start_angle=0, angle=PI, color=WHITE, stroke_width=2, arc_center=center)
        self.play(Create(diameter), run_time=0.6)
        brace_a = Brace(Line(left, mid), DOWN, buff=0.12)
        brace_b = Brace(Line(mid, right), DOWN, buff=0.12)
        lab_a = MathTex("a", font_size=32).next_to(brace_a, DOWN, buff=0.08)
        lab_b = MathTex("b", font_size=32).next_to(brace_b, DOWN, buff=0.08)
        self.play(GrowFromCenter(brace_a), GrowFromCenter(brace_b), FadeIn(lab_a), FadeIn(lab_b), run_time=0.6)
        self.play(Create(arc), run_time=0.8)
        self.hold(0.5)
        self.left, self.mid, self.right, self.center, self.R = left, mid, right, center, R

    def compare_lengths(self):
        height = np.sqrt(self.a * self.b)
        top = np.array([self.mid[0], self.origin[1] + height, 0.0])
        # 半円上の点（タレス: 直径に対する円周角が直角）
        # 接合点から垂直に上げた線が半円と交わる高さが √(ab)
        vert = Line(self.mid, top, color=GREEN, stroke_width=4)
        radius = Line(self.center, self.center + UP * self.R, color=ORANGE, stroke_width=4)
        geo = Dot(top, color=GREEN, radius=0.07)
        am = Dot(self.center + UP * self.R, color=ORANGE, radius=0.07)
        self.play(Create(vert), FadeIn(geo), run_time=0.7)
        gm_lab = MathTex(r"\sqrt{ab}", color=GREEN, font_size=32)
        gm_lab.next_to(vert, RIGHT, buff=0.12)
        self.play(FadeIn(gm_lab), run_time=0.4)
        self.hold(0.6)
        self.play(Create(radius), FadeIn(am), run_time=0.7)
        am_lab = MathTex(r"\dfrac{a+b}{2}", color=ORANGE, font_size=32)
        am_lab.next_to(radius, LEFT, buff=0.12)
        self.play(FadeIn(am_lab), run_time=0.4)
        self.hold(0.8)
        note = self.ja_text("半径の方が長い（または等しい）", font_size=26)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.6)
        self.play(FadeIn(note), run_time=0.45)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\frac{a+b}{2}\ge\sqrt{ab}\quad(a,b>0)").scale(1.05)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        eq = self.ja_text("等号は a=b のとき", font_size=24)
        eq.next_to(formula, UP, buff=0.18)
        self.play(FadeIn(eq), run_time=0.4)
        self.play(Indicate(formula, color=ORANGE), run_time=0.7)
        self.hold(1.2)
