from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class HarmonicSeries(JapaneseScene):
    """#56 調和級数は発散する（約90秒）"""

    def construct(self):
        self.show_heading("調和級数")
        self.show_groups()
        self.show_formula()
        self.hold(1.2)

    def show_groups(self):
        series = MathTex(r"1+\frac12+\frac13+\frac14+\frac15+\cdots", font_size=36)
        series.shift(UP * 2.0)
        self.play(Write(series), run_time=0.8)
        self.hold(0.4)
        groups = VGroup(
            MathTex(r"1", font_size=34),
            MathTex(r"\frac12", font_size=34),
            MathTex(r"\frac13+\frac14>\frac12", font_size=34),
            MathTex(r"\frac15+\cdots+\frac18>\frac12", font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        groups.next_to(series, DOWN, buff=0.45).to_edge(LEFT, buff=1.1)
        for g in groups:
            self.play(FadeIn(g, shift=DOWN * 0.1), run_time=0.4)
            self.hold(0.4)
        note = self.ja_text("1/2 が無限に足せる", font_size=26)
        note.to_edge(RIGHT, buff=0.45).shift(DOWN * 0.2)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"H_n=1+\frac12+\cdots+\frac1n\to\infty").scale(0.95)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
