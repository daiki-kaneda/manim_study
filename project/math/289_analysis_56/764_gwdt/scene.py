from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GWDTCorrespondence(PacedScene):
    """#764 GW-DT対応：二つの数え上げの関係（約45秒）"""

    def construct(self):
        self.show_heading("GW-DT対応")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        left = RoundedRectangle(width=2.5, height=1.4, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        right = RoundedRectangle(width=2.5, height=1.4, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        self.play(Create(left), Create(right),
                  FadeIn(MathTex(r"GW", font_size=32).move_to(left)),
                  FadeIn(MathTex(r"DT", font_size=32).move_to(right)), run_time=1.4)
        note = self.ja_text("変数変換で結ぶ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("MNOP対応", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("3つ折りで成立", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Z_{GW}(u)=Z_{DT}(-e^{iu})").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
