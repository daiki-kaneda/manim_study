from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class NormTopology(PacedScene):
    """#428 ノルム位相：作用素ノルムでの収束（約45秒）"""

    def construct(self):
        self.show_heading("ノルム位相")
        self.draw_ops()
        self.converge()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        ops = VGroup(*[
            Square(side_length=0.85, color=BLUE, stroke_width=2).shift(LEFT * 2.6 + RIGHT * i * 1.05 + UP * 0.5)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"T_{n}", font_size=26).move_to(ops[i]) for i, n in enumerate([1, 2, 3, "n"])])
        self.play(LaggedStart(*[FadeIn(o) for o in ops], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("作用素列", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def converge(self):
        axes = Axes(x_range=[0, 5, 1], y_range=[0, 1.2, 1], x_length=5.2, y_length=2.0,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(DOWN * 0.7 + RIGHT * 0.2)
        vals = [1.0, 0.55, 0.3, 0.15, 0.08]
        dots = VGroup(*[Dot(axes.c2p(i + 1, v), color=ORANGE, radius=0.08) for i, v in enumerate(vals)])
        path = VMobject(color=ORANGE, stroke_width=3)
        path.set_points_as_corners([d.get_center() for d in dots])
        cap = self.ja_text("ノルム差", font_size=24).move_to(self.note)
        self.play(Create(axes), Create(path), FadeIn(dots), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("0 へ収束", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\|T_n-T\|\to 0").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|T_n-T\|\to 0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|T_n-T\|\to 0").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
