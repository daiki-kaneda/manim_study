from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DKWInequality(PacedScene):
    """#328 DKW：経験分布の一様偏差の指数界（約45秒）"""

    def construct(self):
        self.show_heading("DKW 不等式")
        self.draw_band()
        self.bound()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_band(self):
        self.axes = Axes(x_range=[-0.2, 4.2, 1], y_range=[0, 1.15, 1], x_length=6.8, y_length=2.8,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.35 + LEFT * 0.2)
        import math
        F = self.axes.plot(lambda x: 1 / (1 + math.exp(-1.5 * (x - 2))), x_range=[0.2, 4.0], color=BLUE, stroke_width=4)
        up = self.axes.plot(lambda x: min(1.0, 1 / (1 + math.exp(-1.5 * (x - 2))) + 0.12), x_range=[0.2, 4.0], color=GREY, stroke_width=2)
        lo = self.axes.plot(lambda x: max(0.0, 1 / (1 + math.exp(-1.5 * (x - 2))) - 0.12), x_range=[0.2, 4.0], color=GREY, stroke_width=2)
        self.play(Create(self.axes), Create(F), run_time=1.2)
        self.play(Create(up), Create(lo), run_time=1.1)
        note = self.ja_text("一様バンド", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bound(self):
        cap = self.ja_text("ずれの最大", font_size=24).move_to(self.note)
        brace = MathTex(r"\|F_n-F\|_{\infty}", color=ORANGE, font_size=34).shift(RIGHT * 2.5 + DOWN * 0.2)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("指数で押さえる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"P(\|F_n-F\|_{\infty}>\varepsilon)\le 2e^{-2n\varepsilon^{2}}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P(\|F_n-F\|_{\infty}>\varepsilon)\le 2e^{-2n\varepsilon^{2}}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P(\|F_n-F\|_{\infty}>\varepsilon)\le 2e^{-2n\varepsilon^{2}}").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
