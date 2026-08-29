from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Bayes(JapaneseScene):
    """#25 ベイズの定理（面積モデル、約90秒）"""

    def construct(self):
        self.show_heading("ベイズの定理")
        self.draw_prior()
        self.shade_evidence()
        self.show_formula()
        self.hold(1.2)

    def draw_prior(self):
        # 見やすい比率: P(A)=0.4, 全体は幅 6.4 × 高さ 3.2
        self.W, self.H = 6.4, 3.2
        self.origin = LEFT * 3.5 + DOWN * 1.55
        self.wa = 0.4 * self.W
        frame = Rectangle(width=self.W, height=self.H, color=WHITE, stroke_width=2)
        frame.move_to(self.origin + RIGHT * (self.W / 2) + UP * (self.H / 2))
        a_box = Rectangle(width=self.wa, height=self.H, color=BLUE, fill_opacity=0.55, stroke_width=1)
        a_box.move_to(self.origin + RIGHT * (self.wa / 2) + UP * (self.H / 2))
        ac_box = Rectangle(
            width=self.W - self.wa, height=self.H, color=GREY, fill_opacity=0.25, stroke_width=1
        )
        ac_box.move_to(self.origin + RIGHT * (self.wa + (self.W - self.wa) / 2) + UP * (self.H / 2))
        self.play(Create(frame), run_time=0.5)
        self.play(FadeIn(a_box), FadeIn(ac_box), run_time=0.7)
        lab_a = VGroup(self.ja_text("事象 A", font_size=24), MathTex(r"P(A)", font_size=28)).arrange(
            DOWN, buff=0.1
        )
        lab_a.move_to(a_box.get_center() + DOWN * 0.15)
        lab_ac = VGroup(self.ja_text("A 以外", font_size=24), MathTex(r"P(A^c)", font_size=28)).arrange(
            DOWN, buff=0.1
        )
        lab_ac.move_to(ac_box.get_center() + DOWN * 0.15)
        self.play(FadeIn(lab_a), FadeIn(lab_ac), run_time=0.5)
        prior = self.ja_text("事前", font_size=26).to_edge(RIGHT, buff=0.45).shift(UP * 1.85)
        self.play(FadeIn(prior), run_time=0.35)
        self.hold(0.7)
        self.a_box, self.ac_box = a_box, ac_box
        self.lab_a, self.lab_ac, self.prior = lab_a, lab_ac, prior

    def shade_evidence(self):
        # P(B|A)=0.75, P(B|A^c)=0.25
        ha = 0.75 * self.H
        hac = 0.25 * self.H
        b_a = Rectangle(width=self.wa, height=ha, color=YELLOW, fill_opacity=0.75, stroke_width=1)
        b_a.move_to(self.origin + RIGHT * (self.wa / 2) + UP * (self.H - ha / 2))
        b_ac = Rectangle(
            width=self.W - self.wa, height=hac, color=YELLOW, fill_opacity=0.75, stroke_width=1
        )
        b_ac.move_to(
            self.origin + RIGHT * (self.wa + (self.W - self.wa) / 2) + UP * (self.H - hac / 2)
        )
        self.play(FadeOut(self.lab_a), FadeOut(self.lab_ac), run_time=0.3)
        self.play(FadeIn(b_a), FadeIn(b_ac), run_time=0.8)
        ev = self.ja_text("B が起きた部分", font_size=26).move_to(self.prior)
        self.play(Transform(self.prior, ev), run_time=0.4)
        ba = MathTex(r"P(B\mid A)", font_size=26, color=YELLOW)
        ba.next_to(b_a, UP, buff=0.12)
        self.play(FadeIn(ba), run_time=0.4)
        self.hold(0.8)
        highlight = SurroundingRectangle(VGroup(b_a, b_ac), color=YELLOW, buff=0.06)
        self.play(Create(highlight), run_time=0.5)
        post = self.ja_text("黄色い面積のうち、A 側の割合が事後", font_size=24)
        post.to_edge(DOWN, buff=1.15)
        self.play(FadeIn(post), run_time=0.5)
        self.hold(0.9)
        self.post_note = post

    def show_formula(self):
        formula = MathTex(r"P(A\mid B)=\dfrac{P(B\mid A)\,P(A)}{P(B)}").scale(0.95)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeOut(self.post_note), run_time=0.3)
        self.play(Write(formula), run_time=1.15)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
