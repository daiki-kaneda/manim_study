from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class MatrixMoments(PacedScene):
    """#455 行列モーメント：Tr(A^k) でスペクトルを探る（約45秒）"""

    def construct(self):
        self.show_heading("行列モーメント")
        self.draw_powers()
        self.trace()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_powers(self):
        mats = VGroup(*[
            MathTex(rf"A^{k}", font_size=36).shift(LEFT * 2.8 + RIGHT * i * 1.4 + UP * 0.5)
            for i, k in enumerate([1, 2, 3, "k"])
        ])
        self.play(LaggedStart(*[FadeIn(m) for m in mats], lag_ratio=0.12), run_time=1.4)
        note = self.ja_text("冪を取る", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def trace(self):
        tr = MathTex(r"\mathrm{Tr}(A^k)", font_size=40, color=ORANGE).shift(DOWN * 0.7)
        cap = self.ja_text("トレース", font_size=24).move_to(self.note)
        self.play(FadeIn(tr), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("固有値の冪和", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\mathrm{Tr}(A^k)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{Tr}(A^k)=\sum_i\lambda_i^k").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{Tr}(A^k)=\sum_i\lambda_i^k").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
