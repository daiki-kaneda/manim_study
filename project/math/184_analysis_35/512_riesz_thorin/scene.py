from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class RieszThorin(PacedScene):
    """#512 リース・ソーリン：補間でノルムを挟む（約45秒）"""

    def construct(self):
        self.show_heading("リース・ソーリン")
        self.draw_endpoints()
        self.interpolate()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_endpoints(self):
        a = Dot(LEFT * 3 + DOWN * 0.5, color=BLUE, radius=0.12)
        b = Dot(RIGHT * 3 + UP * 1.0, color=TEAL, radius=0.12)
        la = MathTex(r"L^{p_0}", font_size=30).next_to(a, DOWN)
        lb = MathTex(r"L^{p_1}", font_size=30).next_to(b, UP)
        self.play(FadeIn(a), FadeIn(b), FadeIn(la), FadeIn(lb), run_time=1.2)
        note = self.ja_text("端点評価", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.a, self.b = a, b

    def interpolate(self):
        line = Line(self.a.get_center(), self.b.get_center(), color=ORANGE, stroke_width=4)
        mid = Dot(line.point_from_proportion(0.45), color=YELLOW, radius=0.1)
        cap = self.ja_text("複素補間", font_size=24).move_to(self.note)
        self.play(Create(line), FadeIn(mid), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("中間の p も有界", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\|T\|_{p_\theta\to q_\theta}\le\|T\|_{p_0\to q_0}^{1-\theta}\|T\|_{p_1\to q_1}^{\theta}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|T\|_{p_\theta\to q_\theta}\le\|T\|_{p_0\to q_0}^{1-\theta}\|T\|_{p_1\to q_1}^{\theta}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|T\|_{p_\theta\to q_\theta}\le\|T\|_{p_0\to q_0}^{1-\theta}\|T\|_{p_1\to q_1}^{\theta}").scale(0.62)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
