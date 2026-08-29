from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class SpectralProjection(PacedScene):
    """#426 スペクトル射影：スペクトル部分集合への射影（約45秒）"""

    def construct(self):
        self.show_heading("スペクトル射影")
        self.draw_spec()
        self.cut()
        self.show_formula()
        self.read(1.4)

    def draw_spec(self):
        self.O = LEFT * 0.2
        ax = Line(self.O + LEFT * 3.0, self.O + RIGHT * 3.2, color=GREY, stroke_width=2)
        band = Line(self.O + LEFT * 1.8, self.O + RIGHT * 2.0, color=BLUE, stroke_width=10)
        self.play(Create(ax), Create(band), run_time=1.3)
        note = self.ja_text("スペクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.band = band

    def cut(self):
        hi = Line(self.O + RIGHT * 0.2, self.O + RIGHT * 2.0, color=ORANGE, stroke_width=12)
        box = SurroundingRectangle(hi, color=YELLOW, buff=0.15)
        cap = self.ja_text("一部を切り出す", font_size=24).move_to(self.note)
        self.play(Create(hi), Create(box), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("射影作用素", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"E(\Delta)^2=E(\Delta)").scale(0.95)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
