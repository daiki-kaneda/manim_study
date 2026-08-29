from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Resolvent(PacedScene):
    """#299 レゾルベント：(zI−A)^{-1} が正則な領域（約45秒）"""

    def construct(self):
        self.show_heading("レゾルベント")
        self.draw_plane()
        self.holes()
        self.show_formula()
        self.read(1.4)

    def draw_plane(self):
        self.O = LEFT * 0.4 + DOWN * 0.1
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 3.0, color=GREY, stroke_width=2)
        ay = Line(self.O + DOWN * 2.0, self.O + UP * 2.0, color=GREY, stroke_width=2)
        self.play(Create(ax), Create(ay), run_time=0.8)
        note = self.ja_text("複素平面", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def holes(self):
        holes = VGroup(*[
            Dot(self.O + RIGHT * x + UP * y, color=ORANGE, radius=0.12)
            for x, y in [(1.4, 0.6), (-1.0, -0.8), (0.3, 1.3)]
        ])
        # shaded resolvent region hint
        region = Circle(radius=2.4, color=BLUE, fill_opacity=0.15, stroke_width=2).move_to(self.O)
        cap = self.ja_text("固有値の穴", font_size=24).move_to(self.note)
        self.play(FadeIn(region), FadeIn(holes), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("外では正則", font_size=24).move_to(self.note)
        z = MathTex(r"z", color=YELLOW, font_size=36).move_to(self.O + LEFT * 1.6 + UP * 1.2)
        self.play(FadeIn(z), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"R(z,A)=(zI-A)^{-1}").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
