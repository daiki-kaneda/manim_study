from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GromovWitten(PacedScene):
    """#714 グロモフ・ウィッテン：正則曲線の数え上げ不変量（約45秒）"""

    def construct(self):
        self.show_heading("グロモフ・ウィッテン")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        box = RoundedRectangle(width=3.8, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 0.4 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"\overline{\mathcal{M}}_{g,n}", font_size=28).move_to(box)), run_time=1.3)

        note = self.ja_text("正則曲線", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("仮想基本類", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("量子コホモロジーへ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"GW_{g,n}(X)=\langle\alpha\rangle_{g,n}^X").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
