from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TaylorCircle(PacedScene):
    """#721 テーラー円：垂足三角形の辺上の6点円（約45秒）"""

    def construct(self):
        self.show_heading("テーラー円")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.7 + DOWN * 1.2, RIGHT * 2.7 + DOWN * 1.2, UP * 1.8, color=BLUE, stroke_width=3)
        circ = Circle(radius=1.0, color=ORANGE, stroke_width=3).shift(DOWN * 0.05)
        pts = VGroup(*[Dot(circ.point_at_angle(a), color=YELLOW, radius=0.07) for a in [0.2, 1.2, 2.2, 3.2, 4.2, 5.2]])
        self.play(Create(tri), Create(circ), FadeIn(pts), run_time=1.4)

        note = self.ja_text("垂足辺上の点", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("6点が共円", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("テーラー中心", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"6\ \mathrm{pts\ on\ C}").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
