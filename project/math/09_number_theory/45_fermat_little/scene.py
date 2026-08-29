from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class FermatLittle(JapaneseScene):
    """#45 フェルマーの小定理（約90秒）"""

    beat = 2.6

    def construct(self):
        self.show_heading("フェルマーの小定理")
        self.show_powers()
        self.show_formula()
        self.hold(1.2)

    def show_powers(self):
        p = MathTex(r"p=5", font_size=40).shift(UP * 2.05)
        self.play(FadeIn(p), run_time=0.45)
        self.hold(0.4)
        rows = VGroup(
            MathTex(r"2^1=2", font_size=36),
            MathTex(r"2^2=4", font_size=36),
            MathTex(r"2^3=8\equiv 3", font_size=36),
            MathTex(r"2^4=16\equiv 1", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        rows.shift(LEFT * 2.4 + DOWN * 0.15)
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=DOWN * 0.1), run_time=0.4)
            self.hold(0.45 if i < 3 else 0.7)
        three = MathTex(r"3^4=81\equiv 1\pmod{5}", font_size=34)
        three.to_edge(RIGHT, buff=0.45).shift(DOWN * 0.1)
        self.play(FadeIn(three), run_time=0.55)
        self.hold(0.7)
        self.last = rows[-1]

    def show_formula(self):
        formula = MathTex(r"a^{p-1}\equiv 1\pmod{p}").scale(1.1)
        formula.to_edge(DOWN, buff=0.4)
        note = self.ja_text("p が素数、p が a を割らない", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(note), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
