from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class TomitaTakesaki(PacedScene):
    """#510 冨田竹崎：モジュラー自己同型の流れ（約45秒）"""

    def construct(self):
        self.show_heading("冨田竹崎")
        self.draw_algebra()
        self.flow()
        self.show_formula()
        self.read(1.4)

    def draw_algebra(self):
        m = RoundedRectangle(width=2.8, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.3 + UP * 0.2)
        self.play(Create(m), FadeIn(MathTex(r"M", font_size=36).move_to(m)), run_time=1.2)
        note = self.ja_text("フォンノイマン代数", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def flow(self):
        arrows = VGroup(*[
            CurvedArrow(LEFT * 0.5 + UP * (0.9 - i * 0.7), RIGHT * 2.4 + UP * (0.9 - i * 0.7), color=c, tip_length=0.2)
            for i, c in enumerate([ORANGE, TEAL, YELLOW])
        ])
        cap = self.ja_text("モジュラー流", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("状態が流れを決める", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\sigma_t^\varphi(x)=\Delta^{it}x\Delta^{-it}").scale(0.88)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
