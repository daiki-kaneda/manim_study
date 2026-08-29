from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HarmonicConjugate(PacedScene):
    """#385 調和共役：(A,B;C,D)=-1（約45秒）"""

    def construct(self):
        self.show_heading("調和共役")
        self.draw_line()
        self.mark_points()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_line(self):
        self.base = Line(LEFT * 3.4, RIGHT * 3.4, color=GREY, stroke_width=3).shift(UP * 0.35)
        self.play(Create(self.base), run_time=1.0)
        note = self.ja_text("直線上の 4 点", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mark_points(self):
        # A=-2.4, C=-0.8, B=1.2, D=2.4  (rough harmonic feel)
        coords = {"A": -2.4, "C": -0.8, "B": 1.2, "D": 2.4}
        colors = {"A": BLUE, "B": BLUE, "C": ORANGE, "D": TEAL}
        self.dots = {}
        labels = VGroup()
        for name, x in coords.items():
            p = self.base.point_from_proportion((x + 3.4) / 6.8)
            d = Dot(p, color=colors[name], radius=0.11)
            lab = MathTex(name, font_size=30).next_to(d, DOWN, buff=0.18)
            self.dots[name] = d
            labels.add(lab)
        self.play(
            LaggedStart(*[FadeIn(self.dots[n], scale=0.5) for n in "ACBD"], lag_ratio=0.12),
            FadeIn(labels),
            run_time=1.5,
        )
        # cross-ratio braces
        brace_ab = BraceBetweenPoints(
            self.dots["A"].get_center(), self.dots["B"].get_center(), direction=UP, color=YELLOW
        )
        cap = self.ja_text("比の比", font_size=24).move_to(self.note)
        self.play(FadeIn(brace_ab), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        # highlight D as conjugate of C
        ring = Circle(radius=0.28, color=TEAL, stroke_width=3).move_to(self.dots["D"])
        cap2 = self.ja_text("D が共役", font_size=24).move_to(self.note)
        self.play(Create(ring), Indicate(self.dots["C"], color=ORANGE), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"(A,B;C,D)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"(A,B;C,D)=-1").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"(A,B;C,D)=-1").scale(1.05)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
