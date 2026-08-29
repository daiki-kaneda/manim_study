from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class SymmedianPoint(PacedScene):
    """#662 類似中線点：類似中線の交点（約45秒）"""

    def construct(self):
        self.show_heading("類似中線点")
        self.draw()
        self.reflect()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        A, B, C = UP * 1.9, LEFT * 2.7 + DOWN * 1.2, RIGHT * 2.7 + DOWN * 1.2
        tri = Polygon(A, B, C, color=BLUE, stroke_width=3)
        # median rough
        med = DashedLine(A, (B + C) / 2, color=GREY, stroke_width=2)
        # symmedian tilted
        sym = Line(A, (B + C) / 2 + RIGHT * 0.55, color=ORANGE, stroke_width=3)
        self.play(Create(tri), Create(med), Create(sym), run_time=1.4)
        note = self.ja_text("中線の鏡映", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def reflect(self):
        K = Dot(UP * 0.15, color=TEAL, radius=0.1)
        cap = self.ja_text("三本が一点", font_size=24).move_to(self.note)
        self.play(FadeIn(K), Transform(self.note, cap), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("等角共役は重心", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"K=X(6)").scale(0.9)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
