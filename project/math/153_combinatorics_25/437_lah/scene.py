from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LahNumbers(PacedScene):
    """#437 ラホール数：順序付き分割の数（約45秒）"""

    def construct(self):
        self.show_heading("ラホール数")
        self.draw_blocks()
        self.order()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        els = VGroup(*[Dot(LEFT * 2.4 + RIGHT * i * 0.75 + UP * 1.1, color=BLUE, radius=0.11) for i in range(5)])
        b1 = SurroundingRectangle(VGroup(els[0], els[1], els[2]), color=ORANGE, buff=0.2)
        b2 = SurroundingRectangle(VGroup(els[3], els[4]), color=TEAL, buff=0.2)
        self.play(FadeIn(els), Create(b1), Create(b2), run_time=1.4)
        note = self.ja_text("ブロック分割", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def order(self):
        arrows = VGroup(
            MathTex(r"1\to 2\to 3", font_size=28, color=ORANGE).shift(LEFT * 1.6 + DOWN * 0.2),
            MathTex(r"4\to 5", font_size=28, color=TEAL).shift(RIGHT * 0.9 + DOWN * 0.2),
        )
        cap = self.ja_text("中を並べる", font_size=24).move_to(self.note)
        self.play(FadeIn(arrows), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("順序付き分割", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"L(n,k)=\frac{n!}{k!}\binom{n-1}{k-1}").scale(0.9)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
