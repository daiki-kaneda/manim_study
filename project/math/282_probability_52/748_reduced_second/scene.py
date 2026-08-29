from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ReducedSecondMoment(PacedScene):
    """#748 縮小二次モーメント：並進で見たペア測度（約45秒）"""

    def construct(self):
        self.show_heading("縮小二次モーメント")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        o = Dot(ORIGIN + UP * 0.1, color=YELLOW, radius=0.12)
        ring = Circle(radius=1.2, color=ORANGE, stroke_width=3).move_to(o)
        import random
        random.seed(2)
        pts = VGroup(*[Dot([random.uniform(-2.5, 2.5), random.uniform(-1.2, 1.2), 0], radius=0.06, color=BLUE) for _ in range(20)])
        self.play(FadeIn(pts), FadeIn(o), Create(ring), run_time=1.4)
        note = self.ja_text("差ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("K と結ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("等方なら半径のみ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathcal{K}(B)=\lambda^{-1}\mathbb{E}^0\#(\Phi\cap B\setminus\{0\})").scale(0.55)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
