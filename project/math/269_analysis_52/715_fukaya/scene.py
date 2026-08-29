from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FukayaCategory(PacedScene):
    """#715 深谷圏：ラグランジュ部分多様体の圏（約45秒）"""

    def construct(self):
        self.show_heading("深谷圏")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        ell = Ellipse(width=3.5, height=2.0, color=BLUE, stroke_width=3).shift(UP * 0.2)
        L1 = Line(LEFT * 1.5 + DOWN * 0.5, RIGHT * 1.5 + UP * 0.8, color=ORANGE, stroke_width=3)
        L2 = Line(LEFT * 1.2 + UP * 0.9, RIGHT * 1.2 + DOWN * 0.7, color=TEAL, stroke_width=3)
        self.play(Create(ell), Create(L1), Create(L2), run_time=1.4)

        note = self.ja_text("ラグランジュ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("フロアー鎖複体", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ホモロジーミラー", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathrm{Hom}(L_0,L_1)=CF(L_0,L_1)").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
