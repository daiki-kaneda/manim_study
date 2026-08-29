from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LucasTheorem(PacedScene):
    """#341 リュカの定理：素数 p で二項係数を桁ごとに（約45秒）"""

    def construct(self):
        self.show_heading("リュカの定理")
        self.draw_digits()
        self.product()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_digits(self):
        n = MathTex(r"n=(n_r\ldots n_0)_p", font_size=40).shift(UP * 1.2 + LEFT * 0.3)
        k = MathTex(r"k=(k_r\ldots k_0)_p", font_size=40).shift(UP * 0.35 + LEFT * 0.3)
        self.play(Write(n), Write(k), run_time=1.6)
        note = self.ja_text("p 進展開", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def product(self):
        boxes = VGroup()
        for i in range(3):
            b = RoundedRectangle(width=1.4, height=0.85, corner_radius=0.08, color=BLUE, stroke_width=3)
            b.shift(LEFT * 2.0 + RIGHT * i * 1.7 + DOWN * 0.7)
            t = MathTex(rf"\binom{{n_{i}}}{{k_{i}}}", font_size=30).move_to(b)
            boxes.add(VGroup(b, t))
        cap = self.ja_text("桁ごと", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        times = MathTex(r"\times", font_size=36).move_to(DOWN * 0.7)
        # place between boxes - visual only
        cap2 = self.ja_text("積が合同", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(boxes, color=YELLOW), run_time=1.2)
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
        eq = MathTex(r"\binom{n}{k}\equiv\prod_i\binom{n_i}{k_i}\pmod p").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\binom{n}{k}\equiv\prod_i\binom{n_i}{k_i}\pmod p").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\binom{n}{k}\equiv\prod_i\binom{n_i}{k_i}\pmod p").scale(0.8)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=2.0)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
