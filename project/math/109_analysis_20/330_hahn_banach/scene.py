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
        self.derive()
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

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"f|_Y").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"f|_Y=g,\ \|f\|=\|g\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"f|_Y=g,\ \|f\|=\|g\|").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
