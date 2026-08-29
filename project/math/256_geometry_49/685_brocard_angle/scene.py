from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BrocardAngle(PacedScene):
    """#685 ブロカール角：ブロカール点を定める角（約45秒）"""

    def construct(self):
        self.show_heading("ブロカール角")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        arc = Arc(radius=1.2, start_angle=0.2, angle=0.7, color=ORANGE, stroke_width=4).shift(LEFT * 0.5 + DOWN * 0.2)
        self.play(Create(Polygon(LEFT * 2.5 + DOWN * 1.1, RIGHT * 2.5 + DOWN * 1.1, UP * 1.7, color=BLUE, stroke_width=3)), Create(arc), run_time=1.4)

        note = self.ja_text("唯一の角 ω", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("点を決める", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("公式で計算", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\cot\omega=\frac{a^2+b^2+c^2}{4K}").scale(0.78)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
