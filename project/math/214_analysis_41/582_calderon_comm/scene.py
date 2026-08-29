from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CalderonCommutator(PacedScene):
    """#582 カルデロン交換子：[H,a] の有界性（約45秒）"""

    def construct(self):
        self.show_heading("カルデロン交換子")
        self.draw_ops()
        self.comm()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        H = RoundedRectangle(width=2.0, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.6 + UP * 0.2)
        a = RoundedRectangle(width=2.0, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.6 + UP * 0.2)
        self.play(Create(H), FadeIn(MathTex(r"H", font_size=36).move_to(H)),
                  Create(a), FadeIn(MathTex(r"a", font_size=36).move_to(a)), run_time=1.3)
        note = self.ja_text("ヒルベルト変換", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def comm(self):
        box = RoundedRectangle(width=2.8, height=1.2, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(DOWN * 0.9)
        cap = self.ja_text("交換子が有界", font_size=24).move_to(self.note)
        self.play(Create(box), FadeIn(MathTex(r"[H,a]", font_size=34).move_to(box)), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("リプシッツで十分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"[H,a]f=H(af)-a\,Hf").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
