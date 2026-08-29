from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GMRES(PacedScene):
    """#371 GMRES：クリロフ空間で残差を最小化（約45秒）"""

    def construct(self):
        self.show_heading("GMRES")
        self.draw_krylov()
        self.minimize()
        self.show_formula()
        self.read(1.4)

    def draw_krylov(self):
        self.O = LEFT * 1.5 + DOWN * 0.2
        basis = VGroup(*[
            Arrow(self.O, self.O + d, buff=0, color=c, stroke_width=4)
            for d, c in [
                (RIGHT * 2.0, BLUE),
                (RIGHT * 1.2 + UP * 1.4, TEAL),
                (LEFT * 0.3 + UP * 1.8, GREY),
            ]
        ])
        self.play(LaggedStart(*[GrowArrow(a) for a in basis], lag_ratio=0.15), run_time=1.5)
        note = self.ja_text("クリロフ空間", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def minimize(self):
        # residual arrow shrinking
        r0 = Arrow(RIGHT * 1.5 + UP * 1.2, RIGHT * 2.8 + UP * 1.8, buff=0, color=ORANGE, stroke_width=5)
        r1 = Arrow(RIGHT * 1.5 + UP * 0.3, RIGHT * 2.0 + UP * 0.5, buff=0, color=YELLOW, stroke_width=5)
        cap = self.ja_text("残差", font_size=24).move_to(self.note)
        self.play(GrowArrow(r0), Transform(self.note, cap), run_time=1.1)
        self.read(0.2)
        cap2 = self.ja_text("最小にする", font_size=24).move_to(self.note)
        self.play(Transform(r0, r1), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\min_{x\in x_0+\mathcal{K}_m}\|b-Ax\|").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
