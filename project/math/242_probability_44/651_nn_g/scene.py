from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class NearestNeighborG(PacedScene):
    """#651 最近傍関数：点から最近点までの距離分布（約45秒）"""

    def construct(self):
        self.show_heading("最近傍関数")
        self.draw_g()
        self.mean()
        self.show_formula()
        self.read(1.4)

    def draw_g(self):
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 1.2, 1], x_length=5.2, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        G = axes.plot(lambda r: 1 - (2.0 ** (-1.6 * r)), x_range=[0.02, 2.9], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(G), run_time=1.3)
        note = self.ja_text("G(r) 曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mean(self):
        cap = self.ja_text("典型点からの距離", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("F と対になる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"G(r)=P^0(d(0,\Phi\setminus\{0\})\le r)").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
