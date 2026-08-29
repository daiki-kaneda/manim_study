from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PowerMethod(PacedScene):
    """#491 パワー法：反復で主成分を取り出す（約45秒）"""

    def construct(self):
        self.show_heading("パワー法")
        self.draw_iterate()
        self.converge()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_iterate(self):
        axes = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-1.6, 1.6, 1],
            x_length=5.5, y_length=3.2, tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(LEFT * 0.4 + UP * 0.15)
        v0 = Arrow(axes.c2p(0, 0), axes.c2p(0.6, 0.9), buff=0, color=GREY, stroke_width=4)
        v1 = Arrow(axes.c2p(0, 0), axes.c2p(1.2, 0.7), buff=0, color=BLUE, stroke_width=4)
        v2 = Arrow(axes.c2p(0, 0), axes.c2p(1.6, 0.35), buff=0, color=ORANGE, stroke_width=4)
        self.play(Create(axes), GrowArrow(v0), run_time=1.1)
        self.play(GrowArrow(v1), run_time=0.7)
        self.play(GrowArrow(v2), run_time=0.7)
        note = self.ja_text("反復で伸びる", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def converge(self):
        cap = self.ja_text("最大固有方向", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("正規化を忘れず", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"v_{k+1}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"v_{k+1}=\frac{Av_k}{\|Av_k\|}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"v_{k+1}=\frac{Av_k}{\|Av_k\|}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
