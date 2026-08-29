from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Independence(JapaneseScene):
    """#38 独立：面積が積になる（約90秒）"""

    def construct(self):
        self.show_heading("独立")
        self.draw_grid()
        self.highlight_product()
        self.show_formula()
        self.hold(1.2)

    def draw_grid(self):
        # 幅 6.2, 高さ 3.4。A が左 40%、B が上 30%
        self.W, self.H = 6.2, 3.4
        self.origin = LEFT * 3.4 + DOWN * 1.55
        wa, hb = 0.4 * self.W, 0.3 * self.H
        frame = Rectangle(width=self.W, height=self.H, color=WHITE, stroke_width=2)
        frame.move_to(self.origin + RIGHT * (self.W / 2) + UP * (self.H / 2))
        vline = Line(
            self.origin + RIGHT * wa,
            self.origin + RIGHT * wa + UP * self.H,
            color=GREY,
            stroke_width=2,
        )
        hline = Line(
            self.origin + UP * (self.H - hb),
            self.origin + UP * (self.H - hb) + RIGHT * self.W,
            color=GREY,
            stroke_width=2,
        )
        self.play(Create(frame), run_time=0.5)
        self.play(Create(vline), Create(hline), run_time=0.6)
        lab_a = VGroup(self.ja_text("A", font_size=28), MathTex(r"P(A)", font_size=28)).arrange(DOWN, buff=0.08)
        lab_a.move_to(self.origin + RIGHT * (wa / 2) + UP * (self.H * 0.45))
        lab_b = VGroup(self.ja_text("B", font_size=28), MathTex(r"P(B)", font_size=28)).arrange(RIGHT, buff=0.12)
        lab_b.move_to(self.origin + RIGHT * (self.W * 0.7) + UP * (self.H - hb / 2))
        self.play(FadeIn(lab_a), FadeIn(lab_b), run_time=0.5)
        self.hold(0.6)
        self.wa, self.hb, self.lab_a = wa, hb, lab_a

    def highlight_product(self):
        inter = Rectangle(width=self.wa, height=self.hb, color=YELLOW, fill_opacity=0.75, stroke_width=1)
        inter.move_to(self.origin + RIGHT * (self.wa / 2) + UP * (self.H - self.hb / 2))
        self.play(FadeOut(self.lab_a), FadeIn(inter), run_time=0.7)
        cap = self.ja_text("長方形の面積＝積", font_size=26)
        cap.to_edge(RIGHT, buff=0.4).shift(UP * 1.75)
        self.play(FadeIn(cap), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"P(A\cap B)=P(A)\,P(B)").scale(1.05)
        formula.to_edge(DOWN, buff=0.38)
        note = self.ja_text("独立のとき", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(note), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
