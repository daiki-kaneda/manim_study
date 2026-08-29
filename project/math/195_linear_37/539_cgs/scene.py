from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CGS(PacedScene):
    """#539 CGS：残差多項式を二乗して進む（約45秒）"""

    def construct(self):
        self.show_heading("CGS")
        self.draw_poly()
        self.square()
        self.show_formula()
        self.read(1.4)

    def draw_poly(self):
        box = RoundedRectangle(width=3.2, height=1.4, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.0 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"p_k(A)r_0", font_size=32).move_to(box)), run_time=1.3)
        note = self.ja_text("残差多項式", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def square(self):
        box2 = RoundedRectangle(width=3.2, height=1.4, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        cap = self.ja_text("二乗して加速", font_size=24).move_to(self.note)
        self.play(Create(box2), FadeIn(MathTex(r"p_k(A)^2 r_0", font_size=30).move_to(box2)), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("転置不要", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"r_k=p_k(A)^2 r_0").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
