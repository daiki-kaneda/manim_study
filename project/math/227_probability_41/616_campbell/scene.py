from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CampbellFormula(PacedScene):
    """#616 キャンベル公式：点過程の期待値を強度で積分（約45秒）"""

    def construct(self):
        self.show_heading("キャンベル公式")
        self.draw_sum()
        self.intensity()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_sum(self):
        line = NumberLine(x_range=[0, 5, 1], length=6.5, include_numbers=False).shift(UP * 0.6)
        xs = [0.7, 1.6, 2.5, 3.4, 4.3]
        dots = VGroup(*[Dot(line.n2p(x), color=YELLOW, radius=0.09) for x in xs])
        bars = VGroup(*[
            Line(line.n2p(x), line.n2p(x) + UP * (0.4 + 0.25 * (i % 3)), color=BLUE, stroke_width=4)
            for i, x in enumerate(xs)
        ])
        self.play(Create(line), FadeIn(dots), LaggedStart(*[Create(b) for b in bars], lag_ratio=0.08), run_time=1.4)
        note = self.ja_text("点ごとの和", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def intensity(self):
        cap = self.ja_text("強度で積分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("メッケの拡張", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\mathbb{E}\sum_{x\in\Phi}f(x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\mathbb{E}\sum_{x\in\Phi}f(x)=\int f(x)\lambda(dx)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\mathbb{E}\sum_{x\in\Phi}f(x)=\int f(x)\lambda(dx)").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
