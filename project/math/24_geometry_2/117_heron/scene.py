from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Heron(JapaneseScene):
    """#117 ヘロンの公式（約90秒）"""

    def construct(self):
        self.show_heading("ヘロンの公式")
        self.draw_triangle()
        self.show_formula()
        self.hold(1.2)

    def draw_triangle(self):
        A = LEFT * 2.6 + UP * 1.55
        B = LEFT * 3.5 + DOWN * 1.4
        C = RIGHT * 0.7 + DOWN * 1.2
        tri = Polygon(A, B, C, color=WHITE, stroke_width=3, fill_opacity=0.2, fill_color=BLUE)
        self.play(Create(tri), run_time=0.7)
        a = MathTex("a", color=YELLOW, font_size=32).move_to((B + C) / 2 + DOWN * 0.32)
        b = MathTex("b", color=YELLOW, font_size=32).move_to((A + C) / 2 + RIGHT * 0.28)
        c = MathTex("c", color=YELLOW, font_size=32).move_to((A + B) / 2 + LEFT * 0.28)
        self.play(FadeIn(a), FadeIn(b), FadeIn(c), run_time=0.5)
        note = self.ja_text("半周 s", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"A=\sqrt{s(s-a)(s-b)(s-c)}").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
