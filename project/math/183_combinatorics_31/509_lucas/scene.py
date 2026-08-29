from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class LucasNumbers(PacedScene):
    """#509 リュカ数：フィボナッチの兄弟数列（約45秒）"""

    def construct(self):
        self.show_heading("リュカ数")
        self.draw_seq()
        self.relation()
        self.show_formula()
        self.read(1.4)

    def draw_seq(self):
        vals = ["2", "1", "3", "4", "7", "11", "18"]
        cells = VGroup(*[
            MathTex(v, font_size=36).shift(LEFT * 3.0 + RIGHT * i * 1.0 + UP * 0.6)
            for i, v in enumerate(vals)
        ])
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.08), run_time=1.4)
        note = self.ja_text("L0=2, L1=1", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def relation(self):
        cap = self.ja_text("同じ漸化式", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("フィボと密接", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"L_n=L_{n-1}+L_{n-2},\quad L_n=F_{n-1}+F_{n+1}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
