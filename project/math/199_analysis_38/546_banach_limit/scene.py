from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class BanachLimit(PacedScene):
    """#546 バナッハ極限：シフト不変な有界列の極限（約45秒）"""

    def construct(self):
        self.show_heading("バナッハ極限")
        self.draw_seq()
        self.shift_inv()
        self.show_formula()
        self.read(1.4)

    def draw_seq(self):
        vals = ["a1", "a2", "a3", "a4", "a5"]
        cells = VGroup(*[MathTex(rf"a_{{{i+1}}}", font_size=32).shift(LEFT * 2.8 + RIGHT * i * 1.1 + UP * 0.5) for i in range(5)])
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.08), run_time=1.3)
        note = self.ja_text("有界列", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def shift_inv(self):
        arrow = Arrow(LEFT * 1.5 + DOWN * 0.5, RIGHT * 1.5 + DOWN * 0.5, buff=0.05, color=ORANGE, stroke_width=4)
        cap = self.ja_text("シフト不変", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("ハーンバナッハ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathrm{LIM}(a_{n+1})=\mathrm{LIM}(a_n)").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
