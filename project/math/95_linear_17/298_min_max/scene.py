from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MinMaxTheorem(PacedScene):
    """#298 ミニマックス：固有値はレイリー商の極値（約45秒）"""

    def construct(self):
        self.show_heading("ミニマックス定理")
        self.draw_sphere()
        self.levels()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_sphere(self):
        self.circ = Circle(radius=2.0, color=GREY, stroke_width=3).shift(LEFT * 0.5 + DOWN * 0.1)
        self.play(Create(self.circ), run_time=1.1)
        note = self.ja_text("単位球面", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def levels(self):
        # nested ellipses as Rayleigh level sets projection
        e1 = Ellipse(width=3.2, height=1.6, color=BLUE, stroke_width=3).move_to(self.circ)
        e2 = Ellipse(width=2.2, height=2.8, color=TEAL, stroke_width=3).move_to(self.circ)
        dots = VGroup(
            Dot(self.circ.get_center() + RIGHT * 1.55, color=ORANGE, radius=0.1),
            Dot(self.circ.get_center() + UP * 1.55, color=YELLOW, radius=0.1),
        )
        cap = self.ja_text("レイリー商", font_size=24).move_to(self.note)
        self.play(Create(e1), Create(e2), Transform(self.note, cap), run_time=1.4)
        self.play(FadeIn(dots), run_time=0.8)
        self.read(0.25)
        cap2 = self.ja_text("最大・最小", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(dots[0]), Indicate(dots[1]), run_time=1.2)
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
        eq = MathTex(r"\lambda_{\max}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\lambda_{\max}=\max_{\|x\|=1}x^{*}Ax").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\lambda_{\max}=\max_{\|x\|=1}x^{*}Ax").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
