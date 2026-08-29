from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class VarianceAdditivity(PacedScene):
    """#267 独立なら分散は足せる（約45秒）"""

    def construct(self):
        self.show_heading("分散の加法性")
        self.draw_spreads()
        self.add_them()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_spreads(self):
        self.axes = Axes(
            x_range=[-0.2, 5.2, 1],
            y_range=[0, 1.2, 1],
            x_length=8.0,
            y_length=2.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.5 + LEFT * 0.15)
        # two narrow bumps
        import math
        x1 = self.axes.plot(lambda x: 0.9 * math.exp(-8 * (x - 1.3) ** 2), x_range=[0.2, 2.5], color=BLUE, stroke_width=4)
        x2 = self.axes.plot(lambda x: 0.9 * math.exp(-5 * (x - 3.5) ** 2), x_range=[2.2, 4.8], color=TEAL, stroke_width=4)
        self.play(Create(self.axes), run_time=0.75)
        self.play(Create(x1), Create(x2), run_time=1.5)
        note = self.ja_text("独立", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def add_them(self):
        import math
        # wider sum bump
        s = self.axes.plot(
            lambda x: 0.75 * math.exp(-2.2 * (x - 2.5) ** 2),
            x_range=[0.3, 4.8],
            color=ORANGE,
            stroke_width=5,
        )
        # braces for widths
        w1 = Line(self.axes.c2p(0.9, 0.15), self.axes.c2p(1.7, 0.15), color=BLUE, stroke_width=6)
        w2 = Line(self.axes.c2p(3.0, 0.15), self.axes.c2p(4.0, 0.15), color=TEAL, stroke_width=6)
        ws = Line(self.axes.c2p(1.4, -0.05), self.axes.c2p(3.6, -0.05), color=ORANGE, stroke_width=6)
        cap = self.ja_text("和は広がる", font_size=24).move_to(self.note)
        self.play(Create(s), Create(w1), Create(w2), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("分散を足す", font_size=24).move_to(self.note)
        self.play(Create(ws), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"\mathrm{Var}(X+Y)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
