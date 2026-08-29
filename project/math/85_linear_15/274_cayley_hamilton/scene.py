from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CayleyHamilton(PacedScene):
    """#274 ケーリー・ハミルトン：A は固有多項式を満たす（約45秒）"""

    def construct(self):
        self.show_heading("ケーリー・ハミルトン")
        self.draw_charpoly()
        self.plug_matrix()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_charpoly(self):
        self.poly = MathTex(r"p(\lambda)=\det(\lambda I-A)", font_size=42)
        self.poly.shift(UP * 1.1)
        self.play(Write(self.poly), run_time=1.6)
        note = self.ja_text("固有多項式", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def plug_matrix(self):
        arrow = Arrow(UP * 0.55, DOWN * 0.15, buff=0.05, color=ORANGE)
        plugged = MathTex(r"p(A)", font_size=48, color=ORANGE).shift(DOWN * 0.55)
        cap = self.ja_text("A を代入", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.2)
        self.play(Write(plugged), run_time=1.0)
        self.read(0.25)
        zero = MathTex(r"=O", font_size=48, color=YELLOW).next_to(plugged, RIGHT, buff=0.25)
        cap2 = self.ja_text("零行列", font_size=24).move_to(self.note)
        self.play(Write(zero), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"p(A)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"p(A)=O").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"p(A)=O").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
