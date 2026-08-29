from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Warmup(PacedScene):
    """#671 ウォームアップ：序盤だけ学習率を上げる（約45秒）"""

    def construct(self):
        self.show_heading("ウォームアップ")
        self.draw()
        self.ramp()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.2, y_length=2.3,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.2 + UP * 0.15)
        import math
        warm = axes.plot(lambda t: (1.5 * t / 1.0) if t < 1 else 1.5 * math.exp(-0.35 * (t - 1)), x_range=[0.05, 3.8], color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(warm), run_time=1.4)
        note = self.ja_text("序盤で上昇", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ramp(self):
        cap = self.ja_text("線形に立ち上げ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("大バッチ安定化", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\eta_t").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\eta_t=\eta\cdot\min(1,t/t_w)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\eta_t=\eta\cdot\min(1,t/t_w)").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
