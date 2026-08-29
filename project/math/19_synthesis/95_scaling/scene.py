from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Scaling(JapaneseScene):
    """#95 長さ・面積・体積のスケール（約90秒）"""

    def construct(self):
        self.show_heading("スケール")
        self.grow_square()
        self.show_formula()
        self.hold(1.2)

    def grow_square(self):
        small = Square(side_length=1.1, color=BLUE, fill_opacity=0.5, stroke_width=2)
        small.move_to(LEFT * 3.3 + DOWN * 0.2)
        lab1 = MathTex("L", font_size=28).next_to(small, DOWN, buff=0.15)
        self.play(FadeIn(small), FadeIn(lab1), run_time=0.55)
        big = Square(side_length=2.2, color=YELLOW, fill_opacity=0.4, stroke_width=2)
        big.move_to(RIGHT * 1.6 + DOWN * 0.05)
        lab2 = MathTex("2L", font_size=28).next_to(big, DOWN, buff=0.15)
        self.play(FadeIn(big), FadeIn(lab2), run_time=0.7)
        note = self.ja_text("面積は 4 倍", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"A\propto L^{2},\quad V\propto L^{3}").scale(1.1)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
