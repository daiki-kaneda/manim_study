from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class SSOR(PacedScene):
    """#574 SSOR：対称化された SOR 前処理（約45秒）"""

    def construct(self):
        self.show_heading("SSOR")
        self.draw_sweep()
        self.sym()
        self.show_formula()
        self.read(1.4)

    def draw_sweep(self):
        arrows = VGroup(
            Arrow(LEFT * 2.8 + UP * 0.6, RIGHT * 2.8 + UP * 0.6, buff=0.05, color=BLUE, stroke_width=4),
            Arrow(RIGHT * 2.8 + DOWN * 0.4, LEFT * 2.8 + DOWN * 0.4, buff=0.05, color=ORANGE, stroke_width=4),
        )
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.25), run_time=1.4)
        note = self.ja_text("往復スイープ", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def sym(self):
        cap = self.ja_text("対称な前処理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("CG と相性良い", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"M=(D-\omega L)D^{-1}(D-\omega U)/\omega(2-\omega)").scale(0.62)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
