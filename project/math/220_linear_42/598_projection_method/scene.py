from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class ProjectionMethod(PacedScene):
    """#598 射影法：部分空間へ残差を直交化（約45秒）"""

    def construct(self):
        self.show_heading("射影法")
        self.draw_spaces()
        self.galerkin()
        self.show_formula()
        self.read(1.4)

    def draw_spaces(self):
        K = RoundedRectangle(width=2.8, height=1.6, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        L = RoundedRectangle(width=2.8, height=1.6, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        self.play(Create(K), FadeIn(MathTex(r"\mathcal{K}", font_size=34).move_to(K)),
                  Create(L), FadeIn(MathTex(r"\mathcal{L}", font_size=34).move_to(L)), run_time=1.3)
        note = self.ja_text("探索と拘束", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def galerkin(self):
        cap = self.ja_text("ガラーキン条件", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("クリロフ法の枠", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"x\in x_0+\mathcal{K},\quad r\perp\mathcal{L}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
