from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class EuclidGCD(JapaneseScene):
    """#41 ユークリッドの互除法（約90秒）"""

    def construct(self):
        self.show_heading("最大公約数")
        self.draw_rect()
        self.tile()
        self.show_formula()
        self.hold(1.2)

    def draw_rect(self):
        # 21×15 を縮小。1 単位 = 0.18
        self.s = 0.18
        self.origin = LEFT * 3.6 + DOWN * 1.55
        w, h = 21 * self.s, 15 * self.s
        self.rect = Rectangle(width=w, height=h, color=WHITE, stroke_width=2)
        self.rect.move_to(self.origin + RIGHT * (w / 2) + UP * (h / 2))
        cap = VGroup(
            self.ja_text("長方形", font_size=24),
            MathTex(r"21\times 15", font_size=32),
        ).arrange(DOWN, buff=0.1)
        cap.to_edge(RIGHT, buff=0.45).shift(UP * 1.6)
        self.play(Create(self.rect), FadeIn(cap), run_time=0.8)
        self.hold(0.5)
        self.cap = cap

    def _sq(self, x, y, side, color):
        sq = Square(side_length=side * self.s, color=color, fill_opacity=0.7, stroke_width=1)
        sq.move_to(self.origin + RIGHT * ((x + side / 2) * self.s) + UP * ((y + side / 2) * self.s))
        return sq

    def tile(self):
        # 15×15 を1つ
        s1 = self._sq(0, 0, 15, BLUE)
        self.play(FadeIn(s1), run_time=0.5)
        self.play(Transform(self.cap, MathTex(r"21=15\cdot 1+6", font_size=32).move_to(self.cap)), run_time=0.4)
        self.hold(0.55)
        # 残り 6×15 に 6×6 を2つ
        s2 = self._sq(15, 0, 6, GREEN)
        s3 = self._sq(15, 6, 6, GREEN)
        self.play(FadeIn(s2), FadeIn(s3), run_time=0.55)
        self.play(Transform(self.cap, MathTex(r"15=6\cdot 2+3", font_size=32).move_to(self.cap)), run_time=0.4)
        self.hold(0.55)
        # 残り 6×3 に 3×3 を2つ
        s4 = self._sq(15, 12, 3, YELLOW)
        s5 = self._sq(18, 12, 3, YELLOW)
        self.play(FadeIn(s4), FadeIn(s5), run_time=0.55)
        self.play(Transform(self.cap, MathTex(r"6=3\cdot 2+0", font_size=32).move_to(self.cap)), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\gcd(21,15)=3").scale(1.15)
        formula.to_edge(DOWN, buff=0.38)
        note = self.ja_text("最後に残る正方形の辺", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(note), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
