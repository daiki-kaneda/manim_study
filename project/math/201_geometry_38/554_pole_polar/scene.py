from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PolePolar(PacedScene):
    """#554 極と極線：円に関する双対対応（約45秒）"""

    def construct(self):
        self.show_heading("極と極線")
        self.draw_circle()
        self.polar()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        self.circ = Circle(radius=1.6, color=BLUE, stroke_width=3).shift(LEFT * 0.5 + UP * 0.1)
        self.play(Create(self.circ), run_time=1.1)
        note = self.ja_text("基準円", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def polar(self):
        P = LEFT * 0.5 + UP * 0.1 + RIGHT * 2.4 + UP * 0.3
        polar = Line(LEFT * 2.5 + UP * 1.3, RIGHT * 1.2 + DOWN * 1.5, color=ORANGE, stroke_width=4)
        tangents = VGroup(
            Line(P, LEFT * 0.5 + UP * 0.1 + RIGHT * 1.1 + UP * 1.15, color=GREY, stroke_width=2),
            Line(P, LEFT * 0.5 + UP * 0.1 + RIGHT * 1.3 + DOWN * 0.9, color=GREY, stroke_width=2),
        )
        dot = Dot(P, color=YELLOW, radius=0.1)
        cap = self.ja_text("点に直線が対応", font_size=24).move_to(self.note)
        self.play(FadeIn(dot), Create(tangents), Create(polar), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("配極変換", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"P\cdot X=r^2").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
