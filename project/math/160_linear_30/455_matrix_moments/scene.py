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

    def show_formula(self):
        formula = MathTex(r"\mathrm{Tr}(A^k)=\sum_i\lambda_i^k").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
