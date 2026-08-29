from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import PacedScene


class AngleBisector(PacedScene):
    """#148 角の二等分線定理（約50秒）"""

    def construct(self):
        self.show_heading("角の二等分線")
        self.draw_triangle()
        self.bisect()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = LEFT * 0.15 + UP * 2.15
        self.B = LEFT * 3.55 + DOWN * 1.5
        self.C = RIGHT * 2.25 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=WHITE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.5)
        self.labs = VGroup(
            MathTex("A", font_size=28).next_to(self.A, UP, buff=0.08),
            MathTex("B", font_size=28).next_to(self.B, DL, buff=0.08),
            MathTex("C", font_size=28).next_to(self.C, DR, buff=0.08),
        )
        self.play(FadeIn(self.labs), run_time=0.65)
        self.read(0.35)

    def _ang(self, v):
        return np.arctan2(v[1], v[0])

    def bisect(self):
        ab = np.linalg.norm((self.B - self.A)[:2])
        ac = np.linalg.norm((self.C - self.A)[:2])
        self.D = (ac * self.B + ab * self.C) / (ab + ac)
        a1 = self._ang(self.B - self.A)
        a2 = self._ang(self.C - self.A)
        # unwrap so arc is the interior angle
        if a2 < a1:
            a1, a2 = a2, a1
        if a2 - a1 > np.pi:
            a1, a2 = a2, a1 + 2 * np.pi
        mid = 0.5 * (a1 + a2)
        arc_l = Arc(radius=0.42, start_angle=a1, angle=0.5 * (a2 - a1), color=YELLOW, stroke_width=4).move_arc_center_to(self.A)
        arc_r = Arc(radius=0.42, start_angle=mid, angle=0.5 * (a2 - a1), color=YELLOW, stroke_width=4).move_arc_center_to(self.A)
        note = self.ja_text("同じ角", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(Create(arc_l), Create(arc_r), FadeIn(note), run_time=1.5)
        self.read(0.4)
        bis = Line(self.A, self.D, color=YELLOW, stroke_width=5)
        dlab = MathTex("D", font_size=28).next_to(self.D, DOWN, buff=0.1)
        self.play(Create(bis), FadeIn(Dot(self.D, color=ORANGE, radius=0.08)), FadeIn(dlab), run_time=1.5)
        self.read(0.4)
        brace_bd = BraceBetweenPoints(self.B, self.D, direction=DOWN, color=BLUE)
        brace_dc = BraceBetweenPoints(self.D, self.C, direction=DOWN, color=GREEN)
        cap = self.ja_text("底辺の比", font_size=24).move_to(note)
        self.play(GrowFromCenter(brace_bd), GrowFromCenter(brace_dc), Transform(note, cap), run_time=1.5)
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
        eq = MathTex(r"\frac{BD}{DC}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{BD}{DC}=\frac{AB}{AC}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{BD}{DC}=\frac{AB}{AC}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
