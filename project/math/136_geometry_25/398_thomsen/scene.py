from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

import numpy as np


class Thomsen(PacedScene):
    """#398 トムセン：辺に平行線を辿ると閉じる（約45秒）"""

    def construct(self):
        self.show_heading("トムセンの図形")
        self.draw_triangle()
        self.walk()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.2
        self.B = LEFT * 2.7 + DOWN * 1.5
        self.C = RIGHT * 2.7 + DOWN * 1.5
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def walk(self):
        # schematic closed chain of points on the sides
        pts = [
            0.7 * self.B + 0.3 * self.C,
            0.55 * self.B + 0.45 * self.A,
            0.55 * self.A + 0.45 * self.C,
            0.3 * self.B + 0.7 * self.C,
            0.45 * self.A + 0.55 * self.C,
            0.45 * self.A + 0.55 * self.B,
        ]
        order = [0, 5, 1, 4, 2, 3, 0]
        path = VMobject(color=ORANGE, stroke_width=4)
        path.set_points_as_corners([pts[i] for i in order])
        dots = VGroup(*[Dot(pts[i], color=YELLOW, radius=0.08) for i in order[:-1]])
        cap = self.ja_text("平行に辿る", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.0)
        self.play(Create(path), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("必ず閉じる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(path, color=YELLOW), run_time=1.1)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("平行移動の巡回路は閉じる", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
