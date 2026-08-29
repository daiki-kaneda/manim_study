from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GateauxDerivative(PacedScene):
    """#343 ゲートー微分：方向ごとの微分（約45秒）"""

    def construct(self):
        self.show_heading("ゲートー微分")
        self.draw_surface()
        self.directions()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_surface(self):
        self.O = LEFT * 0.5 + DOWN * 0.3
        # fake 2d contour
        ells = VGroup(*[
            Ellipse(width=w, height=h, color=BLUE, stroke_width=2).move_to(self.O)
            for w, h in [(4.2, 2.4), (3.0, 1.7), (1.8, 1.0)]
        ])
        self.play(LaggedStart(*[Create(e) for e in ells], lag_ratio=0.15), run_time=1.4)
        note = self.ja_text("等高線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def directions(self):
        arrows = VGroup(*[
            Arrow(self.O, self.O + d, buff=0, color=c, stroke_width=4)
            for d, c in [(RIGHT * 1.8 + UP * 0.4, ORANGE), (LEFT * 0.6 + UP * 1.5, TEAL), (RIGHT * 0.9 + DOWN * 1.2, YELLOW)]
        ])
        cap = self.ja_text("各方向へ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.12), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        cap2 = self.ja_text("方向微分", font_size=24).move_to(self.note)
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
        eq = MathTex(r"Df(x;v)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"Df(x;v)=\lim_{t\to 0}\frac{f(x+tv)-f(x)}{t}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"Df(x;v)=\lim_{t\to 0}\frac{f(x+tv)-f(x)}{t}").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
