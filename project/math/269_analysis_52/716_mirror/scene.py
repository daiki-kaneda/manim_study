from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MirrorSymmetry(PacedScene):
    """#716 ミラー対称性：複素とシンプレクティックの双対（約45秒）"""

    def construct(self):
        self.show_heading("ミラー対称性")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        left = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        right = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        self.play(Create(left), Create(right),
                  FadeIn(MathTex(r"X", font_size=34).move_to(left)),
                  FadeIn(MathTex(r"X^\vee", font_size=34).move_to(right)), run_time=1.4)

        note = self.ja_text("双対な対", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("A模型とB模型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("周期と曲線数え", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"X\longleftrightarrow X^\vee").scale(0.85)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
