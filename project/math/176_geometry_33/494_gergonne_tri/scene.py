from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class GergonneTriangle(PacedScene):
    """#494 ジェルゴンヌ三角形：内接接点を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("ジェルゴンヌ三角形")
        self.draw_incircle()
        self.contact()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_incircle(self):
        self.A = UP * 2.15
        self.B = LEFT * 2.7 + DOWN * 1.45
        self.C = RIGHT * 2.7 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        inc = Circle(radius=0.7, color=GREY, stroke_width=2).shift(DOWN * 0.35)
        self.play(Create(self.tri), Create(inc), run_time=1.3)
        note = self.ja_text("内接円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def contact(self):
        Ta = DOWN * 0.35 + DOWN * 0.7
        Tb = DOWN * 0.35 + LEFT * 0.55 + UP * 0.35
        Tc = DOWN * 0.35 + RIGHT * 0.55 + UP * 0.35
        # better: side mid-ish contact approximations
        Ta = self.B * 0.5 + self.C * 0.5
        Tb = self.A * 0.45 + self.C * 0.55
        Tc = self.A * 0.5 + self.B * 0.5
        g = Polygon(Ta, Tb, Tc, color=ORANGE, stroke_width=3)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.09) for p in [Ta, Tb, Tc]])
        cap = self.ja_text("接点三角形", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Create(g), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("ジェルゴンヌ点", font_size=24).move_to(self.note)
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
        formula = self.ja_text("接点三角形＝ジェルゴンヌ三角形", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
