from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PerspectiveAxis(PacedScene):
    """#577 配景軸：対応辺の交点が共線（約45秒）"""

    def construct(self):
        self.show_heading("配景軸")
        self.draw_tris()
        self.axis()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_tris(self):
        t1 = Polygon(UP * 2.0 + LEFT * 0.5, LEFT * 2.6 + DOWN * 1.2, RIGHT * 1.5 + DOWN * 1.4, color=BLUE, stroke_width=3)
        t2 = Polygon(UP * 1.2 + RIGHT * 0.8, LEFT * 1.0 + DOWN * 0.2, RIGHT * 2.6 + DOWN * 0.5, color=TEAL, stroke_width=3)
        self.play(Create(t1), Create(t2), run_time=1.3)
        note = self.ja_text("配景な二三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def axis(self):
        axis = Line(LEFT * 3.0 + DOWN * 1.6, RIGHT * 3.0 + DOWN * 0.8, color=YELLOW, stroke_width=4)
        dots = VGroup(*[Dot(p, color=ORANGE, radius=0.09) for p in [
            LEFT * 1.8 + DOWN * 1.35, ORIGIN + DOWN * 1.2, RIGHT * 2.0 + DOWN * 1.0
        ]])
        cap = self.ja_text("辺の交点が共線", font_size=24).move_to(self.note)
        self.play(Create(axis), FadeIn(dots), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("デザルグの双対", font_size=24).move_to(self.note)
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
        formula = self.ja_text("配景軸：対応辺の交点は一直線", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
