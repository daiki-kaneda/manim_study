from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class GreensFunction(PacedScene):
    """#236 グリーン関数は点源への応答（約45秒）"""

    def construct(self):
        self.show_heading("グリーン関数")
        self.draw_source()
        self.response()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_source(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[-0.2, 2.2, 1],
            x_length=8.0,
            y_length=3.0,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.2 + LEFT * 0.15)
        self.play(Create(self.axes), run_time=0.8)
        src = Arrow(self.axes.c2p(2.0, 2.0), self.axes.c2p(2.0, 0.15), buff=0, color=RED, stroke_width=5)
        self.play(GrowArrow(src), run_time=1.0)
        note = self.ja_text("点源", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def response(self):
        # 1D green-like tent / exponential decay from source
        g = self.axes.plot(
            lambda x: 1.6 * math.exp(-1.8 * abs(x - 2.0)),
            x_range=[0.05, 4.1],
            color=TEAL,
            stroke_width=5,
        )
        cap = self.ja_text("応答", font_size=24).move_to(self.note)
        self.play(Create(g), Transform(self.note, cap), run_time=1.6)
        self.read(0.3)
        # second source
        g2 = self.axes.plot(
            lambda x: 1.0 * math.exp(-1.8 * abs(x - 0.9)) + 0.7 * math.exp(-1.8 * abs(x - 3.1)),
            x_range=[0.05, 4.1],
            color=YELLOW,
            stroke_width=4,
        )
        cap2 = self.ja_text("重ね合わせ", font_size=24).move_to(self.note)
        self.play(Transform(g, g2), Transform(self.note, cap2), run_time=1.5)
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
        eq = MathTex(r"Lu").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"Lu=f\Rightarrow u=G*f").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"Lu=f\Rightarrow u=G*f").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
