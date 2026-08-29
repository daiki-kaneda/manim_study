from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Hoeffding(PacedScene):
    """#291 ヘフディング：有界なら指数で集中（約45秒）"""

    def construct(self):
        self.show_heading("ヘフディングの不等式")
        self.draw_bound()
        self.tail()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_bound(self):
        self.axes = Axes(
            x_range=[-0.2, 5.2, 1],
            y_range=[0, 1.3, 1],
            x_length=7.2,
            y_length=2.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.45 + LEFT * 0.2)
        import math
        dens = self.axes.plot(lambda x: 0.95 * math.exp(-2.8 * (x - 2.5) ** 2), x_range=[0.3, 4.7], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(dens), run_time=1.4)
        note = self.ja_text("有界な和", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def tail(self):
        # shade right tail
        x0 = 3.6
        line = DashedLine(self.axes.c2p(x0, 0), self.axes.c2p(x0, 1.1), color=ORANGE, stroke_width=3)
        cap = self.ja_text("右の尾", font_size=24).move_to(self.note)
        self.play(Create(line), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        # exponential decay arrow
        arr = Arrow(self.axes.c2p(3.8, 0.55), self.axes.c2p(4.8, 0.15), buff=0.05, color=YELLOW, stroke_width=4)
        decay = MathTex(r"e^{-2nt^{2}}", color=YELLOW, font_size=34).next_to(arr, UP, buff=0.1)
        cap2 = self.ja_text("指数で減衰", font_size=24).move_to(self.note)
        self.play(GrowArrow(arr), FadeIn(decay), Transform(self.note, cap2), run_time=1.4)
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
        eq = MathTex(r"P(\bar X-\mu\ge t)\le e^{-2nt^{2}}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P(\bar X-\mu\ge t)\le e^{-2nt^{2}}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P(\bar X-\mu\ge t)\le e^{-2nt^{2}}").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
