from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SORMethod(PacedScene):
    """#285 SOR：緩和パラメータで加速（約45秒）"""

    def construct(self):
        self.show_heading("SOR 法")
        self.draw_iters()
        self.relax()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_iters(self):
        self.dots = VGroup()
        xs = [LEFT * 3.2, LEFT * 1.6, ORIGIN, RIGHT * 1.4]
        for i, p in enumerate(xs):
            d = Dot(p + UP * 0.4, color=BLUE, radius=0.12)
            lab = MathTex(rf"x^{{({i})}}", font_size=28).next_to(d, DOWN, buff=0.2)
            self.dots.add(VGroup(d, lab))
        arrows = VGroup(*[
            Arrow(self.dots[i][0].get_right(), self.dots[i + 1][0].get_left(), buff=0.1, color=GREY, stroke_width=3)
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in self.dots], lag_ratio=0.12), run_time=1.3)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), run_time=1.0)
        note = self.ja_text("反復", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def relax(self):
        omega = MathTex(r"\omega", color=ORANGE, font_size=48).shift(UP * 1.6 + LEFT * 0.3)
        cap = self.ja_text("緩和係数", font_size=24).move_to(self.note)
        self.play(FadeIn(omega, scale=0.6), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        # stretch last step
        big = Arrow(self.dots[2][0].get_center(), self.dots[3][0].get_center() + RIGHT * 0.8, buff=0.15, color=ORANGE, stroke_width=5)
        cap2 = self.ja_text("歩幅を調整", font_size=24).move_to(self.note)
        self.play(GrowArrow(big), Transform(self.note, cap2), run_time=1.3)
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
        eq = MathTex(r"x^{\mathrm{new}}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x^{\mathrm{new}}=(1-\omega)x+\omega\,\hat{x}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x^{\mathrm{new}}=(1-\omega)x+\omega\,\hat{x}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
