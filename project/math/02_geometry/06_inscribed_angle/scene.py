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


class InscribedAngle(JapaneseScene):
    """#6 円周角の定理（約90秒）"""

    def construct(self):
        self.R = 2.05
        self.origin = LEFT * 2.3 + DOWN * 0.15
        self.a_ang = 205 * DEGREES
        self.b_ang = -25 * DEGREES
        self.title = self.show_heading("円周角の定理")
        self.draw_circle_and_chord()
        self.show_central_angle()
        self.show_inscribed_angles()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_circle_and_chord(self):
        self.circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        self.A = self._pt(self.a_ang)
        self.B = self._pt(self.b_ang)
        self.dot_a = Dot(self.A, radius=0.06)
        self.dot_b = Dot(self.B, radius=0.06)
        self.lab_a = MathTex("A", font_size=28).next_to(self.A, DL, buff=0.12)
        self.lab_b = MathTex("B", font_size=28).next_to(self.B, DR, buff=0.12)
        chord = Line(self.A, self.B, color=GREY_B, stroke_width=2)
        self.play(Create(self.circle), run_time=0.8)
        self.play(Create(chord), FadeIn(self.dot_a), FadeIn(self.dot_b), FadeIn(self.lab_a), FadeIn(self.lab_b), run_time=0.7)
        self.hold(0.5)

    def show_central_angle(self):
        o = Dot(self.origin, color=YELLOW, radius=0.06)
        lab_o = MathTex("O", font_size=28).next_to(self.origin, LEFT, buff=0.15)
        oa = Line(self.origin, self.A, color=YELLOW, stroke_width=2)
        ob = Line(self.origin, self.B, color=YELLOW, stroke_width=2)
        central = Angle(oa, ob, radius=0.42, color=YELLOW)
        a = self.a_ang
        b = self.b_ang + (TAU if self.b_ang < self.a_ang else 0)
        mid = (a + b) / 2
        two_theta = MathTex(r"2\theta", color=YELLOW, font_size=32).move_to(
            self.origin + 0.75 * np.array(polar(1, mid))
        )
        self.play(FadeIn(o), FadeIn(lab_o), Create(oa), Create(ob), run_time=0.8)
        self.play(Create(central), FadeIn(two_theta), run_time=0.6)
        self.hold(0.9)
        self.central_group = VGroup(o, lab_o, oa, ob, central, two_theta)

    def _inscribed(self, p_ang, color=BLUE):
        p = self._pt(p_ang)
        pa = Line(p, self.A, color=color, stroke_width=2)
        pb = Line(p, self.B, color=color, stroke_width=2)
        ang = Angle(pa, pb, radius=0.38, color=color)
        theta = MathTex(r"\theta", color=color, font_size=30).next_to(ang, DOWN, buff=0.08)
        dot = Dot(p, color=color, radius=0.06)
        lab = MathTex("P", color=color, font_size=28).next_to(p, UP, buff=0.12)
        return VGroup(pa, pb, ang, theta, dot, lab)

    def show_inscribed_angles(self):
        fig = self._inscribed(90 * DEGREES)
        self.play(Create(fig), run_time=1.0)
        self.hold(0.8)
        for ang in (140 * DEGREES, 55 * DEGREES):
            nxt = self._inscribed(ang)
            self.play(Transform(fig, nxt), run_time=1.1)
            self.hold(0.7)
        note = self.ja_text("P を動かしても角は同じ", font_size=24)
        note.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(note), run_time=0.5)
        self.hold(0.9)
        self.play(FadeOut(note), run_time=0.3)
        self.inscribed = fig

    def show_formula(self):
        formula = VGroup(
            self.ja_text("円周角", font_size=28),
            MathTex(r"=").scale(0.9),
            self.ja_text("中心角", font_size=28),
            MathTex(r"/\,2").scale(0.9),
        ).arrange(RIGHT, buff=0.15)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.0)
        half = MathTex(r"\theta = \frac{2\theta}{2}", font_size=36)
        half.next_to(self.title, DOWN, buff=0.3).to_edge(RIGHT, buff=0.7)
        self.play(FadeIn(half), run_time=0.7)
        self.play(Indicate(formula, color=BLUE), run_time=0.7)
        self.hold(1.3)
