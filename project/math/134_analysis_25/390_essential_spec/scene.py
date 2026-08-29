from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EssentialSpectrum(PacedScene):
    """#390 本質スペクトル：コンパクト摂動で不変（約45秒）"""

    def construct(self):
        self.show_heading("本質スペクトル")
        self.draw_spec()
        self.perturb()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_spec(self):
        self.O = LEFT * 0.3 + DOWN * 0.1
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        # discrete eigenvalues + continuum blob
        eigs = VGroup(*[Dot(self.O + RIGHT * x, color=BLUE, radius=0.09) for x in [-2.2, -1.4, 0.2]])
        band = Line(self.O + RIGHT * 1.0, self.O + RIGHT * 2.8, color=ORANGE, stroke_width=8)
        self.play(Create(ax), FadeIn(eigs), Create(band), run_time=1.4)
        note = self.ja_text("スペクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.band = band
        self.eigs = eigs

    def perturb(self):
        # compact perturbation moves isolated points, band stays
        shifts = [0.25, -0.2, 0.15]
        anims = [
            self.eigs[i].animate.shift(RIGHT * shifts[i] + UP * 0.35)
            for i in range(3)
        ]
        cap = self.ja_text("コンパクト摂動", font_size=24).move_to(self.note)
        self.play(*anims, Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        ring = SurroundingRectangle(self.band, color=YELLOW, buff=0.15)
        cap2 = self.ja_text("本質は不変", font_size=24).move_to(self.note)
        self.play(Create(ring), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"\sigma_{\mathrm{ess}}(T+K)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sigma_{\mathrm{ess}}(T+K)=\sigma_{\mathrm{ess}}(T)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sigma_{\mathrm{ess}}(T+K)=\sigma_{\mathrm{ess}}(T)").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
