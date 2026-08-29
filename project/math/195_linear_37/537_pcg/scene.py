from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PreconditionedCG(PacedScene):
    """#537 前処理付きCG：条件数を下げて加速（約45秒）"""

    def construct(self):
        self.show_heading("前処理付きCG")
        self.draw_M()
        self.effect()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_M(self):
        a = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.2)
        m = RoundedRectangle(width=2.2, height=1.4, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.2)
        self.play(Create(a), FadeIn(MathTex("A", font_size=36).move_to(a)), Create(m), FadeIn(MathTex("M", font_size=36).move_to(m)), run_time=1.3)
        note = self.ja_text("前処理行列", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def effect(self):
        arrow = Arrow(LEFT * 1.1, RIGHT * 1.1, buff=0.1, color=YELLOW, stroke_width=4)
        cap = self.ja_text("条件数を改善", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("収束が速くなる", font_size=24).move_to(self.note)
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
        eq = MathTex(r"M^{-1}Ax").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"M^{-1}Ax=M^{-1}b\quad(M\approx A)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"M^{-1}Ax=M^{-1}b\quad(M\approx A)").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
