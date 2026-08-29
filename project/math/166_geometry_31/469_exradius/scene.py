from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Exradius(PacedScene):
    """#469 傍接円半径：r_a=S/(s-a)（約45秒）"""

    def construct(self):
        self.show_heading("傍接円半径")
        self.draw_triangle()
        self.excircle()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 1.8
        self.B = LEFT * 2.4 + DOWN * 1.2
        self.C = RIGHT * 2.4 + DOWN * 1.2
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def excircle(self):
        # excircle opposite A, below BC
        center = DOWN * 1.9
        circ = Circle(radius=1.1, color=ORANGE, stroke_width=3).move_to(center)
        # tangent feel to BC extended
        line = DashedLine(LEFT * 3.2 + DOWN * 1.2, RIGHT * 3.2 + DOWN * 1.2, color=GREY, stroke_width=2)
        cap = self.ja_text("傍接円", font_size=24).move_to(self.note)
        self.play(Create(line), Create(circ), FadeIn(Dot(center, color=RED, radius=0.09)), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("半径の公式", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"r_a").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"r_a=\frac{S}{s-a}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"r_a=\frac{S}{s-a}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
