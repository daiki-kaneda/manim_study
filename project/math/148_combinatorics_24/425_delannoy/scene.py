from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Delannoy(PacedScene):
    """#425 デランノワ数：格子の右・上・斜めの道（約45秒）"""

    def construct(self):
        self.show_heading("デランノワ数")
        self.draw_grid()
        self.paths()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        axes = NumberPlane(
            x_range=[0, 3, 1], y_range=[0, 3, 1], x_length=4.5, y_length=4.5,
            background_line_style={"stroke_color": GREY, "stroke_width": 2},
        ).shift(LEFT * 1.3 + UP * 0.1)
        # NumberPlane may be heavy; use manual grid
        axes = VGroup()
        O = LEFT * 2.8 + DOWN * 1.6
        for i in range(4):
            axes.add(Line(O + RIGHT * i * 1.1, O + RIGHT * i * 1.1 + UP * 3.3, color=GREY, stroke_width=2))
            axes.add(Line(O + UP * i * 1.1, O + UP * i * 1.1 + RIGHT * 3.3, color=GREY, stroke_width=2))
        self.O = O
        self.play(Create(axes), run_time=1.2)
        note = self.ja_text("格子点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def paths(self):
        # path with east, north, northeast steps
        pts = [self.O, self.O + RIGHT * 1.1, self.O + RIGHT * 1.1 + UP * 1.1,
               self.O + RIGHT * 2.2 + UP * 2.2, self.O + RIGHT * 3.3 + UP * 3.3]
        path = VMobject(color=ORANGE, stroke_width=4)
        path.set_points_as_corners(pts)
        dots = VGroup(*[Dot(p, color=YELLOW, radius=0.08) for p in pts])
        cap = self.ja_text("3 種の歩み", font_size=24).move_to(self.note)
        self.play(Create(path), FadeIn(dots), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("道を数える", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"D(m,n)=\sum_k\binom{m}{k}\binom{n}{k}2^{k}").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
