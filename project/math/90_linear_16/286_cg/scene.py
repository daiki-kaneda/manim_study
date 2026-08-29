from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ConjugateGradient(PacedScene):
    """#286 共役勾配：共役方向に進む（約45秒）"""

    def construct(self):
        self.show_heading("共役勾配法")
        self.draw_ellipse()
        self.conjugate_steps()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ellipse(self):
        self.O = LEFT * 0.4 + DOWN * 0.1
        self.ell = Ellipse(width=5.2, height=3.0, color=GREY, stroke_width=3).move_to(self.O)
        self.start = Dot(self.O + LEFT * 2.0 + DOWN * 0.9, color=BLUE, radius=0.1)
        self.play(Create(self.ell), FadeIn(self.start), run_time=1.3)
        note = self.ja_text("二次形式", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def conjugate_steps(self):
        p1 = self.O + LEFT * 0.3 + UP * 0.7
        p2 = self.O + RIGHT * 0.9 + DOWN * 0.15
        a1 = Arrow(self.start.get_center(), p1, buff=0.05, color=ORANGE, stroke_width=4)
        a2 = Arrow(p1, p2, buff=0.05, color=TEAL, stroke_width=4)
        cap = self.ja_text("共役な方向", font_size=24).move_to(self.note)
        self.play(GrowArrow(a1), Transform(self.note, cap), run_time=1.2)
        self.play(GrowArrow(a2), FadeIn(Dot(p2, color=YELLOW, radius=0.1)), run_time=1.1)
        self.read(0.3)
        cap2 = self.ja_text("少ない歩数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(Dot(p2, color=YELLOW), color=YELLOW), run_time=1.0)
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
        eq = MathTex(r"p_i^{\top} A p_j").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"p_i^{\top} A p_j=0\ (i\neq j)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"p_i^{\top} A p_j=0\ (i\neq j)").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
