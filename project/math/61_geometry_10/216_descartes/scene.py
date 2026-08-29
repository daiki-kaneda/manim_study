from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class DescartesCircle(PacedScene):
    """#216 デカルト：曲率は根号つきの和（約45秒）"""

    def construct(self):
        self.show_heading("デカルトの円定理")
        self.draw_three()
        self.fourth()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_three(self):
        # three mutually tangent equal circles (centers form equilateral of side 2R)
        R = 1.15
        h = np.sqrt(3) * R
        self.c1 = Circle(radius=R, color=BLUE, stroke_width=3).move_to(LEFT * R + DOWN * 0.55)
        self.c2 = Circle(radius=R, color=TEAL, stroke_width=3).move_to(RIGHT * R + DOWN * 0.55)
        self.c3 = Circle(radius=R, color=YELLOW, stroke_width=3).move_to(UP * (h - 0.55))
        self.R = R
        self.play(Create(self.c1), Create(self.c2), Create(self.c3), run_time=1.7)
        note = self.ja_text("3 円が接する", font_size=24)
        note.to_edge(RIGHT, buff=0.3).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def fourth(self):
        center = (self.c1.get_center() + self.c2.get_center() + self.c3.get_center()) / 3
        k = 1 / self.R
        k4 = k * (3 + 2 * np.sqrt(3))
        r4 = 1 / k4
        c4 = Circle(radius=r4, color=ORANGE, stroke_width=4).move_to(center)
        cap = self.ja_text("第 4 円", font_size=24).move_to(self.note)
        self.play(Create(c4), Transform(self.note, cap), run_time=1.5)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"k_4").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"k_4=k_1+k_2+k_3\pm 2\sqrt{k_1k_2+k_2k_3+k_3k_1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"k_4=k_1+k_2+k_3\pm 2\sqrt{k_1k_2+k_2k_3+k_3k_1}").scale(0.55)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.1)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
