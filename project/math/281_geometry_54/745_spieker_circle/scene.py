from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SpiekerCircle(PacedScene):
    """#745 シュピーカー円：中点三角形の内接円（約45秒）"""

    def construct(self):
        self.show_heading("シュピーカー円")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.7 + DOWN * 1.2, RIGHT * 2.7 + DOWN * 1.2, UP * 1.8, color=BLUE, stroke_width=3)
        A, B, C = LEFT * 2.7 + DOWN * 1.2, RIGHT * 2.7 + DOWN * 1.2, UP * 1.8
        mids = VGroup(*[Dot((P + Q) / 2, color=YELLOW, radius=0.07) for P, Q in [(A, B), (B, C), (C, A)]])
        medial = Polygon(*[m.get_center() for m in mids], color=ORANGE, stroke_width=3)
        circ = Circle(radius=0.55, color=TEAL, stroke_width=3).move_to(medial.get_center_of_mass())
        self.play(Create(tri), FadeIn(mids), Create(medial), Create(circ), run_time=1.5)
        note = self.ja_text("中点三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("その内接円", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("周長の重心が中心", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Sp=\mathrm{incenter}(m(\triangle))").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
