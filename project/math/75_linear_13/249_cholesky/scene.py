from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Cholesky(PacedScene):
    """#249 コレスキーは A=LL^T（約45秒）"""

    def construct(self):
        self.show_heading("コレスキー分解")
        self.draw_matrix()
        self.factor()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_matrix(self):
        a = Matrix([["4", "2"], ["2", "3"]], h_buff=0.85, v_buff=0.7).scale(0.9)
        a.shift(LEFT * 2.8 + UP * 0.3)
        self.play(FadeIn(a), run_time=1.2)
        note = self.ja_text("正定値対称", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.a = a

    def factor(self):
        # L = [[2,0],[1,√2]] approx
        L = Matrix([["2", "0"], ["1", r"\sqrt{2}"]], h_buff=0.85, v_buff=0.7).scale(0.85)
        Lt = Matrix([["2", "1"], ["0", r"\sqrt{2}"]], h_buff=0.85, v_buff=0.7).scale(0.85)
        L.shift(RIGHT * 0.3 + UP * 0.3)
        times = MathTex(r"\times").next_to(L, RIGHT, buff=0.25)
        Lt.next_to(times, RIGHT, buff=0.25)
        box = SurroundingRectangle(L, color=TEAL, buff=0.12, corner_radius=0.06)
        cap = self.ja_text("下三角 L", font_size=24).move_to(self.note)
        self.play(FadeIn(L), Create(box), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("L L^{T}", font_size=24).move_to(self.note)
        self.play(FadeIn(times), FadeIn(Lt), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"A").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"A=LL^{\mathsf T}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"A=LL^{\mathsf T}").scale(1.15)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.6)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
