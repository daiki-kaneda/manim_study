from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EvansKrylov(PacedScene):
    """#654 エヴァンス・クリロフ：完全非線形楕円の C^{2,α}（約45秒）"""

    def construct(self):
        self.show_heading("エヴァンス・クリロフ")
        self.draw_pde()
        self.reg()
        self.show_formula()
        self.read(1.4)

    def draw_pde(self):
        box = RoundedRectangle(width=4.0, height=1.4, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 0.5 + UP * 0.25)
        self.play(Create(box), FadeIn(MathTex(r"F(D^2u)=0", font_size=36).move_to(box)), run_time=1.3)
        note = self.ja_text("完全非線形", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def reg(self):
        cap = self.ja_text("内部正則性", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("C²,α 評価", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\|u\|_{C^{2,\alpha}(B')}\le C\|u\|_{L^\infty(B)}").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
