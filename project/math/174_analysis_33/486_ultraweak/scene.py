from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class UltraweakTopology(PacedScene):
    """#486 超弱作用素位相：トレース双対で決まる位相（約45秒）"""

    def construct(self):
        self.show_heading("超弱作用素位相")
        self.draw_dual()
        self.nets()
        self.show_formula()
        self.read(1.4)

    def draw_dual(self):
        box = RoundedRectangle(width=3.2, height=1.6, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.0 + UP * 0.2)
        lab = MathTex(r"B(H)_*", font_size=36).move_to(box)
        self.play(Create(box), FadeIn(lab), run_time=1.3)
        note = self.ja_text("トレースクラス双対", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def nets(self):
        arrows = VGroup(*[
            Arrow(LEFT * 0.2 + UP * (0.8 - i * 0.7), RIGHT * 2.6 + UP * (0.8 - i * 0.7),
                  buff=0.05, color=c, stroke_width=3)
            for i, c in enumerate([ORANGE, TEAL, YELLOW])
        ])
        cap = self.ja_text("汎関数で収束", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("WOTより細かい", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"T_\alpha\to T\ \Leftrightarrow\ \mathrm{tr}(\rho T_\alpha)\to\mathrm{tr}(\rho T)").scale(0.72)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
