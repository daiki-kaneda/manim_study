from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HarmonicMap(PacedScene):
    """#678 調和写像：エネルギーを最小にする写像（約45秒）"""

    def construct(self):
        self.show_heading("調和写像")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        domain = Circle(radius=1.3, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        target = Circle(radius=1.3, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        arrow = Arrow(domain.get_right(), target.get_left(), buff=0.15, color=TEAL, stroke_width=4)
        self.play(Create(domain), Create(target), GrowArrow(arrow),
                  FadeIn(MathTex(r"M", font_size=28).move_to(domain)),
                  FadeIn(MathTex(r"N", font_size=28).move_to(target)), run_time=1.4)

        note = self.ja_text("エネルギー臨界", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("張力場ゼロ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("調和方程式", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\tau(u)=0").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
