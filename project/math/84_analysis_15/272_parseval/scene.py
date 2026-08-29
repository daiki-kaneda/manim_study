from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ParsevalIdentity(PacedScene):
    """#272 パーセバル：完全なら二乗和＝ノルム（約45秒）"""

    def construct(self):
        self.show_heading("パーセバルの等式")
        self.draw_energy()
        self.complete()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_energy(self):
        # bars for |c_k|^2
        heights = [1.8, 1.2, 0.7, 0.4]
        self.bars = VGroup()
        for i, h in enumerate(heights):
            b = Rectangle(width=0.7, height=h, color=BLUE, fill_opacity=0.55, stroke_width=2)
            b.move_to(LEFT * 2.8 + RIGHT * i * 1.0 + UP * (h / 2 - 0.6))
            self.bars.add(b)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in self.bars], lag_ratio=0.12), run_time=1.5)
        note = self.ja_text("係数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def complete(self):
        total_h = sum(b.height for b in self.bars) * 0.55
        energy = Rectangle(width=1.1, height=total_h, color=ORANGE, fill_opacity=0.65, stroke_width=3)
        energy.move_to(RIGHT * 2.6 + UP * (total_h / 2 - 0.6))
        brace = Brace(self.bars, DOWN, color=YELLOW)
        cap = self.ja_text("全部足す", font_size=24).move_to(self.note)
        self.play(FadeIn(brace), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("一致", font_size=24).move_to(self.note)
        arrow = Arrow(brace.get_right(), energy.get_left(), buff=0.15, color=YELLOW)
        self.play(GrowArrow(arrow), FadeIn(energy), Transform(self.note, cap2), run_time=1.5)
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
        eq = MathTex(r"\sum_k|c_k|^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\sum_k|c_k|^{2}=\|f\|^{2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\sum_k|c_k|^{2}=\|f\|^{2}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
