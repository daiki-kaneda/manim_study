from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class II1Factor(PacedScene):
    """#522 II1因子：有限で連続次元の因子（約45秒）"""

    def construct(self):
        self.show_heading("II1因子")
        self.draw_trace()
        self.types()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_trace(self):
        box = RoundedRectangle(width=3.0, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.0 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"\tau", font_size=40).move_to(box)), run_time=1.2)
        note = self.ja_text("有限トレース", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def types(self):
        caps = VGroup(*[
            RoundedRectangle(width=1.5, height=0.9, corner_radius=0.08, color=c, stroke_width=2)
            .shift(RIGHT * 2.2 + UP * (1.0 - i * 1.0))
            for i, c in enumerate([GREY, ORANGE, TEAL])
        ])
        labs = VGroup(*[MathTex(s, font_size=26).move_to(caps[i]) for i, s in enumerate([r"I_n", r"II_1", r"III"])])
        cap = self.ja_text("型分類の中心", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(c) for c in caps], lag_ratio=0.1), FadeIn(labs), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("連続次元", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\tau(1)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\tau(1)=1,\ \tau(x^*x)=0\Rightarrow x=0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\tau(1)=1,\ \tau(x^*x)=0\Rightarrow x=0").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
