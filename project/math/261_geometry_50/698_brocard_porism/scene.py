from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BrocardPorism(PacedScene):
    """#698 ブロカールのポリズム：無限に続くブロカール配置（約45秒）"""

    def construct(self):
        self.show_heading("ブロカールのポリズム")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        c1 = Circle(radius=1.7, color=BLUE, stroke_width=3).shift(UP*0.1)
        c2 = Circle(radius=0.7, color=ORANGE, stroke_width=3).shift(UP*0.1)
        self.play(Create(c1), Create(c2), run_time=1.3)

        note = self.ja_text("円の連鎖", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("ポンスレ型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("無限家族", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\omega=\mathrm{const}").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
