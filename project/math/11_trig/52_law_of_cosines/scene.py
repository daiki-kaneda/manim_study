from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class LawOfCosines(JapaneseScene):
    """#52 余弦定理（約90秒）"""

    def construct(self):
        self.show_heading("余弦定理")
        self.draw_triangle()
        self.show_right_case()
        self.show_formula()
        self.hold(1.2)

    def draw_triangle(self):
        self.C = LEFT * 2.8 + DOWN * 1.35
        self.B = RIGHT * 0.9 + DOWN * 1.35
        self.A = LEFT * 1.3 + UP * 1.55
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=0.7)
        lab_c = MathTex("c", color=YELLOW, font_size=32).move_to((self.A + self.B) / 2 + UR * 0.18)
        lab_a = MathTex("a", font_size=30).move_to((self.B + self.C) / 2 + DOWN * 0.28)
        lab_b = MathTex("b", font_size=30).move_to((self.A + self.C) / 2 + LEFT * 0.28)
        ang = Angle.from_three_points(self.A, self.C, self.B, radius=0.38, color=ORANGE)
        g = MathTex(r"\gamma", color=ORANGE, font_size=30).next_to(ang, UR, buff=0.08)
        self.play(FadeIn(lab_a), FadeIn(lab_b), FadeIn(lab_c), Create(ang), FadeIn(g), run_time=0.7)
        self.hold(0.55)
        self.lab_c = lab_c

    def show_right_case(self):
        note = self.ja_text("γ=90° なら三平方", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.6)
        self.play(FadeIn(note), run_time=0.4)
        pyth = MathTex(r"c^2=a^2+b^2", font_size=34).next_to(note, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(pyth), run_time=0.45)
        self.hold(0.7)
        fix = self.ja_text("鋭角・鈍角は補正項", font_size=24).move_to(note)
        self.play(Transform(note, fix), FadeOut(pyth), run_time=0.45)
        self.hold(0.55)

    def show_formula(self):
        formula = MathTex(r"c^2=a^2+b^2-2ab\cos\gamma").scale(0.95)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
