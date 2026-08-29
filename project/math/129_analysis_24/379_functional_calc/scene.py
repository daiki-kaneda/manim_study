from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FunctionalCalculus(PacedScene):
    """#379 関数カリキュラス：f(A) をスペクトルで定義（約45秒）"""

    def construct(self):
        self.show_heading("関数カリキュラス")
        self.draw_spec()
        self.apply_f()
        self.show_formula()
        self.read(1.4)

    def draw_spec(self):
        self.O = LEFT * 0.5 + DOWN * 0.2
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 3.0, color=GREY, stroke_width=2)
        eigs = VGroup(*[Dot(self.O + RIGHT * x, color=BLUE, radius=0.1) for x in [-1.5, 0.3, 1.8]])
        self.play(Create(ax), FadeIn(eigs), run_time=1.3)
        note = self.ja_text("スペクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.eigs = eigs

    def apply_f(self):
        # map eigenvalues via f(t)=t^2 visual lift
        imgs = VGroup(*[
            Dot(self.O + RIGHT * (x * abs(x) * 0.55) + UP * 1.2, color=ORANGE, radius=0.1)
            for x in [-1.5, 0.3, 1.8]
        ])
        arrows = VGroup(*[
            Arrow(e.get_center(), i.get_center(), buff=0.08, color=YELLOW, stroke_width=3)
            for e, i in zip(self.eigs, imgs)
        ])
        cap = self.ja_text("f を当てる", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.play(FadeIn(imgs), run_time=0.8)
        self.read(0.25)
        cap2 = self.ja_text("f(A) の固有値", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"f(A)=\sum f(\lambda_i)P_i").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
