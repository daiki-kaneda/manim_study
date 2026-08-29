from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class SumOfCubes(JapaneseScene):
    """#14 a³+b³ の因数分解（約90秒）"""

    def construct(self):
        self.show_heading("a³ + b³ の因数分解")
        self.show_start()
        self.expand_product()
        self.conclude()
        self.hold(1.2)

    def show_start(self):
        start = MathTex(r"a^3+b^3").scale(1.6)
        start.shift(UP * 1.4)
        self.play(Write(start), run_time=0.8)
        self.hold(0.6)
        self.start = start

    def expand_product(self):
        product = MathTex(r"(a+b)(a^2-ab+b^2)").scale(1.2)
        product.next_to(self.start, DOWN, buff=0.55)
        self.play(TransformMatchingTex(self.start.copy(), product), run_time=1.0)
        self.hold(0.7)

        step1 = MathTex(r"=a\cdot a^2+a(-ab)+a\cdot b^2+b\cdot a^2+b(-ab)+b\cdot b^2").scale(0.7)
        step1.next_to(product, DOWN, buff=0.45)
        self.play(Write(step1), run_time=1.2)
        self.hold(0.8)

        step2 = MathTex(r"=a^3-a^2b+ab^2+a^2b-ab^2+b^3").scale(0.85)
        step2.next_to(step1, DOWN, buff=0.4)
        self.play(Write(step2), run_time=1.0)
        self.hold(0.7)

        cancel = self.ja_text("打ち消し合う項", font_size=24)
        cancel.next_to(step2, DOWN, buff=0.3)
        self.play(FadeIn(cancel), run_time=0.4)
        self.hold(0.7)
        self.play(FadeOut(cancel), FadeOut(step1), run_time=0.4)
        self.product = product
        self.step2 = step2

    def conclude(self):
        result = MathTex(r"a^3+b^3=(a+b)(a^2-ab+b^2)").scale(1.15)
        result.to_edge(DOWN, buff=0.45)
        self.play(Write(result), run_time=1.0)
        self.play(Indicate(result, color=BLUE), run_time=0.8)
        self.hold(1.3)
