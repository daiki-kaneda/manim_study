from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Iff(JapaneseScene):
    """#65 必要十分条件（約90秒）"""

    def construct(self):
        self.show_heading("必要十分")
        self.show_two_arrows()
        self.show_formula()
        self.hold(1.2)

    def show_two_arrows(self):
        p = MathTex("P", font_size=56)
        q = MathTex("Q", font_size=56)
        p.shift(LEFT * 2.4 + UP * 0.35)
        q.shift(RIGHT * 2.4 + UP * 0.35)
        self.play(FadeIn(p), FadeIn(q), run_time=0.5)
        fwd = Arrow(p.get_right() + RIGHT * 0.15, q.get_left() + LEFT * 0.15, buff=0, color=BLUE, stroke_width=5)
        fwd.shift(UP * 0.22)
        back = Arrow(q.get_left() + LEFT * 0.15, p.get_right() + RIGHT * 0.15, buff=0, color=GREEN, stroke_width=5)
        back.shift(DOWN * 0.22)
        self.play(GrowArrow(fwd), run_time=0.55)
        n1 = self.ja_text("十分", font_size=24, color=BLUE).next_to(fwd, UP, buff=0.12)
        self.play(FadeIn(n1), run_time=0.3)
        self.hold(0.45)
        self.play(GrowArrow(back), run_time=0.55)
        n2 = self.ja_text("必要", font_size=24, color=GREEN).next_to(back, DOWN, buff=0.12)
        self.play(FadeIn(n2), run_time=0.3)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"P\iff Q").scale(1.4)
        formula.to_edge(DOWN, buff=0.55)
        note = self.ja_text("両方向なら同じ", font_size=26)
        note.next_to(formula, UP, buff=0.25)
        self.play(Write(formula), FadeIn(note), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
