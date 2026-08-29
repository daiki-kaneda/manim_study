from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EllipseReflection(PacedScene):
    """#624 楕円の反射：一方の焦点から他方へ（約45秒）"""

    def construct(self):
        self.show_heading("楕円の反射")
        self.draw_ellipse()
        self.rays()
        self.show_formula()
        self.read(1.4)

    def draw_ellipse(self):
        ell = Ellipse(width=5.0, height=3.0, color=BLUE, stroke_width=4).shift(UP * 0.15)
        f1 = Dot(ell.get_center() + LEFT * 1.5, color=YELLOW, radius=0.1)
        f2 = Dot(ell.get_center() + RIGHT * 1.5, color=YELLOW, radius=0.1)
        self.play(Create(ell), FadeIn(f1), FadeIn(f2),
                  FadeIn(MathTex(r"F_1", font_size=24).next_to(f1, DOWN, buff=0.12)),
                  FadeIn(MathTex(r"F_2", font_size=24).next_to(f2, DOWN, buff=0.12)),
                  run_time=1.4)
        note = self.ja_text("二焦点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.f1, self.f2, self.ell = f1, f2, ell

    def rays(self):
        # hit near top of ellipse
        hit = self.ell.point_at_angle(PI / 2.4)
        r1 = Arrow(self.f1.get_center(), hit, buff=0.05, color=ORANGE, stroke_width=3)
        r2 = Arrow(hit, self.f2.get_center(), buff=0.05, color=TEAL, stroke_width=3)
        hit2 = self.ell.point_at_angle(-PI / 2.6)
        r3 = Arrow(self.f1.get_center(), hit2, buff=0.05, color=ORANGE, stroke_width=3)
        r4 = Arrow(hit2, self.f2.get_center(), buff=0.05, color=TEAL, stroke_width=3)
        cap = self.ja_text("F1→境界→F2", font_size=24).move_to(self.note)
        self.play(GrowArrow(r1), GrowArrow(r2), GrowArrow(r3), GrowArrow(r4), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("接線が二等分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\angle i=\angle r\ \Rightarrow\ F_1\to F_2").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
