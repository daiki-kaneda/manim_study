from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PtolemyGeneral(PacedScene):
    """#552 トレミーの一般化：不等式と等号条件（約45秒）"""

    def construct(self):
        self.show_heading("トレミーの一般化")
        self.draw_quad()
        self.ineq()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_quad(self):
        pts = [UP * 1.8, RIGHT * 2.3 + UP * 0.4, RIGHT * 1.2 + DOWN * 1.5, LEFT * 2.4 + DOWN * 0.8]
        quad = Polygon(*pts, color=BLUE, stroke_width=3)
        diags = VGroup(Line(pts[0], pts[2], color=ORANGE), Line(pts[1], pts[3], color=ORANGE))
        self.play(Create(quad), Create(diags), run_time=1.4)
        note = self.ja_text("一般四角形", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ineq(self):
        cap = self.ja_text("不等式になる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("等号は共円のとき", font_size=24).move_to(self.note)
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
        eq = MathTex(r"ac+bd\ge ef").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"ac+bd\ge ef").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"ac+bd\ge ef").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
