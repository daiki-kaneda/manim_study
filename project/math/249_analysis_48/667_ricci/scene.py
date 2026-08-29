from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class RicciFlow(PacedScene):
    """#667 リッチ流：計量をリッチ曲率で変形（約45秒）"""

    def construct(self):
        self.show_heading("リッチ流")
        self.draw()
        self.evolve()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        # bumpy ellipse -> rounder
        e1 = Ellipse(width=4.0, height=2.0, color=BLUE, stroke_width=3).shift(UP * 0.15)
        e2 = Ellipse(width=3.0, height=2.6, color=TEAL, stroke_width=3).shift(UP * 0.15)
        self.play(Create(e1), run_time=1.0)
        self.play(Transform(e1, e2), run_time=1.1)
        note = self.ja_text("計量が進化", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def evolve(self):
        cap = self.ja_text("曲率を均一化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ポアンカレ予想へ", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\partial_t g_{ij}=-2\mathrm{Ric}_{ij}").scale(0.8)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
