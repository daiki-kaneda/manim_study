from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Vandermonde(PacedScene):
    """#293 ヴァンデルモンド：二項係数の畳み込み（約45秒）"""

    def construct(self):
        self.show_heading("ヴァンデルモンドの恒等式")
        self.draw_bins()
        self.convolve()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_bins(self):
        left = RoundedRectangle(width=2.2, height=1.2, corner_radius=0.1, color=BLUE, stroke_width=3)
        right = RoundedRectangle(width=2.2, height=1.2, corner_radius=0.1, color=TEAL, stroke_width=3)
        left.shift(LEFT * 2.6 + UP * 0.8)
        right.shift(RIGHT * 2.6 + UP * 0.8)
        l1 = MathTex(r"\binom{m}{k}", font_size=36).move_to(left)
        l2 = MathTex(r"\binom{n}{r-k}", font_size=36).move_to(right)
        self.play(FadeIn(left), FadeIn(l1), FadeIn(right), FadeIn(l2), run_time=1.4)
        note = self.ja_text("2 つの組", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.left, self.right = left, right

    def convolve(self):
        mid = RoundedRectangle(width=2.4, height=1.2, corner_radius=0.1, color=ORANGE, stroke_width=3)
        mid.shift(DOWN * 0.5)
        lab = MathTex(r"\binom{m+n}{r}", font_size=38).move_to(mid)
        a1 = Arrow(self.left.get_bottom(), mid.get_top() + LEFT * 0.4, buff=0.1, color=YELLOW, stroke_width=3)
        a2 = Arrow(self.right.get_bottom(), mid.get_top() + RIGHT * 0.4, buff=0.1, color=YELLOW, stroke_width=3)
        cap = self.ja_text("分けて足す", font_size=24).move_to(self.note)
        self.play(GrowArrow(a1), GrowArrow(a2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("全体の選び方", font_size=24).move_to(self.note)
        self.play(FadeIn(mid), FadeIn(lab), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\sum_k\binom{m}{k}\binom{n}{r-k}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sum_k\binom{m}{k}\binom{n}{r-k}=\binom{m+n}{r}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sum_k\binom{m}{k}\binom{n}{r-k}=\binom{m+n}{r}").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
