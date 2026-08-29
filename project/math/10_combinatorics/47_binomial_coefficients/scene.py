from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class BinomialCoefficients(JapaneseScene):
    """#47 二項定理の係数（約90秒）"""

    def construct(self):
        self.show_heading("二項定理")
        self.show_expansions()
        self.show_formula()
        self.hold(1.2)

    def show_expansions(self):
        lines = VGroup(
            MathTex(r"(a+b)^0=1", font_size=34),
            MathTex(r"(a+b)^1=a+b", font_size=34),
            MathTex(r"(a+b)^2=a^2+2ab+b^2", font_size=34),
            MathTex(r"(a+b)^3=a^3+3a^2b+3ab^2+b^3", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        lines.shift(UP * 0.55)
        for i, line in enumerate(lines):
            self.play(FadeIn(line, shift=DOWN * 0.12), run_time=0.45)
            self.hold(0.4 if i < 3 else 0.65)
        self.lines = lines

    def show_formula(self):
        formula = MathTex(r"(a+b)^n=\sum_{k=0}^{n}\binom{n}{k}a^{n-k}b^k").scale(0.85)
        formula.to_edge(DOWN, buff=0.38)
        note = self.ja_text("係数はパスカルの三角形", font_size=24)
        note.next_to(formula, UP, buff=0.16)
        self.play(Write(formula), FadeIn(note), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
