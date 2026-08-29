from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SanovTheorem(PacedScene):
    """#364 サノフ：経験分布の大偏差は KL（約45秒）"""

    def construct(self):
        self.show_heading("サノフの定理")
        self.draw_emp()
        self.kl_rate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_emp(self):
        self.axes = Axes(x_range=[-0.2, 4.2, 1], y_range=[0, 1.2, 1], x_length=6.5, y_length=2.5,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.4 + UP * 0.35)
        import math
        p = self.axes.plot(lambda x: 0.9 * math.exp(-2.8 * (x - 1.6) ** 2), x_range=[0.3, 3.5], color=BLUE, stroke_width=4)
        emp = self.axes.plot(lambda x: 0.75 * math.exp(-2.2 * (x - 2.5) ** 2), x_range=[0.8, 4.0], color=ORANGE, stroke_width=4)
        self.play(Create(self.axes), Create(p), run_time=1.1)
        self.play(Create(emp), run_time=1.0)
        note = self.ja_text("経験分布", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def kl_rate(self):
        gap = DoubleArrow(self.axes.c2p(1.6, 1.05), self.axes.c2p(2.5, 1.05), buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("ずれの速さ", font_size=24).move_to(self.note)
        self.play(Create(gap), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("KL がレート", font_size=24).move_to(self.note)
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
        eq = MathTex(r"I(\mu)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"I(\mu)=D_{\mathrm{KL}}(\mu\|P)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"I(\mu)=D_{\mathrm{KL}}(\mu\|P)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
