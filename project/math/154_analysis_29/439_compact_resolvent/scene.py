from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class CompactResolvent(PacedScene):
    """#439 コンパクトレゾルベント：離散スペクトル（約45秒）"""

    def construct(self):
        self.show_heading("コンパクトレゾルベント")
        self.draw_spec()
        self.discrete()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_spec(self):
        self.O = LEFT * 0.2
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        pts = VGroup(*[Dot(self.O + RIGHT * x, color=ORANGE, radius=0.09) for x in [-2.2, -1.0, 0.3, 1.4, 2.4]])
        self.play(Create(ax), FadeIn(pts), run_time=1.3)
        note = self.ja_text("固有値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.pts = pts

    def discrete(self):
        rings = VGroup(*[Circle(radius=0.22, color=YELLOW, stroke_width=2).move_to(p.get_center()) for p in self.pts])
        cap = self.ja_text("孤立している", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.08), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("離散スペクトル", font_size=24).move_to(self.note)
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
        eq = MathTex(r"(z-A)^{-1}\ \mathrm{compact}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"(z-A)^{-1}\ \mathrm{compact}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"(z-A)^{-1}\ \mathrm{compact}").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
