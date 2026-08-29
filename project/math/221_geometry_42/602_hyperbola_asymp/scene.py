from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class HyperbolaAsymptotes(PacedScene):
    """#602 双曲線の漸近線：無限遠で近づく直線（約45秒）"""

    def construct(self):
        self.show_heading("双曲線の漸近線")
        self.draw_hyp()
        self.asymp()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_hyp(self):
        axes = Axes(x_range=[-3.2, 3.2, 1], y_range=[-2.2, 2.2, 1], x_length=6.8, y_length=3.2, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(UP * 0.1)
        def branch(sign_x, sign_y):
            return axes.plot(
                lambda x: sign_y * 0.7 * ((x / 1.1) ** 2 - 1) ** 0.5 if abs(x) >= 1.1 else 0,
                x_range=[sign_x * 1.1, sign_x * 3.0] if sign_x > 0 else [sign_x * 3.0, sign_x * 1.1],
                color=BLUE, stroke_width=4,
            )
        curves = VGroup(branch(1, 1), branch(1, -1), branch(-1, 1), branch(-1, -1))
        self.play(Create(axes), * [Create(c) for c in curves], run_time=1.5)
        note = self.ja_text("双曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def asymp(self):
        a1 = DashedLine(LEFT * 3 + DOWN * 1.9, RIGHT * 3 + UP * 1.9, color=ORANGE, stroke_width=3)
        a2 = DashedLine(LEFT * 3 + UP * 1.9, RIGHT * 3 + DOWN * 1.9, color=ORANGE, stroke_width=3)
        cap = self.ja_text("漸近線", font_size=24).move_to(self.note)
        self.play(Create(a1), Create(a2), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("無限で近づく", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\frac{x^2}{a^2}-\frac{y^2}{b^2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\ \to\ y=\pm\frac{b}{a}x").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{x^2}{a^2}-\frac{y^2}{b^2}=1\ \to\ y=\pm\frac{b}{a}x").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
