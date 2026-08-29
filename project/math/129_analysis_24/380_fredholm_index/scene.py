from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FredholmIndex(PacedScene):
    """#380 フレドホルム指数：dim ker − dim coker（約45秒）"""

    def construct(self):
        self.show_heading("フレドホルム指数")
        self.draw_dims()
        self.subtract()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_dims(self):
        ker = RoundedRectangle(width=2.6, height=1.4, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.5 + UP * 0.4)
        coker = RoundedRectangle(width=2.6, height=1.4, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.5 + UP * 0.4)
        k = MathTex(r"\dim\ker T", font_size=34).move_to(ker)
        c = MathTex(r"\dim\mathrm{coker}\,T", font_size=30).move_to(coker)
        self.play(FadeIn(ker), FadeIn(k), FadeIn(coker), FadeIn(c), run_time=1.5)
        note = self.ja_text("二つの次元", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def subtract(self):
        minus = MathTex(r"-", font_size=56).move_to(UP * 0.4)
        idx = MathTex(r"\mathrm{index}\,T", color=ORANGE, font_size=40).shift(DOWN * 0.8)
        cap = self.ja_text("引く", font_size=24).move_to(self.note)
        self.play(FadeIn(minus), Transform(self.note, cap), run_time=1.0)
        self.play(Write(idx), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("指数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(idx, color=YELLOW), run_time=1.1)
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
        eq = MathTex(r"\mathrm{index}\,T").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{index}\,T=\dim\ker T-\dim\mathrm{coker}\,T").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{index}\,T=\dim\ker T-\dim\mathrm{coker}\,T").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
