from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class KosnitaPoint(PacedScene):
    """#769 コスニタ点：外心と頂点外心の共線性（約45秒）"""

    def construct(self):
        self.show_heading("コスニタ点")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        tri = Polygon(LEFT * 2.5 + DOWN * 1.0, RIGHT * 2.5 + DOWN * 1.0, UP * 1.6, color=BLUE, stroke_width=3)
        O = Dot(ORIGIN + DOWN * 0.1, color=YELLOW, radius=0.1)
        K = Dot(ORIGIN + UP * 0.35, color=TEAL, radius=0.1)
        self.play(Create(tri), FadeIn(O), FadeIn(K),
                  Create(DashedLine(O.get_center(), K.get_center(), color=GREY)), run_time=1.4)
        note = self.ja_text("外心と結ぶ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("共線条件", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("X(54)", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"K=X(54)").scale(0.9)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
