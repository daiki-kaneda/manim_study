from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MarkIntensity(PacedScene):
    """#604 マーク強度：印ごとの発生率（約45秒）"""

    def construct(self):
        self.show_heading("マーク強度")
        self.draw_marks()
        self.rates()
        self.show_formula()
        self.read(1.4)

    def draw_marks(self):
        line = NumberLine(x_range=[0, 6, 1], length=7, include_numbers=False).shift(UP * 0.4)
        items = [(0.7, "a"), (1.6, "b"), (2.8, "a"), (3.9, "c"), (5.1, "b")]
        dots = VGroup(*[Dot(line.n2p(x), color=YELLOW, radius=0.1) for x, _ in items])
        labs = VGroup(*[MathTex(m, font_size=26).next_to(dots[i], UP, buff=0.12) for i, (_, m) in enumerate(items)])
        self.play(Create(line), FadeIn(dots), FadeIn(labs), run_time=1.4)
        note = self.ja_text("印つき点", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def rates(self):
        cap = self.ja_text("印ごとに強度", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("結合強度から分解", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\lambda(t,dm)=\lambda(t)\,Q(t,dm)").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
