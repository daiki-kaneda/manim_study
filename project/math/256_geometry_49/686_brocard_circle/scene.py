from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BrocardCircle(PacedScene):
    """#686 ブロカール円：ブロカール点と類似中線点を結ぶ（約45秒）"""

    def construct(self):
        self.show_heading("ブロカール円")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        circ = Circle(radius=1.6, color=BLUE, stroke_width=3).shift(UP * 0.1)
        dots = VGroup(Dot(circ.point_at_angle(0.3), color=YELLOW), Dot(circ.point_at_angle(2.0), color=ORANGE), Dot(circ.point_at_angle(4.0), color=TEAL))
        self.play(Create(circ), FadeIn(dots), run_time=1.3)

        note = self.ja_text("中心は円上", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("二つのブロカール", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("幾何の円", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"K,\Omega,\Omega'\in C").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
