from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import JapaneseScene


class BaselProblem(JapaneseScene):
    """#58 バーゼル問題 1/n² の和（約90秒）"""

    def construct(self):
        self.show_heading("1/n² の和")
        self.draw_squares()
        self.show_formula()
        self.hold(1.2)

    def draw_squares(self):
        # 1 + 1/4 + 1/9 + 1/16 を入れ子の正方形で
        origin = LEFT * 3.6 + DOWN * 1.7
        colors = [BLUE, GREEN, ORANGE, YELLOW, TEAL]
        side = 3.4
        labels = [r"1", r"1/4", r"1/9", r"1/16"]
        for i in range(4):
            s = side / (i + 1)
            sq = Square(side_length=s, color=colors[i], fill_opacity=0.55, stroke_width=1.5)
            sq.move_to(origin + RIGHT * (s / 2) + UP * (s / 2))
            lab = MathTex(labels[i], font_size=26).move_to(sq.get_center() if i == 0 else sq.get_corner(UR) + DL * 0.25)
            self.play(FadeIn(sq), FadeIn(lab), run_time=0.5)
            self.hold(0.3)
        note = self.ja_text("面積はどんどん小さくなる", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.6)

    def show_formula(self):
        formula = MathTex(r"1+\frac1{4}+\frac1{9}+\frac1{16}+\cdots=\frac{\pi^2}{6}").scale(0.9)
        formula.to_edge(DOWN, buff=0.38)
        val = MathTex(rf"\approx {math.pi ** 2 / 6:.3f}", font_size=28)
        val.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(val), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
