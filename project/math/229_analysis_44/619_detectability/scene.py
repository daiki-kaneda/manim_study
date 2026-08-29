from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Detectability(PacedScene):
    """#619 可検出性：観測できないモードは安定（約45秒）"""

    def construct(self):
        self.show_heading("可検出性")
        self.draw_modes()
        self.stable()
        self.show_formula()
        self.read(1.4)

    def draw_modes(self):
        left = RoundedRectangle(width=2.8, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.2)
        right = RoundedRectangle(width=2.8, height=1.5, corner_radius=0.12, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.2)
        self.play(Create(left), Create(right),
                  FadeIn(MathTex(r"C", font_size=34).move_to(left)),
                  FadeIn(MathTex(r"\ker C", font_size=30).move_to(right)),
                  run_time=1.4)
        note = self.ja_text("見えぬ部分空間", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def stable(self):
        cap = self.ja_text("不可観測は安定", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("可観測の弱形", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Ax=\lambda x,\ Cx=0\ \Rightarrow\ \Re\lambda<0").scale(0.72)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
