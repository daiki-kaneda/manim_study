from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MatrixLogarithm(PacedScene):
    """#369 行列対数：exp の逆（約45秒）"""

    def construct(self):
        self.show_heading("行列対数")
        self.draw_exp()
        self.invert()
        self.show_formula()
        self.read(1.4)

    def draw_exp(self):
        a = MathTex(r"A", font_size=52).shift(LEFT * 2.8 + UP * 0.4)
        arrow = Arrow(LEFT * 2.0, LEFT * 0.4, buff=0.1, color=YELLOW, stroke_width=4)
        e = MathTex(r"e^{A}", font_size=52, color=ORANGE).shift(RIGHT * 0.8 + UP * 0.4)
        self.play(FadeIn(a), GrowArrow(arrow), FadeIn(e), run_time=1.5)
        note = self.ja_text("指数関数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def invert(self):
        back = Arrow(RIGHT * 0.8 + DOWN * 0.3, LEFT * 2.0 + DOWN * 0.3, buff=0.1, color=TEAL, stroke_width=4)
        log = MathTex(r"\log", color=TEAL, font_size=40).next_to(back, DOWN, buff=0.15)
        cap = self.ja_text("逆向き", font_size=24).move_to(self.note)
        self.play(GrowArrow(back), FadeIn(log), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("対数行列", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\log(e^{A})=A").scale(1.05)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
