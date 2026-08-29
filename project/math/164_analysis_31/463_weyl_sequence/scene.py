from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class WeylSequence(PacedScene):
    """#463 Weyl列：近似固有ベクトルの列（約45秒）"""

    def construct(self):
        self.show_heading("Weyl列")
        self.draw_seq()
        self.almost()
        self.show_formula()
        self.read(1.4)

    def draw_seq(self):
        vecs = VGroup(*[
            Arrow(ORIGIN, RIGHT * 1.2 + UP * (0.4 - 0.15 * i), buff=0, color=BLUE, stroke_width=3).shift(LEFT * 2.8 + RIGHT * i * 1.3 + UP * 0.3)
            for i in range(4)
        ])
        self.play(LaggedStart(*[GrowArrow(v) for v in vecs], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("単位ベクトル列", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def almost(self):
        dots = VGroup(*[Dot(LEFT * 2.2 + RIGHT * i * 1.3 + DOWN * 0.9, color=ORANGE, radius=0.09) for i in range(4)])
        path = VMobject(color=ORANGE, stroke_width=3)
        path.set_points_as_corners([d.get_center() for d in dots])
        # decreasing residuals feel
        for i,d in enumerate(dots):
            d.shift(UP * (0.5 / (i + 1)))
        path.set_points_as_corners([d.get_center() for d in dots])
        cap = self.ja_text("(A-λ)x_n → 0", font_size=24).move_to(self.note)
        self.play(Create(path), FadeIn(dots), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("弱収束なし", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|x_n\|=1,\ (A-\lambda)x_n\to 0").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
