from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class SelfExciting(PacedScene):
    """#544 自己励起過程：発生が次の発生を呼ぶ（約45秒）"""

    def construct(self):
        self.show_heading("自己励起過程")
        self.draw_chain()
        self.feedback()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_chain(self):
        dots = VGroup(*[Dot(LEFT * 3 + RIGHT * i * 1.2 + UP * 0.4, color=BLUE, radius=0.12) for i in range(6)])
        arrows = VGroup(*[
            Arrow(dots[i].get_center(), dots[i + 1].get_center(), buff=0.15, color=ORANGE, stroke_width=3)
            for i in range(5)
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.08),
                  LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.08), run_time=1.5)
        note = self.ja_text("連鎖反応", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def feedback(self):
        cap = self.ja_text("正のフィードバック", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ホーケスの一般形", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\lambda(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\lambda(t)=\lambda_0+\int_0^{t-}g(t-s)\,dN(s)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\lambda(t)=\lambda_0+\int_0^{t-}g(t-s)\,dN(s)").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
