from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AdamW(PacedScene):
    """#657 AdamW：重み減衰を勾配から分離（約45秒）"""

    def construct(self):
        self.show_heading("AdamW")
        self.draw_split()
        self.decay()
        self.show_formula()
        self.read(1.4)

    def draw_split(self):
        left = RoundedRectangle(width=2.8, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.2 + UP * 0.25)
        right = RoundedRectangle(width=2.8, height=1.3, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.2 + UP * 0.25)
        self.play(Create(left), Create(right),
                  FadeIn(MathTex(r"\mathrm{Adam}", font_size=30).move_to(left)),
                  FadeIn(MathTex(r"\lambda\theta", font_size=30).move_to(right)), run_time=1.4)
        note = self.ja_text("減衰を分離", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def decay(self):
        cap = self.ja_text("真の weight decay", font_size=22).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("汎化に効く", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\theta\leftarrow\theta-\eta(\hat m/\sqrt{\hat v}+\lambda\theta)").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
