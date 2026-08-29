from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class HilleYosida(PacedScene):
    """#488 ヒレ・吉田：縮約半群の生成条件（約45秒）"""

    def construct(self):
        self.show_heading("ヒレ・吉田の定理")
        self.draw_semigroup()
        self.resolvent_bound()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_semigroup(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.3, height=0.9, corner_radius=0.08, color=BLUE, stroke_width=2)
            .shift(LEFT * 2.8 + RIGHT * i * 1.5 + UP * 0.5)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"T({t})", font_size=26).move_to(boxes[i]) for i, t in enumerate(["0", "t", "s", "t+s"])])
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("C0半群", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def resolvent_bound(self):
        formula_mini = MathTex(r"\|R(\lambda,A)\|\le\frac{1}{\lambda}", font_size=32).shift(DOWN * 0.6)
        cap = self.ja_text("リゾルベント評価", font_size=24).move_to(self.note)
        self.play(FadeIn(formula_mini), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("生成元を特徴づけ", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\|R(\lambda,A)^n\|\le\lambda^{-n}\ (\lambda>0)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|R(\lambda,A)^n\|\le\lambda^{-n}\ (\lambda>0)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|R(\lambda,A)^n\|\le\lambda^{-n}\ (\lambda>0)").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
