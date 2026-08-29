from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BrocardMidpoint(PacedScene):
    """#710 ブロカール中点：二つのブロカール点の中点（約45秒）"""

    def construct(self):
        self.show_heading("ブロカール中点")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.6 + DOWN * 1.2, RIGHT * 2.6 + DOWN * 1.2, UP * 1.8, color=BLUE, stroke_width=3)
        O1 = Dot(LEFT * 0.4 + UP * 0.2, color=YELLOW, radius=0.09)
        O2 = Dot(RIGHT * 0.4 + UP * 0.05, color=ORANGE, radius=0.09)
        M = Dot((O1.get_center() + O2.get_center()) / 2, color=TEAL, radius=0.1)
        self.play(Create(tri), FadeIn(O1), FadeIn(O2), FadeIn(M),
                  Create(DashedLine(O1.get_center(), O2.get_center(), color=GREY)), run_time=1.4)

        note = self.ja_text("Ω と Ω'", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("中点が特殊点", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ブロカール円の弦", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M=\tfrac12(\Omega+\Omega')").scale(0.8)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
