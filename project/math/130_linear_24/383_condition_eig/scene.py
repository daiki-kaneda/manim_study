from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EigenCondition(PacedScene):
    """#383 固有値の条件数：摂動感度（約45秒）"""

    def construct(self):
        self.show_heading("固有値の条件数")
        self.draw_eigs()
        self.sensitivity()
        self.show_formula()
        self.read(1.4)

    def draw_eigs(self):
        self.O = LEFT * 0.4 + DOWN * 0.1
        ax = Line(self.O + LEFT * 2.8, self.O + RIGHT * 3.0, color=GREY, stroke_width=2)
        self.lam = Dot(self.O + RIGHT * 1.2, color=BLUE, radius=0.12)
        self.play(Create(ax), FadeIn(self.lam), run_time=1.2)
        note = self.ja_text("固有値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sensitivity(self):
        # perturbation spreads
        spread = VGroup(*[
            Dot(self.lam.get_center() + RIGHT * dx, color=ORANGE, radius=0.08)
            for dx in [-0.45, -0.2, 0.25, 0.5]
        ])
        brace = BraceBetweenPoints(spread[0].get_center(), spread[-1].get_center(), direction=UP, color=YELLOW)
        cap = self.ja_text("摂動で動く", font_size=24).move_to(self.note)
        self.play(FadeIn(spread), Transform(self.note, cap), run_time=1.3)
        self.play(FadeIn(brace), run_time=0.8)
        self.read(0.25)
        cap2 = self.ja_text("感度が大きい", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\kappa(\lambda)=\|y\|\|x\|/|y^{*}x|").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
