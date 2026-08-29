from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Filtration(PacedScene):
    """#496 フィルトレーション：情報が単調に増える（約45秒）"""

    def construct(self):
        self.show_heading("フィルトレーション")
        self.draw_sigma()
        self.nested()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_sigma(self):
        rings = VGroup(*[
            Circle(radius=0.7 + i * 0.55, color=c, stroke_width=3).shift(LEFT * 1.8 + UP * 0.1)
            for i, c in enumerate([BLUE, TEAL, ORANGE])
        ])
        labs = VGroup(*[
            MathTex(rf"\mathcal{{F}}_{{{t}}}", font_size=28).move_to(LEFT * 1.8 + UP * (0.1) + RIGHT * (0.35 + i * 0.35) + UP * (0.9 - i * 0.15))
            for i, t in enumerate(["1", "2", "3"])
        ])
        self.play(LaggedStart(*[Create(r) for r in rings], lag_ratio=0.2), FadeIn(labs), run_time=1.5)
        note = self.ja_text("情報の増大", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def nested(self):
        arrow = Arrow(LEFT * 0.2, RIGHT * 2.4, buff=0.05, color=YELLOW, stroke_width=4).shift(DOWN * 1.0)
        cap = self.ja_text("入れ子のσ加法族", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("適合過程の土台", font_size=24).move_to(self.note)
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
        eq = MathTex(r"s\le t\ \Rightarrow\ \mathcal{F}_s\subset\mathcal{F}_t").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"s\le t\ \Rightarrow\ \mathcal{F}_s\subset\mathcal{F}_t").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"s\le t\ \Rightarrow\ \mathcal{F}_s\subset\mathcal{F}_t").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
