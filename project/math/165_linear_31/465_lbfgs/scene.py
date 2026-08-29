from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LBFGS(PacedScene):
    """#465 L-BFGS：限られた履歴でヘッセを近似（約45秒）"""

    def construct(self):
        self.show_heading("L-BFGS")
        self.draw_history()
        self.two_loop()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_history(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.1, height=0.7, corner_radius=0.08, color=BLUE, stroke_width=2)
            .shift(LEFT * 2.6 + RIGHT * i * 1.25 + UP * 0.7)
            for i in range(4)
        ])
        labs = VGroup(*[MathTex(rf"s_{{{k}}}", font_size=26).move_to(boxes[i]) for i, k in enumerate(["n-3", "n-2", "n-1", "n"])])
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("短い履歴", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def two_loop(self):
        arrows = VGroup(
            Arrow(LEFT * 1.5 + DOWN * 0.5, RIGHT * 1.5 + DOWN * 0.5, buff=0.05, color=ORANGE, stroke_width=3),
            Arrow(RIGHT * 1.5 + DOWN * 1.2, LEFT * 1.5 + DOWN * 1.2, buff=0.05, color=TEAL, stroke_width=3),
        )
        cap = self.ja_text("二回ループ", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("メモリ節約", font_size=24).move_to(self.note)
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
        eq = MathTex(r"H_k \approx \mathrm{LBFGS}(\{s_i,y_i\})").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"H_k \approx \mathrm{LBFGS}(\{s_i,y_i\})").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"H_k \approx \mathrm{LBFGS}(\{s_i,y_i\})").scale(0.82)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
