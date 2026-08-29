from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class WeakConvergence(PacedScene):
    """#523 弱収束：汎関数ごとに収束（約45秒）"""

    def construct(self):
        self.show_heading("弱収束")
        self.draw_seq()
        self.dual()
        self.show_formula()
        self.read(1.4)

    def draw_seq(self):
        dots = VGroup(*[Dot(LEFT * 2.5 + RIGHT * i * 0.9 + UP * 0.5, color=BLUE, radius=0.1) for i in range(5)])
        labs = VGroup(*[MathTex(rf"x_{{{i}}}", font_size=24).next_to(dots[i], UP, buff=0.1) for i in range(5)])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.1), FadeIn(labs), run_time=1.3)
        note = self.ja_text("点列", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def dual(self):
        f = MathTex(r"f\in X^*", font_size=34).shift(DOWN * 0.5)
        cap = self.ja_text("すべての汎関数で", font_size=24).move_to(self.note)
        self.play(FadeIn(f), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("強収束より弱い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x_n\rightharpoonup x\ \Leftrightarrow\ f(x_n)\to f(x)\ \forall f\in X^*").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
