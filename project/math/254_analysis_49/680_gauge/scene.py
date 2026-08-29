from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GaugeTheory(PacedScene):
    """#680 ゲージ理論：接続の同値で場を記述（約45秒）"""

    def construct(self):
        self.show_heading("ゲージ理論")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        circ = Circle(radius=1.5, color=BLUE, stroke_width=3).shift(LEFT * 0.3 + UP * 0.15)
        fiber = VGroup(*[Dot(circ.point_at_angle(a), color=ORANGE, radius=0.08) for a in [0, PI/2, PI, 3*PI/2]])
        self.play(Create(circ), FadeIn(fiber), run_time=1.3)

        note = self.ja_text("局所対称性", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("物理と幾何", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("同値類で見る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A\mapsto g^{-1}Ag+g^{-1}dg").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
