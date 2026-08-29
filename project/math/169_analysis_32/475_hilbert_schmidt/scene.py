from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HilbertSchmidt(PacedScene):
    """#475 ヒルベルト・シュミット：二乗特異値が有限（約45秒）"""

    def construct(self):
        self.show_heading("ヒルベルト・シュミット")
        self.draw_matrix()
        self.frobenius()
        self.show_formula()
        self.read(1.4)

    def draw_matrix(self):
        grid = VGroup(*[
            Square(side_length=0.55, color=BLUE, stroke_width=2).shift(
                LEFT * 2.2 + RIGHT * j * 0.6 + UP * 1.0 + DOWN * i * 0.6
            )
            for i in range(3) for j in range(3)
        ])
        self.play(LaggedStart(*[Create(s) for s in grid], lag_ratio=0.05), run_time=1.3)
        note = self.ja_text("無限行列", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def frobenius(self):
        dots = VGroup(*[
            Dot(LEFT * 2.2 + RIGHT * j * 0.6 + UP * 1.0 + DOWN * i * 0.6, color=ORANGE, radius=0.07)
            for i in range(3) for j in range(3)
        ])
        cap = self.ja_text("入口の二乗和", font_size=24).move_to(self.note)
        self.play(FadeIn(dots), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("トレース級に近い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|T\|_{\mathrm{HS}}^2=\sum_n\|Te_n\|^2=\mathrm{tr}(T^*T)").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
