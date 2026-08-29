from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class HessianFree(PacedScene):
    """#515 ヘッセフリー：Hessian-vector 積だけでニュートン（約45秒）"""

    def construct(self):
        self.show_heading("ヘッセフリー")
        self.draw_hv()
        self.cg_inner()
        self.show_formula()
        self.read(1.4)

    def draw_hv(self):
        box = RoundedRectangle(width=3.4, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 1.8 + UP * 0.3)
        lab = MathTex(r"H(x)v\approx\frac{\nabla f(x+\epsilon v)-\nabla f(x)}{\epsilon}", font_size=26).scale(0.85).move_to(box)
        self.play(Create(box), FadeIn(lab), run_time=1.4)
        note = self.ja_text("差分で Hv", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cg_inner(self):
        cap = self.ja_text("内側は CG", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("行列を持たない", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"H(x_k)p_k\approx-\nabla f(x_k)\quad(\mathrm{CG})").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
