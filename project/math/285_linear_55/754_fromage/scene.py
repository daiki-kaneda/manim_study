from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Fromage(PacedScene):
    """#754 Fromage：フロベニウス平均で直交制約最適化（約45秒）"""

    def construct(self):
        self.show_heading("Fromage")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        circ = Circle(radius=1.5, color=BLUE, stroke_width=3).shift(LEFT * 0.3 + UP * 0.15)
        pts = VGroup(*[Dot(circ.point_at_angle(a), color=ORANGE, radius=0.09) for a in [0.3, 1.5, 2.8, 4.5]])
        self.play(Create(circ), FadeIn(pts), run_time=1.3)
        note = self.ja_text("直交多様体", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("フロベニウス平均", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("回転の平均", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"U\leftarrow\mathrm{Fromage}(U_1,\ldots,U_m)").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
