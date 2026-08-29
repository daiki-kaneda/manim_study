from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class MarkovChain(JapaneseScene):
    """#124 マルコフ連鎖（約90秒）"""

    def construct(self):
        self.show_heading("マルコフ連鎖")
        self.draw_states()
        self.show_formula()
        self.hold(1.2)

    def draw_states(self):
        a = Circle(radius=0.7, color=BLUE, fill_opacity=0.35, stroke_width=3).shift(LEFT * 2.6 + DOWN * 0.1)
        b = Circle(radius=0.7, color=GREEN, fill_opacity=0.35, stroke_width=3).shift(RIGHT * 2.2 + DOWN * 0.1)
        la = MathTex("A", font_size=36).move_to(a)
        lb = MathTex("B", font_size=36).move_to(b)
        ab = Arrow(a.get_right() + UP * 0.25, b.get_left() + UP * 0.25, buff=0.05, color=YELLOW, stroke_width=4)
        ba = Arrow(b.get_left() + DOWN * 0.25, a.get_right() + DOWN * 0.25, buff=0.05, color=ORANGE, stroke_width=4)
        pab = MathTex("0.3", color=YELLOW, font_size=28).next_to(ab, UP, buff=0.08)
        pba = MathTex("0.4", color=ORANGE, font_size=28).next_to(ba, DOWN, buff=0.08)
        self.play(FadeIn(a), FadeIn(b), FadeIn(la), FadeIn(lb), run_time=0.7)
        self.play(GrowArrow(ab), GrowArrow(ba), FadeIn(pab), FadeIn(pba), run_time=0.8)
        note = self.ja_text("次は今だけ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"P(X_{n+1}\mid X_n,\ldots)=P(X_{n+1}\mid X_n)").scale(0.78)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
