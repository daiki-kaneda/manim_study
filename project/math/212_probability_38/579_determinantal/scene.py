from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class DeterminantalPP(PacedScene):
    """#579 決定点過程：核の行列式で反発（約45秒）"""

    def construct(self):
        self.show_heading("決定点過程")
        self.draw_points()
        self.repulsion()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        dots = VGroup(*[
            Dot(LEFT * 2.5 + RIGHT * (i % 4) * 1.2 + UP * (0.8 - (i // 4) * 1.2), color=BLUE, radius=0.12)
            for i in range(8)
        ])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.06), run_time=1.3)
        note = self.ja_text("点が反発", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def repulsion(self):
        cap = self.ja_text("核 K で確率", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("行列式が密度", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"P(x_1,\ldots,x_n)\propto\det[K(x_i,x_j)]").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
