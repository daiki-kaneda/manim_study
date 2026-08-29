from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SAM(PacedScene):
    """#659 SAM：損失の平坦な最小を探す摂動（約45秒）"""

    def construct(self):
        self.show_heading("SAM")
        self.draw_loss()
        self.perturb()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_loss(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        sharp = axes.plot(lambda x: 0.3 + 1.4 * (x ** 2), x_range=[-1.2, 1.2], color=RED, stroke_width=2)
        flat = axes.plot(lambda x: 0.5 + 0.25 * (x ** 2), x_range=[-1.8, 1.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(sharp), Create(flat), run_time=1.4)
        note = self.ja_text("平坦な谷", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def perturb(self):
        cap = self.ja_text("最悪方向へ摂動", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("シャープネス意識", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\min_\theta\max_{\|\varepsilon\|\le\rho} L(\theta+\varepsilon)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\min_\theta\max_{\|\varepsilon\|\le\rho} L(\theta+\varepsilon)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\min_\theta\max_{\|\varepsilon\|\le\rho} L(\theta+\varepsilon)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
