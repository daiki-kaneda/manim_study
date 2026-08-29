from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DominatedConvergence(PacedScene):
    """#284 優収束：支配関数があれば極限と積分が交換（約45秒）"""

    def construct(self):
        self.show_heading("優収束定理")
        self.draw_dom()
        self.pass_limit()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_dom(self):
        self.axes = Axes(
            x_range=[0, 4.2, 1],
            y_range=[0, 2.6, 1],
            x_length=6.2,
            y_length=2.9,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 0.5 + UP * 0.2)
        import math
        g = self.axes.plot(lambda x: 2.1 * math.exp(-0.35 * x), x_range=[0.15, 4.0], color=GREY, stroke_width=4)
        f1 = self.axes.plot(lambda x: 1.5 * math.exp(-0.55 * x) * (1 + 0.2 * math.sin(6 * x)), x_range=[0.15, 4.0], color=BLUE, stroke_width=3)
        f2 = self.axes.plot(lambda x: 1.35 * math.exp(-0.5 * x) * (1 + 0.15 * math.sin(5 * x)), x_range=[0.15, 4.0], color=TEAL, stroke_width=3)
        self.play(Create(self.axes), Create(g), run_time=1.1)
        note = self.ja_text("支配する g", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.play(Create(f1), Create(f2), run_time=1.3)
        self.read(0.3)
        self.note = note

    def pass_limit(self):
        import math
        lim = self.axes.plot(lambda x: 1.25 * math.exp(-0.48 * x), x_range=[0.15, 4.0], color=ORANGE, stroke_width=5)
        cap = self.ja_text("極限へ", font_size=24).move_to(self.note)
        self.play(Create(lim), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("積分と交換", font_size=24).move_to(self.note)
        arrow = Arrow(UP * 0.2 + RIGHT * 2.5, DOWN * 1.5 + RIGHT * 2.5, buff=0.05, color=YELLOW)
        self.play(GrowArrow(arrow), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"\lim\int f_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\lim\int f_n=\int\lim f_n").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\lim\int f_n=\int\lim f_n").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
