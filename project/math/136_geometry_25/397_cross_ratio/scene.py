from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CrossRatio(PacedScene):
    """#397 クロス比：射影不変量 (A,B;C,D)（約45秒）"""

    def construct(self):
        self.show_heading("クロス比")
        self.draw_points()
        self.project()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        self.line = Line(LEFT * 3.3, RIGHT * 3.3, color=GREY, stroke_width=3).shift(UP * 0.9)
        xs = [-2.4, -0.6, 0.8, 2.5]
        names = ["A", "B", "C", "D"]
        colors = [BLUE, TEAL, ORANGE, RED]
        self.dots = VGroup()
        labs = VGroup()
        for x, n, c in zip(xs, names, colors):
            d = Dot(self.line.point_from_proportion((x + 3.3) / 6.6), color=c, radius=0.1)
            lab = MathTex(n, font_size=28).next_to(d, UP, buff=0.15)
            self.dots.add(d)
            labs.add(lab)
        self.play(Create(self.line), FadeIn(self.dots), FadeIn(labs), run_time=1.4)
        note = self.ja_text("4 点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def project(self):
        # second line with projected points (same cross ratio look)
        line2 = Line(LEFT * 3.0 + DOWN * 1.3, RIGHT * 3.0 + DOWN * 0.7, color=GREY, stroke_width=3)
        xs2 = [-2.0, -0.2, 1.0, 2.3]
        dots2 = VGroup(*[
            Dot(line2.point_from_proportion((x + 3.0) / 6.0), color=c, radius=0.09)
            for x, c in zip(xs2, [BLUE, TEAL, ORANGE, RED])
        ])
        rays2 = VGroup(*[
            DashedLine(self.dots[i].get_center(), dots2[i].get_center(), color=YELLOW, stroke_width=1.5)
            for i in range(4)
        ])
        cap = self.ja_text("射影しても", font_size=24).move_to(self.note)
        self.play(Create(line2), FadeIn(dots2), Transform(self.note, cap), run_time=1.2)
        self.play(LaggedStart(*[Create(r) for r in rays2], lag_ratio=0.08), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("比は不変", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"(A,B;C,D)=\frac{(C-A)/(D-A)}{(C-B)/(D-B)}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
