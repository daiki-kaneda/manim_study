from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ILU(PacedScene):
    """#573 ILU：不完全 LU で疎前処理（約45秒）"""

    def construct(self):
        self.show_heading("ILU")
        self.draw_factors()
        self.drop()
        self.show_formula()
        self.read(1.4)

    def draw_factors(self):
        L = RoundedRectangle(width=2.2, height=1.5, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.2)
        U = RoundedRectangle(width=2.2, height=1.5, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.2)
        self.play(Create(L), FadeIn(MathTex("L", font_size=36).move_to(L)),
                  Create(U), FadeIn(MathTex("U", font_size=36).move_to(U)), run_time=1.3)
        note = self.ja_text("不完全分解", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def drop(self):
        cap = self.ja_text("フィルインを制限", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("前処理に使う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A\approx \tilde L\tilde U").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
