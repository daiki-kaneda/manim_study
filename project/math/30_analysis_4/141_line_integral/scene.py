from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class LineIntegral(PacedScene):
    """#141 線積分は道に沿って積む（約50秒）"""

    def construct(self):
        self.origin = LEFT * 2.35 + DOWN * 0.15
        self.show_heading("線積分")
        self.draw_field()
        self.draw_path()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_field(self):
        arrows = VGroup()
        for i in range(-2, 4):
            for j in range(-2, 3):
                p = self.origin + RIGHT * (0.72 * i) + UP * (0.72 * j)
                v = np.array([-0.22 * j, 0.22 * i, 0.0])
                if np.linalg.norm(v) < 0.04:
                    continue
                arrows.add(Arrow(p, p + v, buff=0, color=GREY_B, stroke_width=2, max_tip_length_to_length_ratio=0.28))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.03), run_time=2.6)
        note = self.ja_text("ベクトル場", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.4)
        self.note = note

    def draw_path(self):
        r = 1.35
        path = Circle(radius=r, color=YELLOW, stroke_width=6).move_to(self.origin)
        cap = self.ja_text("道に沿う", font_size=24).move_to(self.note)
        self.play(Create(path), Transform(self.note, cap), run_time=2.2)
        self.read(0.35)
        dot = Dot(self.origin + RIGHT * r, color=ORANGE, radius=0.09)
        self.play(FadeIn(dot), run_time=0.4)
        self.play(MoveAlongPath(dot, path), run_time=2.4)
        cap2 = self.ja_text("一周でたまる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.7)
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
        eq = MathTex(r"\int_C\mathbf{F}\cdot d\mathbf{r}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\int_C\mathbf{F}\cdot d\mathbf{r}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\int_C\mathbf{F}\cdot d\mathbf{r}").scale(1.05)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
