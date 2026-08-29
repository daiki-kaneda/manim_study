from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class JointDensity(PacedScene):
    """#184 同時密度は山、周辺は押しつぶし（約45秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 1.5
        self.show_heading("同時分布")
        self.draw_contours()
        self.marginalize()
        self.show_formula()
        self.read(1.4)

    def draw_contours(self):
        ax = Line(self.origin + LEFT * 0.3, self.origin + RIGHT * 5.6, color=GREY, stroke_width=2)
        ay = Line(self.origin + DOWN * 0.3, self.origin + UP * 3.5, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        center = self.origin + RIGHT * 2.3 + UP * 1.7
        ells = VGroup()
        for w, h, op in ((2.8, 1.8, 0.12), (1.9, 1.2, 0.2), (1.1, 0.7, 0.35)):
            e = Ellipse(width=w, height=h, color=BLUE, fill_opacity=op, stroke_width=3)
            e.rotate(25 * DEGREES).move_to(center)
            ells.add(e)
        self.play(LaggedStart(*[FadeIn(e) for e in ells], lag_ratio=0.2), run_time=1.8)
        note = self.ja_text("同時の山", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note
        self.center = center

    def marginalize(self):
        xs = [self.origin + RIGHT * (0.6 + 0.55 * i) for i in range(8)]
        heights = [0.4, 0.9, 1.6, 2.2, 2.0, 1.3, 0.7, 0.3]
        bars = VGroup()
        for x, h in zip(xs, heights):
            bars.add(Line(x, x + UP * h, color=YELLOW, stroke_width=8))
        cap = self.ja_text("潰して周辺", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(b) for b in bars], lag_ratio=0.08), Transform(self.note, cap), run_time=2.0)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"f_X(x)=\int f_{X,Y}(x,y)\,dy").scale(0.88)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
