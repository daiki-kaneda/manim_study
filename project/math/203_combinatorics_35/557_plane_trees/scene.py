from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PlaneTrees(PacedScene):
    """#557 平面木：埋め込みを区別する木（約45秒）"""

    def construct(self):
        self.show_heading("平面木")
        self.draw_trees()
        self.count()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_trees(self):
        t1 = VGroup(
            Dot(LEFT * 2.5 + UP * 1.0, color=BLUE),
            Dot(LEFT * 3.2 + DOWN * 0.3, color=BLUE),
            Dot(LEFT * 1.8 + DOWN * 0.3, color=BLUE),
            Line(LEFT * 2.5 + UP * 1.0, LEFT * 3.2 + DOWN * 0.3, color=GREY),
            Line(LEFT * 2.5 + UP * 1.0, LEFT * 1.8 + DOWN * 0.3, color=GREY),
        )
        t2 = VGroup(
            Dot(RIGHT * 1.5 + UP * 1.0, color=ORANGE),
            Dot(RIGHT * 0.5 + DOWN * 0.1, color=ORANGE),
            Dot(RIGHT * 1.5 + DOWN * 0.5, color=ORANGE),
            Dot(RIGHT * 2.5 + DOWN * 0.1, color=ORANGE),
            Line(RIGHT * 1.5 + UP * 1.0, RIGHT * 0.5 + DOWN * 0.1, color=GREY),
            Line(RIGHT * 1.5 + UP * 1.0, RIGHT * 1.5 + DOWN * 0.5, color=GREY),
            Line(RIGHT * 1.5 + UP * 1.0, RIGHT * 2.5 + DOWN * 0.1, color=GREY),
        )
        self.play(FadeIn(t1), FadeIn(t2), run_time=1.4)
        note = self.ja_text("埋め込みが違う", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def count(self):
        cap = self.ja_text("カタランと関係", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("根付きを数える", font_size=24).move_to(self.note)
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
        eq = MathTex(r"T_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"T_n=C_{n-1}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"T_n=C_{n-1}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
