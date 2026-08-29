from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HomologicalMirror(PacedScene):
    """#726 ホモロジカルミラー：深谷圏と連接層の圏同値（約45秒）"""

    def construct(self):
        self.show_heading("ホモロジカルミラー")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        left = RoundedRectangle(width=2.5, height=1.4, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        right = RoundedRectangle(width=2.5, height=1.4, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        arrow = Arrow(left.get_right(), right.get_left(), buff=0.12, color=TEAL, stroke_width=4)
        self.play(Create(left), Create(right), GrowArrow(arrow),
                  FadeIn(MathTex(r"Fuk(X)", font_size=28).move_to(left)),
                  FadeIn(MathTex(r"D^b(X^*)", font_size=26).move_to(right)), run_time=1.4)

        note = self.ja_text("圏の同値", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("Kontsevich予想", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ミラーの精密化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Fuk(X)\simeq D^b(X^\vee)").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
