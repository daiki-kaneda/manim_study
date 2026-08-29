from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene

class Fagnano(PacedScene):
    """#420 ファニャーノ：周長最小の内接三角形は垂足（約45秒）"""

    def construct(self):
        self.show_heading("ファニャーノの問題")
        self.draw_triangle()
        self.orthic()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.2 + LEFT * 0.2
        self.B = LEFT * 2.7 + DOWN * 1.5
        self.C = RIGHT * 2.8 + DOWN * 1.4
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("鋭角三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def orthic(self):
        # feet of altitudes (schematic)
        Ha = 0.55 * self.B + 0.45 * self.C
        Hb = 0.55 * self.A + 0.45 * self.C
        Hc = 0.55 * self.A + 0.45 * self.B
        orth = Polygon(Ha, Hb, Hc, color=ORANGE, stroke_width=3)
        alts = VGroup(DashedLine(self.A, Ha, color=GREY, stroke_width=2),
                      DashedLine(self.B, Hb, color=GREY, stroke_width=2),
                      DashedLine(self.C, Hc, color=GREY, stroke_width=2))
        cap = self.ja_text("垂線の足", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(a) for a in alts], lag_ratio=0.1), Transform(self.note, cap), run_time=1.3)
        self.play(Create(orth), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("周長が最小", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(orth, color=YELLOW), run_time=1.1)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("垂足三角形が周長最小", font_size=28)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
