from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CosineCircle(PacedScene):
    """#722 余弦円：辺を余弦比で内分する点の円（約45秒）"""

    def construct(self):
        self.show_heading("余弦円")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.6 + DOWN * 1.1, RIGHT * 2.6 + DOWN * 1.1, UP * 1.7, color=BLUE, stroke_width=3)
        circ = Circle(radius=1.15, color=TEAL, stroke_width=3).shift(UP * 0.05)
        self.play(Create(tri), Create(circ), run_time=1.3)

        note = self.ja_text("余弦で内分", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("第1・第2余弦円", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ルモワーヌと関係", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"AX:XB=b\cos B:c\cos C").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
