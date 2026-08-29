from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Bootstrap(PacedScene):
    """#316 ブートストラップ：再標本でばらつきを見る（約45秒）"""

    def construct(self):
        self.show_heading("ブートストラップ")
        self.draw_sample()
        self.resample()
        self.show_formula()
        self.read(1.4)

    def draw_sample(self):
        self.dots = VGroup(*[
            Dot(LEFT * 2.5 + RIGHT * i * 0.55 + UP * (0.2 if i % 2 == 0 else -0.2), color=BLUE, radius=0.1)
            for i in range(7)
        ])
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in self.dots], lag_ratio=0.08), run_time=1.3)
        note = self.ja_text("元の標本", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def resample(self):
        # arrows to new samples
        groups = VGroup()
        for g in range(3):
            row = VGroup(*[
                Dot(RIGHT * 1.5 + RIGHT * i * 0.35 + DOWN * (g * 0.55) + UP * 0.6, color=ORANGE, radius=0.07)
                for i in range(5)
            ])
            groups.add(row)
        arrows = VGroup(*[
            Arrow(ORIGIN + LEFT * 0.2, RIGHT * 1.2 + DOWN * (g * 0.55) + UP * 0.6, buff=0.1, color=YELLOW, stroke_width=3)
            for g in range(3)
        ])
        cap = self.ja_text("復元抽出", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1), Transform(self.note, cap), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(r) for r in groups], lag_ratio=0.12), run_time=1.1)
        self.read(0.25)
        cap2 = self.ja_text("ばらつきを見る", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\widehat{\mathrm{Var}}(\hat\theta)\approx\mathrm{Var}^*(\hat\theta^*)").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
