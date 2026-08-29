from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class Narayana(PacedScene):
    """#413 ナラヤナ数：ピーク数つきカタラン（約45秒）"""

    def construct(self):
        self.show_heading("ナラヤナ数")
        self.draw_path()
        self.peaks()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[0, 6.2, 1], y_range=[-0.2, 2.5, 1], x_length=7.0, y_length=2.8,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35)
        pts = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 2), (5, 1), (6, 0)]
        path = VMobject(color=BLUE, stroke_width=4)
        path.set_points_as_corners([axes.c2p(x, y) for x, y in pts])
        dots = VGroup(*[Dot(axes.c2p(x, y), color=ORANGE, radius=0.08) for x, y in pts])
        self.play(Create(axes), Create(path), FadeIn(dots), run_time=1.5)
        note = self.ja_text("カタラン道", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def peaks(self):
        # peaks at (1,1) and (4,2)
        peaks = VGroup(
            Dot(self.axes.c2p(1, 1), color=RED, radius=0.12),
            Dot(self.axes.c2p(4, 2), color=RED, radius=0.12),
        )
        cap = self.ja_text("ピークを数える", font_size=24).move_to(self.note)
        self.play(FadeIn(peaks), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("細分したカタラン", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"N(n,k)=\frac1n\binom n k\binom n {k-1}").scale(0.85)
        formula = MathTex(r"N(n,k)=rac1ninom{n}{k}inom{n}{k-1}").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
