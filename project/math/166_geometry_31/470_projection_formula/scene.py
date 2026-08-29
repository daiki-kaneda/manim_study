from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ProjectionFormula(PacedScene):
    """#470 投影公式：a=b cos C+c cos B（約45秒）"""

    def construct(self):
        self.show_heading("投影公式")
        self.draw_triangle()
        self.project()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1 + LEFT * 0.3
        self.B = LEFT * 2.6 + DOWN * 1.4
        self.C = RIGHT * 2.8 + DOWN * 1.3
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("辺 a に落とす", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def project(self):
        # feet from A,B conceptually onto BC... actually project AB,AC onto a=BC
        # Drop perpendiculars from B and C onto... projection of sides onto a
        # Show segments on BC
        P = 0.35 * self.B + 0.65 * self.C
        Q = 0.7 * self.B + 0.3 * self.C
        # Actually: from B and C, show cos projections along BC
        foot_from_B_side = self.B  # schematic braces on BC
        seg1 = Line(self.B, 0.45 * self.B + 0.55 * self.C, color=ORANGE, stroke_width=6)
        seg2 = Line(0.45 * self.B + 0.55 * self.C, self.C, color=TEAL, stroke_width=6)
        cap = self.ja_text("cos で投影", font_size=24).move_to(self.note)
        self.play(Create(seg1), Create(seg2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("和が辺 a", font_size=24).move_to(self.note)
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
        eq = MathTex(r"a").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"a=b\cos C+c\cos B").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"a=b\cos C+c\cos B").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
