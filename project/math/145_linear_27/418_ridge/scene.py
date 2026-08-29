from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class RidgeRegression(PacedScene):
    """#418 リッジ：正規方程式に λI を足す（約45秒）"""

    def construct(self):
        self.show_heading("リッジ回帰")
        self.draw_fit()
        self.penalty()
        self.show_formula()
        self.read(1.4)

    def draw_fit(self):
        axes = Axes(x_range=[-0.5, 3.5, 1], y_range=[-0.5, 2.5, 1], x_length=5.5, y_length=3.0,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.15)
        pts = [(0.4, 0.5), (1.0, 1.3), (1.8, 1.1), (2.6, 2.1)]
        dots = VGroup(*[Dot(axes.c2p(x, y), color=BLUE, radius=0.09) for x, y in pts])
        line = axes.plot(lambda x: 0.55 * x + 0.35, x_range=[0.2, 3.2], color=ORANGE, stroke_width=4)
        self.play(Create(axes), FadeIn(dots), Create(line), run_time=1.5)
        note = self.ja_text("当てはめ", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def penalty(self):
        pen = MathTex(r"+\lambda\|x\|^2", font_size=38).shift(DOWN * 0.9)
        cap = self.ja_text("罰則を足す", font_size=24).move_to(self.note)
        self.play(FadeIn(pen), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("安定化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"(A^{*}A+\lambda I)x=A^{*}b").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
