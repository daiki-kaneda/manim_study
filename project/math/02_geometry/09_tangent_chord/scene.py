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


class TangentChord(JapaneseScene):
    """#9 接線と弦（約90秒）"""

    def construct(self):
        self.R = 2.0
        self.origin = LEFT * 2.2 + DOWN * 0.1
        self.show_heading("接線と弦")
        self.draw_tangent()
        self.draw_chord_and_alternate_angle()
        self.show_equality()
        self.hold(1.2)

    def _pt(self, ang):
        return self.origin + np.array(polar(self.R, ang))

    def draw_tangent(self):
        self.circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        self.T = self._pt(0)
        self.O = self.origin
        radius = Line(self.O, self.T, color=YELLOW, stroke_width=2)
        # Tangent is vertical at the rightmost point.
        tangent = Line(self.T + UP * 2.3, self.T + DOWN * 2.3, color=GREEN, stroke_width=3)
        right = RightAngle(radius, Line(self.T, self.T + UP), length=0.28, color=GREEN)
        lab_t = MathTex("T", font_size=28).next_to(self.T, RIGHT, buff=0.15)
        lab_o = MathTex("O", font_size=28).next_to(self.O, LEFT, buff=0.15)
        self.play(Create(self.circle), run_time=0.8)
        self.play(Create(radius), FadeIn(Dot(self.O, radius=0.05)), FadeIn(lab_o), FadeIn(Dot(self.T, radius=0.06)), FadeIn(lab_t), run_time=0.7)
        self.play(Create(tangent), Create(right), run_time=0.8)
        note = self.ja_text("接線 ⊥ 半径", font_size=26).to_edge(DOWN, buff=0.45)
        self.play(FadeIn(note), run_time=0.45)
        self.hold(0.9)
        self.play(FadeOut(note), run_time=0.3)
        self.tangent = tangent
        self.radius = radius

    def draw_chord_and_alternate_angle(self):
        self.A = self._pt(-55 * DEGREES)
        chord = Line(self.T, self.A, color=BLUE, stroke_width=3)
        lab_a = MathTex("A", font_size=28).next_to(self.A, DR, buff=0.12)
        self.play(Create(chord), FadeIn(Dot(self.A, radius=0.06)), FadeIn(lab_a), run_time=0.7)
        tan_down = Line(self.T, self.T + DOWN, color=GREEN)
        ang_tan = Angle(tan_down, Line(self.T, self.A), radius=0.4, color=BLUE)
        lab1 = MathTex(r"\alpha", color=BLUE, font_size=30).next_to(ang_tan, DOWN, buff=0.1)
        self.play(Create(ang_tan), FadeIn(lab1), run_time=0.6)
        self.hold(0.7)

        self.C = self._pt(125 * DEGREES)
        ca = Line(self.C, self.A, color=ORANGE, stroke_width=2)
        ct = Line(self.C, self.T, color=ORANGE, stroke_width=2)
        ang_ins = Angle(ca, ct, radius=0.38, color=ORANGE)
        lab2 = MathTex(r"\alpha", color=ORANGE, font_size=30).next_to(ang_ins, DOWN, buff=0.08)
        lab_c = MathTex("C", font_size=28).next_to(self.C, UL, buff=0.12)
        self.play(Create(ca), Create(ct), FadeIn(Dot(self.C, radius=0.06)), FadeIn(lab_c), run_time=0.8)
        self.play(Create(ang_ins), FadeIn(lab2), run_time=0.6)
        self.hold(0.9)

    def show_equality(self):
        eq = VGroup(
            self.ja_text("接線と弦のなす角", font_size=24),
            MathTex(r"=").scale(0.9),
            self.ja_text("交互の円周角", font_size=24),
        ).arrange(RIGHT, buff=0.15)
        eq.to_edge(DOWN, buff=0.4)
        self.play(Write(eq), run_time=1.0)
        self.play(Indicate(eq, color=BLUE), run_time=0.8)
        self.hold(1.3)
