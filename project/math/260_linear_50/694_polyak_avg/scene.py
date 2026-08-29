from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PolyakAveraging(PacedScene):
    """#694 ポリアック平均：反復列の平均で加速（約45秒）"""

    def construct(self):
        self.show_heading("ポリアック平均")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        pts = [LEFT*2+UP*0.9, LEFT*0.7+UP*0.2, RIGHT*0.5+UP*0.6, RIGHT*2+DOWN*0.1]
        path = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(pts)
        avg = Dot((pts[0]+pts[1]+pts[2]+pts[3])/4, color=YELLOW, radius=0.12)
        self.play(Create(path), FadeIn(VGroup(*[Dot(p, color=ORANGE, radius=0.07) for p in pts])), FadeIn(avg), run_time=1.4)

        note = self.ja_text("反復を平均", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("収束を加速", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("平均で加速", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.75)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\bar x_N").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\bar x_N=\frac{1}{N}\sum_{k=1}^N x_k").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\bar x_N=\frac{1}{N}\sum_{k=1}^N x_k").scale(0.75)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
