from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EssentialNorm(PacedScene):
    """#462 本質ノルム：コンパクト摂動で測るノルム（約45秒）"""

    def construct(self):
        self.show_heading("本質ノルム")
        self.draw_ops()
        self.infimum()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        T = RoundedRectangle(width=2.4, height=1.6, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.6 + UP * 0.2)
        K = RoundedRectangle(width=2.0, height=1.3, corner_radius=0.12, color=GREY, stroke_width=2).shift(LEFT * 2.6 + DOWN * 1.2)
        self.play(Create(T), FadeIn(MathTex("T", font_size=34).move_to(T)), run_time=1.1)
        self.play(Create(K), FadeIn(MathTex("K", font_size=30).move_to(K)), run_time=0.9)
        note = self.ja_text("コンパクトを足す", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def infimum(self):
        arrow = Arrow(LEFT * 0.8, RIGHT * 0.5, buff=0.05, color=YELLOW, stroke_width=4)
        box = RoundedRectangle(width=2.8, height=1.4, corner_radius=0.12, color=ORANGE, stroke_width=3).shift(RIGHT * 2.3 + UP * 0.1)
        lab = MathTex(r"\|T\|_{\mathrm{ess}}", font_size=34).move_to(box)
        cap = self.ja_text("ノルムの下限", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Create(box), FadeIn(lab), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("摂動で不変", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|T\|_{\mathrm{ess}}=\inf_K\|T+K\|").scale(0.88)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
