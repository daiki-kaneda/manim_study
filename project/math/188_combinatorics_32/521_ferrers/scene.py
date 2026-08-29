from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class FerrersDiagram(PacedScene):
    """#521 フェラーズ図：分割を点の並びで見る（約45秒）"""

    def construct(self):
        self.show_heading("フェラーズ図")
        self.draw_dots()
        self.conjugate()
        self.show_formula()
        self.read(1.4)

    def draw_dots(self):
        rows = [5, 3, 3, 1]
        dots = VGroup()
        for i, n in enumerate(rows):
            for j in range(n):
                dots.add(Dot(LEFT * 2.5 + RIGHT * j * 0.55 + UP * 1.3 + DOWN * i * 0.55, color=BLUE, radius=0.12))
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.03), run_time=1.4)
        note = self.ja_text("分割の図", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def conjugate(self):
        cap = self.ja_text("転置で共役分割", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ヤング図形と同型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\lambda=(5,3,3,1)\ \longleftrightarrow\ \text{Ferrers}").scale(0.82)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
