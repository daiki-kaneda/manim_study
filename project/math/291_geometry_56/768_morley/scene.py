from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MorleyTriangle(PacedScene):
    """#768 モーリー三角形：三等分線がつくる正三角形（約45秒）"""

    def construct(self):
        self.show_heading("モーリー三角形")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.7 + DOWN * 1.2, RIGHT * 2.7 + DOWN * 1.2, UP * 1.8, color=BLUE, stroke_width=3)
        inner = Polygon(LEFT * 0.6 + DOWN * 0.2, RIGHT * 0.6 + DOWN * 0.2, UP * 0.7, color=ORANGE, stroke_width=3)
        self.play(Create(tri), Create(inner), run_time=1.3)
        note = self.ja_text("角を三等分", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("内側が正三角形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("一意に定まる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\triangle_M\ \mathrm{equilateral}").scale(0.8)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
