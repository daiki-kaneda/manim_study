from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BallotTheorem(PacedScene):
    """#329 バロット定理：終始リードする道の割合（約45秒）"""

    def construct(self):
        self.show_heading("バロット定理")
        self.draw_paths()
        self.ratio()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_paths(self):
        self.axes = Axes(x_range=[0, 6.2, 1], y_range=[-0.5, 4.2, 1], x_length=7.2, y_length=3.2,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.2 + LEFT * 0.15)
        # winning path always above 0
        win = [0, 1, 2, 1, 2, 3, 4]
        lose = [0, 1, -1, 0, 1, 2, 3]
        wpath = VMobject(color=BLUE, stroke_width=4)
        wpath.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(win)])
        lpath = VMobject(color=GREY, stroke_width=3)
        lpath.set_points_as_corners([self.axes.c2p(i, y) for i, y in enumerate(lose)])
        zero = DashedLine(self.axes.c2p(0, 0), self.axes.c2p(6, 0), color=GREY, stroke_width=2)
        self.play(Create(self.axes), Create(zero), run_time=0.9)
        self.play(Create(lpath), Create(wpath), run_time=1.4)
        note = self.ja_text("常にリード", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ratio(self):
        frac = MathTex(r"\frac{a-b}{a+b}", color=ORANGE, font_size=42).shift(RIGHT * 2.6 + DOWN * 0.3)
        cap = self.ja_text("割合は", font_size=24).move_to(self.note)
        self.play(Write(frac), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("差÷合計", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"P(\text{always lead})").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"P(\text{always lead})=\frac{a-b}{a+b}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"P(\text{always lead})=\frac{a-b}{a+b}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
