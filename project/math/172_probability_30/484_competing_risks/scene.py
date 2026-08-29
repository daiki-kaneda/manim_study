from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CompetingRisks(PacedScene):
    """#484 競合リスク：複数原因が終了を争う（約45秒）"""

    def construct(self):
        self.show_heading("競合リスク")
        self.draw_causes()
        self.cif()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_causes(self):
        start = Dot(LEFT * 3.0 + UP * 0.3, color=BLUE, radius=0.12)
        causes = VGroup(*[
            RoundedRectangle(width=1.8, height=0.9, corner_radius=0.1, color=c, stroke_width=3)
            .shift(RIGHT * 2.2 + UP * (1.2 - i * 1.15))
            for i, c in enumerate([ORANGE, TEAL, PURPLE])
        ])
        labs = VGroup(*[
            MathTex(rf"j={i+1}", font_size=28).move_to(causes[i]) for i in range(3)
        ])
        arrows = VGroup(*[
            Arrow(start.get_center(), causes[i].get_left(), buff=0.12, color=GREY, stroke_width=3)
            for i in range(3)
        ])
        self.play(FadeIn(start), run_time=0.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
                  LaggedStart(*[Create(b) for b in causes], lag_ratio=0.15),
                  FadeIn(labs), run_time=1.5)
        note = self.ja_text("複数の原因", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cif(self):
        cap = self.ja_text("累積発生関数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("打ち切りと区別", font_size=24).move_to(self.note)
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
        eq = MathTex(r"F_j(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"F_j(t)=P(T\le t,\ J=j)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"F_j(t)=P(T\le t,\ J=j)").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
