from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class HahnBanach(PacedScene):
    """#330 ハーン・バナッハ：部分空間の線形汎関数を拡張（約45秒）"""

    def construct(self):
        self.show_heading("ハーン・バナッハの定理")
        self.draw_subspace()
        self.extend()
        self.show_formula()
        self.read(1.4)

    def draw_subspace(self):
        self.O = LEFT * 0.8 + DOWN * 0.2
        plane = Line(self.O + LEFT * 2.6, self.O + RIGHT * 2.8, color=GREY, stroke_width=4)
        y = Line(self.O + DOWN * 1.8, self.O + UP * 1.8, color=BLUE, stroke_width=5)
        self.play(Create(plane), run_time=0.9)
        self.play(Create(y), run_time=0.9)
        note = self.ja_text("部分空間", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def extend(self):
        # functional as dashed level lines then wider plane
        levels = VGroup(*[
            DashedLine(self.O + LEFT * 2.2 + UP * h, self.O + RIGHT * 2.4 + UP * h, color=ORANGE, stroke_width=2)
            for h in [-1.0, -0.3, 0.4, 1.1]
        ])
        cap = self.ja_text("汎関数", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in levels], lag_ratio=0.1), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        wide = Rectangle(width=5.2, height=3.2, color=YELLOW, stroke_width=3).move_to(self.O + RIGHT * 0.1)
        cap2 = self.ja_text("全体へ拡張", font_size=24).move_to(self.note)
        self.play(Create(wide), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"f|_Y=g,\ \|f\|=\|g\|").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
