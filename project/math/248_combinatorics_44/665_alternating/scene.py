from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AlternatingPermutations(PacedScene):
    """#665 交替順列：上下が交互に入れ替わる順列（約45秒）"""

    def construct(self):
        self.show_heading("交替順列")
        self.draw()
        self.zigzag()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        vals = [1, 3, 2, 5, 4]
        xs = [LEFT * 2.4 + RIGHT * i * 1.2 for i in range(5)]
        dots = VGroup(*[Dot(xs[i] + UP * (vals[i] * 0.35 - 0.5), color=YELLOW, radius=0.1) for i in range(5)])
        path = VMobject(color=BLUE, stroke_width=3).set_points_as_corners([d.get_center() for d in dots])
        labs = VGroup(*[MathTex(str(v), font_size=24).next_to(d, UP, buff=0.12) for v, d in zip(vals, dots)])
        self.play(Create(path), FadeIn(dots), FadeIn(labs), run_time=1.4)
        note = self.ja_text("上下交互", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def zigzag(self):
        cap = self.ja_text("ジグザグ順列", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("セカント・タンジェント", font_size=20).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.75)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\sec x+\tan x").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sec x+\tan x=\sum E_n\frac{x^n}{n!}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sec x+\tan x=\sum E_n\frac{x^n}{n!}").scale(0.7)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
