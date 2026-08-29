from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ReducedPalm(PacedScene):
    """#724 縮小パーム：典型点を除いた条件付き配置（約45秒）"""

    def construct(self):
        self.show_heading("縮小パーム")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        import random
        random.seed(9)
        pts = VGroup(*[Dot([random.uniform(-2.8, 2.8), random.uniform(-1.1, 1.1), 0], radius=0.07, color=BLUE) for _ in range(16)])
        typ = Dot(ORIGIN, radius=0.12, color=YELLOW)
        self.play(FadeIn(pts), FadeIn(typ), run_time=1.2)
        self.play(FadeOut(typ), run_time=0.6)

        note = self.ja_text("典型点を除く", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("残りの法則", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("スラヴィニャクへ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"P^{!0}=P^0(\cdot\setminus\{0\})").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
