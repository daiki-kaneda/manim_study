from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class Likelihood(PacedScene):
    """#268 尤度はデータのもとでのパラメータの高さ（約45秒）"""

    def construct(self):
        self.show_heading("尤度関数")
        self.draw_data()
        self.sweep_param()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_data(self):
        self.axes = Axes(
            x_range=[-0.2, 4.2, 1],
            y_range=[0, 1.15, 1],
            x_length=7.8,
            y_length=2.9,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.1 + LEFT * 0.2)
        self.play(Create(self.axes), run_time=0.75)
        xs = [1.1, 1.6, 2.0, 2.4, 2.9]
        self.data = VGroup(*[Dot(self.axes.c2p(x, 0), color=YELLOW, radius=0.08) for x in xs])
        self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in self.data], lag_ratio=0.1), run_time=1.2)
        note = self.ja_text("データ", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.xs = xs

    def sweep_param(self):
        self.curve = None
        for mu, label, col in ((1.2, "合わない", BLUE), (2.0, "よく合う", ORANGE), (3.1, "また外れる", TEAL)):
            f = self.axes.plot(
                lambda x, m=mu: 0.85 * math.exp(-2.5 * (x - m) ** 2),
                x_range=[0.1, 4.0],
                color=col,
                stroke_width=4,
            )
            # stems to data
            stems = VGroup()
            for x in self.xs:
                y = 0.85 * math.exp(-2.5 * (x - mu) ** 2)
                stems.add(DashedLine(self.axes.c2p(x, 0), self.axes.c2p(x, y), color=GREY_B, stroke_width=2))
            cap = self.ja_text(label, font_size=24).move_to(self.note)
            if self.curve is None:
                self.play(Create(f), FadeIn(stems), Transform(self.note, cap), run_time=1.3)
                self.curve = f
                self.stems = stems
            else:
                self.play(Transform(self.curve, f), Transform(self.stems, stems), Transform(self.note, cap), run_time=1.25)
            self.read(0.2)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"L(\theta)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"L(\theta)=\prod_i f(x_i\mid\theta)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"L(\theta)=\prod_i f(x_i\mid\theta)").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
