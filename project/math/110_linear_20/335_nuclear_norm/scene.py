from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class NuclearNorm(PacedScene):
    """#335 核ノルム：特異値の和（約45秒）"""

    def construct(self):
        self.show_heading("核ノルム")
        self.draw_sv()
        self.sum_them()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_sv(self):
        heights = [2.0, 1.3, 0.7, 0.35]
        self.bars = VGroup()
        for i, h in enumerate(heights):
            b = Rectangle(width=0.8, height=h, color=BLUE, fill_opacity=0.55, stroke_width=2)
            b.move_to(LEFT * 2.6 + RIGHT * i * 1.15 + UP * (h / 2 - 0.5))
            lab = MathTex(rf"\sigma_{{{i+1}}}", font_size=28).next_to(b, DOWN, buff=0.15)
            self.bars.add(VGroup(b, lab))
        self.play(LaggedStart(*[FadeIn(b) for b in self.bars], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("特異値", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sum_them(self):
        brace = Brace(VGroup(*[b[0] for b in self.bars]), UP, color=ORANGE)
        cap = self.ja_text("全部足す", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        total = MathTex(r"\|A\|_*", color=YELLOW, font_size=42).shift(RIGHT * 2.6 + UP * 0.4)
        cap2 = self.ja_text("核ノルム", font_size=24).move_to(self.note)
        self.play(FadeIn(total), Transform(self.note, cap2), run_time=1.2)
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
        eq = MathTex(r"\|A\|_*").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\|A\|_*=\sum_i\sigma_i(A)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\|A\|_*=\sum_i\sigma_i(A)").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
