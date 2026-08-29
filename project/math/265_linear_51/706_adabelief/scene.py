from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AdaBelief(PacedScene):
    """#706 AdaBelief：勾配と予測の差で適応（約45秒）"""

    def construct(self):
        self.show_heading("AdaBelief")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        o = Dot(LEFT * 1.5, color=YELLOW)
        pred = Arrow(o.get_center(), o.get_center() + RIGHT * 2.2 + UP * 0.6, buff=0.05, color=BLUE, stroke_width=4)
        grad = Arrow(o.get_center(), o.get_center() + RIGHT * 1.6 + DOWN * 0.5, buff=0.05, color=RED, stroke_width=4)
        self.play(FadeIn(o), GrowArrow(pred), GrowArrow(grad), run_time=1.4)

        note = self.ja_text("信念の誤差", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("s_t で適応", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("汎化が良い", font_size=24).move_to(self.note)
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
        eq = MathTex(r"s_t").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"s_t=\beta_2 s_{t-1}+(1-\beta_2)(g_t-m_t)^2").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"s_t=\beta_2 s_{t-1}+(1-\beta_2)(g_t-m_t)^2").scale(0.58)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
