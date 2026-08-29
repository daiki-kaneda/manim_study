from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HilbertSpace(PacedScene):
    """#354 ヒルベルト空間：完備な内積空間（約45秒）"""

    def construct(self):
        self.show_heading("ヒルベルト空間")
        self.draw_angles()
        self.complete()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_angles(self):
        self.O = LEFT * 0.8 + DOWN * 0.2
        u = Arrow(self.O, self.O + RIGHT * 2.4, buff=0, color=BLUE, stroke_width=5)
        v = Arrow(self.O, self.O + RIGHT * 1.2 + UP * 1.8, buff=0, color=TEAL, stroke_width=5)
        ang = Angle(u, v, radius=0.55, color=ORANGE)
        self.play(GrowArrow(u), GrowArrow(v), run_time=1.3)
        self.play(Create(ang), run_time=0.8)
        note = self.ja_text("内積がある", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def complete(self):
        # Cauchy sequence converging
        pts = VGroup(*[
            Dot(self.O + RIGHT * (1.0 + 0.35 * i) + UP * (0.2 / (i + 1)), color=YELLOW, radius=0.08)
            for i in range(5)
        ])
        cap = self.ja_text("コーシー列", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("極限も中に", font_size=24).move_to(self.note)
        lim = Dot(self.O + RIGHT * 2.6 + UP * 0.05, color=RED, radius=0.11)
        self.play(FadeIn(lim, scale=0.5), Transform(self.note, cap2), run_time=1.1)
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
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("完備な内積空間", font_size=32)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
