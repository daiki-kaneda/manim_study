from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class PtolemyInequality(PacedScene):
    """#433 トレミーの不等式：一般四角形版（約45秒）"""

    def construct(self):
        self.show_heading("トレミーの不等式")
        self.draw_quad()
        self.inequality()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        A = LEFT * 2.5 + UP * 1.2
        B = RIGHT * 2.3 + UP * 1.4
        C = RIGHT * 1.8 + DOWN * 1.5
        D = LEFT * 2.0 + DOWN * 1.3
        self.pts = [A, B, C, D]
        self.quad = Polygon(*self.pts, color=BLUE, stroke_width=3)
        self.play(Create(self.quad), run_time=1.2)
        note = self.ja_text("一般の四角形", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def inequality(self):
        d1 = Line(self.pts[0], self.pts[2], color=ORANGE, stroke_width=3)
        d2 = Line(self.pts[1], self.pts[3], color=TEAL, stroke_width=3)
        cap = self.ja_text("対辺積の和", font_size=24).move_to(self.note)
        self.play(Create(d1), Create(d2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("対角線積以上", font_size=24).move_to(self.note)
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
        eq = MathTex(r"ac+bd\ge pq").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"ac+bd\ge pq").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"ac+bd\ge pq").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
