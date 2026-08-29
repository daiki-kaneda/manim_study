from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class RiordanNumbers(PacedScene):
    """#641 リオルダン数：モツキンに近い格子路の数え上げ（約45秒）"""

    def construct(self):
        self.show_heading("リオルダン数")
        self.draw_path()
        self.count()
        self.show_formula()
        self.read(1.4)

    def draw_path(self):
        axes = Axes(x_range=[0, 6, 1], y_range=[0, 3, 1], x_length=6.0, y_length=2.4,
                    tips=False, axis_config={"stroke_width": 1, "include_ticks": False}).shift(UP * 0.15)
        pts = [axes.c2p(0, 0), axes.c2p(1, 1), axes.c2p(2, 1), axes.c2p(3, 2), axes.c2p(4, 1), axes.c2p(5, 0)]
        path = VMobject(color=BLUE, stroke_width=4).set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, radius=0.07, color=YELLOW) for p in pts])
        self.play(Create(axes), Create(path), FadeIn(dots), run_time=1.4)
        note = self.ja_text("高さ制限路", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def count(self):
        cap = self.ja_text("水平も許す", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("モツキンの仲間", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"R_n=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n}{2k}C_k").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
