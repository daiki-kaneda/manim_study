from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TaylorRemainder(PacedScene):
    """#174 テイラーの余りは次の項の大きさ（約45秒）"""

    def construct(self):
        self.show_heading("テイラー余り")
        self.draw_curve()
        self.build_approx()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_curve(self):
        self.axes = Axes(
            x_range=[-0.4, 3.4, 1],
            y_range=[-0.4, 2.6, 1],
            x_length=7.6,
            y_length=3.4,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.35)
        self.curve = self.axes.plot(lambda x: 0.18 * x * x + 0.35, x_range=[0.05, 3.1], color=BLUE, stroke_width=5)
        self.play(Create(self.axes), run_time=0.85)
        self.play(Create(self.curve), run_time=1.7)
        self.read(0.3)

    def build_approx(self):
        a = 1.1
        note = self.ja_text("1 次", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        t1 = self.axes.plot(lambda x: 0.18 * a * a + 0.35 + 0.36 * a * (x - a), x_range=[0.2, 2.6], color=YELLOW, stroke_width=4)
        self.play(Create(t1), FadeIn(note), run_time=1.4)
        self.read(0.35)
        t2 = self.axes.plot(lambda x: 0.18 * x * x + 0.35, x_range=[0.2, 2.9], color=ORANGE, stroke_width=4)
        cap = self.ja_text("2 次で一致", font_size=24).move_to(note)
        self.play(Transform(t1, t2), Transform(note, cap), run_time=1.5)
        self.read(0.35)
        # remainder gap marker at x=2.5 vs linear would differ - show brace at a point
        p = self.axes.c2p(2.4, 0.18 * 2.4 * 2.4 + 0.35)
        lin_y = 0.18 * a * a + 0.35 + 0.36 * a * (2.4 - a)
        q = self.axes.c2p(2.4, lin_y)
        gap = DashedLine(p, q, color=TEAL, stroke_width=3)
        cap2 = self.ja_text("余り", font_size=24).move_to(note)
        self.play(Create(gap), Transform(note, cap2), run_time=1.1)
        self.read(0.4)
        self.note = note

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"R_n(x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"R_n(x)=\frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
