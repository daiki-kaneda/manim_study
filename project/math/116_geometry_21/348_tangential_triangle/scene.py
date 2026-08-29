from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class TangentialTriangle(PacedScene):
    """#348 接線三角形：外接円の接点を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("接線三角形")
        self.draw_base()
        self.contact()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_base(self):
        self.O = ORIGIN + DOWN * 0.1
        self.circ = Circle(radius=2.2, color=GREY, stroke_width=2).move_to(self.O)
        angs = [0.4, 2.3, 4.5]
        self.pts = [self.O + 2.2 * np.array([np.cos(a), np.sin(a), 0]) for a in angs]
        self.tri = Polygon(*self.pts, color=BLUE, stroke_width=3)
        self.play(Create(self.circ), Create(self.tri), run_time=1.4)
        note = self.ja_text("外接円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def contact(self):
        # mid-arc contact points approx on circle opposite vertices
        contacts = []
        for i in range(3):
            a = (self.pts[(i + 1) % 3] + self.pts[(i + 2) % 3]) / 2
            v = a - self.O
            v = 2.2 * v / np.linalg.norm(v)
            contacts.append(self.O + v)
        tang = Polygon(*contacts, color=ORANGE, stroke_width=3)
        cap = self.ja_text("接点を結ぶ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(Dot(c, color=YELLOW, radius=0.08)) for c in contacts], lag_ratio=0.1), Transform(self.note, cap), run_time=1.2)
        self.play(Create(tang), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("接線三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    
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
        formula = self.ja_text("接点が作る三角形", font_size=30)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
