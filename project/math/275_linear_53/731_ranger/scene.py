from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Ranger(PacedScene):
    """#731 Ranger：RAdam と Lookahead の組み合わせ（約45秒）"""

    def construct(self):
        self.show_heading("Ranger")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        a = RoundedRectangle(width=2.4, height=1.2, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.3)
        b = RoundedRectangle(width=2.4, height=1.2, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.3)
        self.play(Create(a), Create(b),
                  FadeIn(MathTex(r"RAdam", font_size=28).move_to(a)),
                  FadeIn(MathTex(r"Lookahead", font_size=26).move_to(b)), run_time=1.4)

        note = self.ja_text("二つを合成", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("安定と平滑", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("実践的オプティマイザ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Ranger=Lookahead(RAdam)").scale(0.75)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
