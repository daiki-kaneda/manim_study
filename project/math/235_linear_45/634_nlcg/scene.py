from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class NonlinearCG(PacedScene):
    """#634 非線形CG：勾配共役方向を更新（約45秒）"""

    def construct(self):
        self.show_heading("非線形CG")
        self.draw_dirs()
        self.beta()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_dirs(self):
        o = Dot(ORIGIN + DOWN * 0.2, color=YELLOW)
        g = Arrow(o.get_center(), o.get_center() + LEFT * 1.8 + DOWN * 0.4, buff=0.05, color=RED, stroke_width=4)
        d = Arrow(o.get_center(), o.get_center() + LEFT * 0.6 + UP * 1.6, buff=0.05, color=BLUE, stroke_width=4)
        self.play(FadeIn(o), GrowArrow(g), GrowArrow(d),
                  FadeIn(MathTex(r"-\nabla f", font_size=26).next_to(g, DOWN, buff=0.08)),
                  FadeIn(MathTex(r"d_k", font_size=26).next_to(d, RIGHT, buff=0.08)),
                  run_time=1.4)
        note = self.ja_text("探索方向", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def beta(self):
        cap = self.ja_text("β で混ぜる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("FR・PR・HS", font_size=24).move_to(self.note)
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
        eq = MathTex(r"d_{k+1}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"d_{k+1}=-\nabla f_{k+1}+\beta_k d_k").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"d_{k+1}=-\nabla f_{k+1}+\beta_k d_k").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
