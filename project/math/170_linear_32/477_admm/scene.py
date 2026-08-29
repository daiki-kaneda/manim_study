from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ADMM(PacedScene):
    """#477 ADMM：分割して交互に更新（約45秒）"""

    def construct(self):
        self.show_heading("ADMM")
        self.draw_split()
        self.alternate()
        self.show_formula()
        self.read(1.4)

    def draw_split(self):
        f = RoundedRectangle(width=2.2, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.3)
        g = RoundedRectangle(width=2.2, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.3)
        self.play(
            Create(f), FadeIn(MathTex(r"f(x)", font_size=30).move_to(f)),
            Create(g), FadeIn(MathTex(r"g(z)", font_size=30).move_to(g)),
            run_time=1.3,
        )
        note = self.ja_text("問題を分割", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def alternate(self):
        ax = Arrow(LEFT * 1.2 + UP * 0.3, RIGHT * 1.2 + UP * 0.3, buff=0.1, color=ORANGE, stroke_width=3)
        ay = Arrow(RIGHT * 1.2 + DOWN * 0.5, LEFT * 1.2 + DOWN * 0.5, buff=0.1, color=YELLOW, stroke_width=3)
        cap = self.ja_text("交互に更新", font_size=24).move_to(self.note)
        self.play(GrowArrow(ax), GrowArrow(ay), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("双対でつなぐ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\min_x f(x)+g(z)\ \mathrm{s.t.}\ Ax+Bz=c").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
