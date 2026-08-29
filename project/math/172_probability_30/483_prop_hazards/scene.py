from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


import numpy as np


class ProportionalHazards(PacedScene):
    """#483 比例ハザード：共変量で基準ハザードを倍率（約45秒）"""

    def construct(self):
        self.show_heading("比例ハザード")
        self.draw_curves()
        self.ratio()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_curves(self):
        axes = Axes(
            x_range=[0, 4.2, 1], y_range=[0, 1.3, 1],
            x_length=6.5, y_length=2.6, tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(UP * 0.4)
        h0 = axes.plot(lambda t: 0.15 + 0.08 * t, x_range=[0, 4], color=BLUE, stroke_width=4)
        h1 = axes.plot(lambda t: 1.8 * (0.15 + 0.08 * t), x_range=[0, 4], color=ORANGE, stroke_width=4)
        self.play(Create(axes), Create(h0), run_time=1.2)
        self.play(Create(h1), run_time=0.9)
        note = self.ja_text("基準と倍率", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ratio(self):
        brace = BraceBetweenPoints(LEFT * 2.5 + DOWN * 0.9, RIGHT * 2.5 + DOWN * 0.9, color=YELLOW)
        cap = self.ja_text("比は時間一定", font_size=24).move_to(self.note)
        self.play(GrowFromCenter(brace), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("コックス模型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"h(t\mid x)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"h(t\mid x)=h_0(t)\,e^{\beta^\top x}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"h(t\mid x)=h_0(t)\,e^{\beta^\top x}").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
