from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class SingularIntegral(PacedScene):
    """#536 特異積分：主値で定義する積分作用素（約45秒）"""

    def construct(self):
        self.show_heading("特異積分")
        self.draw_pv()
        self.cancel()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_pv(self):
        line = NumberLine(x_range=[-3, 3, 1], length=7, include_numbers=False).shift(UP * 0.4)
        gap = Line(ORIGIN + LEFT * 0.35, ORIGIN + RIGHT * 0.35, color=BLACK, stroke_width=8).shift(UP * 0.4)
        self.play(Create(line), run_time=1.0)
        hole = Circle(radius=0.35, color=ORANGE, stroke_width=3).shift(UP * 0.4)
        self.play(Create(hole), run_time=0.8)
        note = self.ja_text("原点をくり抜く", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def cancel(self):
        cap = self.ja_text("正負が打ち消し", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("主値極限", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\mathrm{p.v.}\int_{-1}^{1}\frac{f(x)}{x}\,dx").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathrm{p.v.}\int_{-1}^{1}\frac{f(x)}{x}\,dx=\lim_{\varepsilon\to0}\int_{|x|>\varepsilon}\frac{f(x)}{x}\,dx").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathrm{p.v.}\int_{-1}^{1}\frac{f(x)}{x}\,dx=\lim_{\varepsilon\to0}\int_{|x|>\varepsilon}\frac{f(x)}{x}\,dx").scale(0.58)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
