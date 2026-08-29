from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class InclusionExclusion(JapaneseScene):
    """#48 包除原理（約90秒）"""

    def construct(self):
        self.show_heading("包除原理")
        self.draw_sets()
        self.count()
        self.show_formula()
        self.hold(1.2)

    def draw_sets(self):
        self.c1 = Circle(radius=1.55, color=BLUE, fill_opacity=0.45, stroke_width=2).shift(LEFT * 0.85 + DOWN * 0.15)
        self.c2 = Circle(radius=1.55, color=ORANGE, fill_opacity=0.45, stroke_width=2).shift(RIGHT * 0.85 + DOWN * 0.15)
        la = MathTex("A", color=BLUE, font_size=36).next_to(self.c1, UL, buff=0.05)
        lb = MathTex("B", color=ORANGE, font_size=36).next_to(self.c2, UR, buff=0.05)
        self.play(FadeIn(self.c1), FadeIn(self.c2), FadeIn(la), FadeIn(lb), run_time=0.8)
        self.hold(0.5)

    def count(self):
        # 数字を配置: A only 4, intersection 2, B only 5
        n_a = MathTex("4", font_size=34).move_to(self.c1.get_center() + LEFT * 0.55)
        n_i = MathTex("2", font_size=34).move_to((self.c1.get_center() + self.c2.get_center()) / 2)
        n_b = MathTex("5", font_size=34).move_to(self.c2.get_center() + RIGHT * 0.55)
        self.play(FadeIn(n_a), FadeIn(n_i), FadeIn(n_b), run_time=0.6)
        add = MathTex(r"|A|+|B|=6+7=13", font_size=32).to_edge(RIGHT, buff=0.35).shift(UP * 1.55)
        self.play(FadeIn(add), run_time=0.45)
        self.hold(0.5)
        wrong = self.ja_text("共通の 2 を二重に数えている", font_size=22)
        wrong.next_to(add, DOWN, buff=0.3)
        self.play(FadeIn(wrong), run_time=0.4)
        self.hold(0.7)
        self.add_eq = add

    def show_formula(self):
        formula = MathTex(r"|A\cup B|=|A|+|B|-|A\cap B|").scale(0.95)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
