from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CenterOfSimilitude(PacedScene):
    """#638 相似の中心：二円を結ぶ相似変換の定点（約45秒）"""

    def construct(self):
        self.show_heading("相似の中心")
        self.draw_circles()
        self.external()
        self.show_formula()
        self.read(1.4)

    def draw_circles(self):
        c1 = Circle(radius=0.9, color=BLUE, stroke_width=3).shift(LEFT * 2.0 + UP * 0.2)
        c2 = Circle(radius=1.5, color=ORANGE, stroke_width=3).shift(RIGHT * 1.6 + UP * 0.2)
        self.play(Create(c1), Create(c2), run_time=1.2)
        note = self.ja_text("二円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.c1, self.c2 = c1, c2

    def external(self):
        # external center roughly left of both
        S = Dot(LEFT * 3.6 + UP * 0.2, color=YELLOW, radius=0.1)
        tang = VGroup(
            Line(S.get_center(), self.c1.get_center() + UP * 0.9, color=TEAL, stroke_width=2),
            Line(S.get_center(), self.c2.get_center() + UP * 1.5, color=TEAL, stroke_width=2),
        )
        cap = self.ja_text("外相似中心", font_size=24).move_to(self.note)
        self.play(FadeIn(S), Create(tang), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("半径比で分割", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\frac{O_1S}{O_2S}=\frac{r_1}{r_2}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
