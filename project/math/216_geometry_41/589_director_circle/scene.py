from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class DirectorCircle(PacedScene):
    """#589 楕円の導円：直交接線の交点の軌跡（約45秒）"""

    def construct(self):
        self.show_heading("楕円の導円")
        self.draw_ellipse()
        self.director()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ellipse(self):
        ell = Ellipse(width=4.0, height=2.4, color=BLUE, stroke_width=3).shift(UP * 0.15)
        self.play(Create(ell), run_time=1.2)
        note = self.ja_text("楕円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def director(self):
        circ = Circle(radius=2.35, color=ORANGE, stroke_width=3).shift(UP * 0.15)
        t1 = Line(LEFT * 2.2 + UP * 1.8, RIGHT * 1.5 + DOWN * 1.2, color=GREY, stroke_width=2)
        t2 = Line(RIGHT * 2.2 + UP * 1.8, LEFT * 1.5 + DOWN * 1.2, color=GREY, stroke_width=2)
        cap = self.ja_text("直交接線の交点", font_size=24).move_to(self.note)
        self.play(Create(circ), Create(t1), Create(t2), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("導円", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x^2+y^2").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x^2+y^2=a^2+b^2").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x^2+y^2=a^2+b^2").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
