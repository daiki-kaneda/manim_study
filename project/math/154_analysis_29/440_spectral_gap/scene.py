from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class SpectralGap(PacedScene):
    """#440 スペクトルギャップ：0 の次との間隙（約45秒）"""

    def construct(self):
        self.show_heading("スペクトルギャップ")
        self.draw_spec()
        self.gap()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_spec(self):
        self.O = ORIGIN + DOWN * 0.1
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        zero = Dot(self.O, color=RED, radius=0.12)
        rest = Line(self.O + RIGHT * 1.2, self.O + RIGHT * 2.8, color=BLUE, stroke_width=10)
        self.play(Create(ax), FadeIn(zero), Create(rest), run_time=1.4)
        note = self.ja_text("0 と残り", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.zero = zero
        self.rest = rest

    def gap(self):
        brace = BraceBetweenPoints(self.zero.get_center(), self.rest.get_left(), direction=UP, color=YELLOW)
        cap = self.ja_text("隙間", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("混合が速い", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\mathrm{gap}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{gap}=\inf(\sigma(A)\setminus\{0\})").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{gap}=\inf(\sigma(A)\setminus\{0\})").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
