from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SWA(PacedScene):
    """#683 SWA：確率的重み平均で汎化（約45秒）"""

    def construct(self):
        self.show_heading("SWA")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        pts = [LEFT * 2 + UP * 0.8, LEFT * 0.5 + DOWN * 0.2, RIGHT * 0.8 + UP * 0.5, RIGHT * 2.2 + DOWN * 0.1]
        path = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(pts)
        avg = Dot((pts[0]+pts[1]+pts[2]+pts[3])/4, color=YELLOW, radius=0.12)
        self.play(Create(path), FadeIn(VGroup(*[Dot(p, radius=0.07, color=ORANGE) for p in pts])), FadeIn(avg), run_time=1.4)

        note = self.ja_text("重みを平均", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("汎化向上", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("後半軌跡を使う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\bar\theta=\frac{1}{T}\sum_{t=1}^T\theta_t").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
