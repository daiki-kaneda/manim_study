from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TrustRegion(PacedScene):
    """#611 信頼領域法：モデルが信頼できる球内で最小化（約45秒）"""

    def construct(self):
        self.show_heading("信頼領域法")
        self.draw_ball()
        self.model()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ball(self):
        ball = Circle(radius=1.6, color=BLUE, stroke_width=3, fill_opacity=0.12).shift(LEFT * 0.4 + UP * 0.15)
        center = Dot(ball.get_center(), color=YELLOW)
        self.play(Create(ball), FadeIn(center),
                  FadeIn(MathTex(r"\Delta_k", font_size=28).next_to(ball, RIGHT, buff=0.15)),
                  run_time=1.3)
        note = self.ja_text("信頼半径", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.ball = ball

    def model(self):
        step = Arrow(self.ball.get_center(), self.ball.get_center() + UR * 0.9, buff=0.05, color=ORANGE, stroke_width=4)
        cap = self.ja_text("モデル最小化", font_size=24).move_to(self.note)
        self.play(GrowArrow(step), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("比で半径更新", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\min_{\|s\|\le\Delta} m_k(s)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\min_{\|s\|\le\Delta} m_k(s)=f+g^{\top}s+\tfrac12 s^{\top}Bs").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\min_{\|s\|\le\Delta} m_k(s)=f+g^{\top}s+\tfrac12 s^{\top}Bs").scale(0.62)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
