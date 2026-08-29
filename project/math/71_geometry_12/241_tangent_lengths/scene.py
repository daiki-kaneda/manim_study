from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class TangentLengths(PacedScene):
    """#241 外点から二接線は等長（約45秒）"""

    def construct(self):
        self.show_heading("接線の長さ")
        self.draw_circle()
        self.draw_tangents()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        self.O = LEFT * 0.8 + DOWN * 0.2
        self.R = 1.6
        self.circ = Circle(radius=self.R, color=GREY, stroke_width=3).move_to(self.O)
        self.P = RIGHT * 3.0 + UP * 1.3
        self.play(Create(self.circ), FadeIn(Dot(self.O, radius=0.07, color=GREY_B)), run_time=1.1)
        self.play(FadeIn(Dot(self.P, color=YELLOW, radius=0.1)), run_time=0.5)
        pl = MathTex("P", font_size=28).next_to(self.P, UR, buff=0.08)
        self.play(FadeIn(pl), run_time=0.3)
        note = self.ja_text("外点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def draw_tangents(self):
        # tangent points: solve |T-O|=R, (T-O)·(T-P)=0
        # geometric: angle
        d = np.linalg.norm(self.P - self.O)
        ang = np.arccos(self.R / d)
        base = np.arctan2(*(self.P - self.O)[1::-1])  # wrong
        v = self.P - self.O
        base = np.arctan2(v[1], v[0])
        t1 = self.O + self.R * np.array([np.cos(base + ang), np.sin(base + ang), 0])
        t2 = self.O + self.R * np.array([np.cos(base - ang), np.sin(base - ang), 0])
        l1 = Line(self.P, t1, color=BLUE, stroke_width=4)
        l2 = Line(self.P, t2, color=TEAL, stroke_width=4)
        self.play(Create(l1), Create(l2), FadeIn(Dot(t1, color=ORANGE, radius=0.08)), FadeIn(Dot(t2, color=ORANGE, radius=0.08)), run_time=1.5)
        # length markers as thick ticks mid-segment
        m1 = Line(0.5 * (self.P + t1) + UP * 0.12, 0.5 * (self.P + t1) + DOWN * 0.12, color=YELLOW, stroke_width=5)
        m2 = Line(0.5 * (self.P + t2) + UP * 0.12, 0.5 * (self.P + t2) + DOWN * 0.12, color=YELLOW, stroke_width=5)
        cap = self.ja_text("長さが等しい", font_size=24).move_to(self.note)
        self.play(Create(m1), Create(m2), Transform(self.note, cap), run_time=1.3)
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
        eq = MathTex(r"PT_1").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"PT_1=PT_2").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"PT_1=PT_2").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.5)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
