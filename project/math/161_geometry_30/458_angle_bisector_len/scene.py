from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class AngleBisectorLength(PacedScene):
    """#458 角の二等分線の長さ：隣接辺で表す（約45秒）"""

    def construct(self):
        self.show_heading("角の二等分線の長さ")
        self.draw_triangle()
        self.bisector()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.15
        self.B = LEFT * 2.7 + DOWN * 1.45
        self.C = RIGHT * 2.6 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bisector(self):
        D = 0.45 * self.B + 0.55 * self.C
        bis = Line(self.A, D, color=ORANGE, stroke_width=4)
        ang = Angle(Line(self.A, self.B), Line(self.A, self.C), radius=0.45, color=TEAL)
        cap = self.ja_text("二等分線", font_size=24).move_to(self.note)
        self.play(Create(ang), Create(bis), FadeIn(Dot(D, color=YELLOW, radius=0.09)), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("長さの公式", font_size=24).move_to(self.note)
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
        eq = MathTex(r"t_a^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"t_a^{2}=bc\left(1-\left(\frac{a}{b+c}\right)^{2}\right)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"t_a^{2}=bc\left(1-\left(\frac{a}{b+c}\right)^{2}\right)").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
