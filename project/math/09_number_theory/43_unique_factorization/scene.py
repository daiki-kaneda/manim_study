from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class UniqueFactorization(JapaneseScene):
    """#43 素因数分解の一意性（約90秒）"""

    def construct(self):
        self.show_heading("素因数分解")
        self.show_number()
        self.split_tree()
        self.show_formula()
        self.hold(1.2)

    def show_number(self):
        n = MathTex("12", font_size=72)
        n.shift(UP * 2.0)
        self.play(FadeIn(n), run_time=0.6)
        self.hold(0.4)
        self.n = n

    def split_tree(self):
        two_a = MathTex("2", color=BLUE, font_size=48)
        six = MathTex("6", font_size=48)
        row1 = VGroup(two_a, six).arrange(RIGHT, buff=1.6)
        row1.next_to(self.n, DOWN, buff=0.7)
        self.play(FadeIn(two_a), FadeIn(six), run_time=0.6)
        self.hold(0.45)
        two_b = MathTex("2", color=BLUE, font_size=48)
        three = MathTex("3", color=GREEN, font_size=48)
        row2 = VGroup(two_b, three).arrange(RIGHT, buff=1.6)
        row2.next_to(six, DOWN, buff=0.7)
        self.play(FadeIn(two_b), FadeIn(three), run_time=0.6)
        self.hold(0.5)
        product = MathTex(r"12=2\cdot 2\cdot 3=2^2\cdot 3", font_size=36)
        product.next_to(row2, DOWN, buff=0.55)
        self.play(Write(product), run_time=0.8)
        self.hold(0.7)
        self.product = product

    def show_formula(self):
        note = self.ja_text("素数の積の表し方はひとつ", font_size=28)
        note.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(note), run_time=0.5)
        self.play(Indicate(self.product, color=YELLOW), run_time=0.7)
        self.hold(1.2)
