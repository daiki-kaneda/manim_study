from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class StraussProcess(PacedScene):
    """#771 シュトラウス過程：近接ペナルティ付き点過程（約45秒）"""

    def construct(self):
        self.show_heading("シュトラウス過程")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        import random
        random.seed(12)
        pts = VGroup(*[Dot([random.uniform(-2.7, 2.7), random.uniform(-1.1, 1.1), 0], radius=0.07, color=BLUE) for _ in range(18)])
        pair = Line(pts[0].get_center(), pts[1].get_center(), color=ORANGE, stroke_width=3)
        self.play(FadeIn(pts), Create(pair), run_time=1.3)
        note = self.ja_text("近接で罰則", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("パラメータ γ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ハードコアの弱形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"p\propto\gamma^{s(x)}").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
