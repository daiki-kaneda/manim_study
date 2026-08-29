from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ChainRule(JapaneseScene):
    """#18 チェーンルール（約90秒）"""

    def construct(self):
        self.show_heading("合成関数の微分")
        self.show_composition()
        self.show_example()
        self.show_formula()
        self.hold(1.2)

    def show_composition(self):
        boxes = VGroup(
            MathTex("x", font_size=40),
            MathTex(r"\xrightarrow{\,g\,}", font_size=36),
            MathTex("u", font_size=40),
            MathTex(r"\xrightarrow{\,f\,}", font_size=36),
            MathTex("y", font_size=40),
        ).arrange(RIGHT, buff=0.25)
        boxes.shift(UP * 1.55)
        self.play(FadeIn(boxes), run_time=0.8)
        note = self.ja_text("内側の変化 × 外側の変化", font_size=26)
        note.next_to(boxes, DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=0.5)
        self.hold(0.8)
        self.boxes, self.note = boxes, note

    def show_example(self):
        ex = VGroup(
            MathTex(r"u=2x,\quad y=u^2", font_size=36),
            MathTex(r"y=(2x)^2=4x^2", font_size=36),
            MathTex(r"y'=8x", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        ex.shift(DOWN * 0.15 + LEFT * 1.6)
        for line in ex:
            self.play(FadeIn(line), run_time=0.45)
            self.hold(0.4)
        check = MathTex(r"f'(u)g'(x)=2u\cdot 2=4x\cdot 2=8x", font_size=32)
        check.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.2)
        self.play(FadeIn(check), run_time=0.6)
        self.hold(0.8)
        self.check = check

    def show_formula(self):
        formula = MathTex(r"\frac{dy}{dx}=\frac{dy}{du}\cdot\frac{du}{dx}").scale(1.15)
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=BLUE), run_time=0.8)
        self.hold(1.2)
