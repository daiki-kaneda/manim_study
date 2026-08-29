from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AreaInteraction(PacedScene):
    """#772 面積相互作用：合併領域の面積で相互作用（約45秒）"""

    def construct(self):
        self.show_heading("面積相互作用")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        c1 = Circle(radius=0.9, color=BLUE, stroke_width=3, fill_opacity=0.2).shift(LEFT * 0.7 + UP * 0.2)
        c2 = Circle(radius=0.9, color=ORANGE, stroke_width=3, fill_opacity=0.2).shift(RIGHT * 0.7 + UP * 0.2)
        self.play(Create(c1), Create(c2), run_time=1.3)
        note = self.ja_text("球の合併面積", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("重なりを測る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ギブス型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"p\propto\exp(-a|\cup B(x_i)|)").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
