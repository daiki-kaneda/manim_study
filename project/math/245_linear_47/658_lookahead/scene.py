from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Lookahead(PacedScene):
    """#658 Lookahead：速い重みを遅い重みへ補間（約45秒）"""

    def construct(self):
        self.show_heading("Lookahead")
        self.draw_two()
        self.interp()
        self.show_formula()
        self.read(1.4)

    def draw_two(self):
        fast = Dot(LEFT * 2 + UP * 0.8, color=ORANGE, radius=0.12)
        slow = Dot(LEFT * 2 + DOWN * 0.6, color=BLUE, radius=0.12)
        path_f = VMobject(color=ORANGE, stroke_width=3).set_points_as_corners(
            [LEFT*2+UP*0.8, ORIGIN+UP*1.0, RIGHT*1.5+UP*0.5, RIGHT*2.5+UP*0.9])
        path_s = VMobject(color=BLUE, stroke_width=3).set_points_as_corners(
            [LEFT*2+DOWN*0.6, ORIGIN+DOWN*0.2, RIGHT*1.5+DOWN*0.1])
        self.play(FadeIn(fast), FadeIn(slow), Create(path_f), Create(path_s), run_time=1.4)
        note = self.ja_text("速い・遅い重み", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def interp(self):
        cap = self.ja_text("k 歩ごとに同期", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("振動を平滑化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\phi\leftarrow\phi+\alpha(\theta-\phi)").scale(0.8)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
