from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class TotalVariation(PacedScene):
    """#303 全変動距離：分布の差の半分（約45秒）"""

    def construct(self):
        self.show_heading("全変動距離")
        self.draw_masses()
        self.diff()
        self.show_formula()
        self.read(1.4)

    def draw_masses(self):
        self.p = VGroup()
        self.q = VGroup()
        hp = [1.6, 1.1, 0.6]
        hq = [0.7, 1.4, 1.2]
        for i, (a, b) in enumerate(zip(hp, hq)):
            ba = Rectangle(width=0.7, height=a, color=BLUE, fill_opacity=0.55, stroke_width=2)
            bb = Rectangle(width=0.7, height=b, color=TEAL, fill_opacity=0.55, stroke_width=2)
            ba.move_to(LEFT * 2.8 + RIGHT * i * 1.0 + UP * (a / 2 - 0.7))
            bb.move_to(RIGHT * 0.4 + RIGHT * i * 1.0 + UP * (b / 2 - 0.7))
            self.p.add(ba)
            self.q.add(bb)
        self.play(LaggedStart(*[FadeIn(x) for x in self.p], lag_ratio=0.1), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(x) for x in self.q], lag_ratio=0.1), run_time=1.1)
        note = self.ja_text("2 つの分布", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def diff(self):
        diffs = VGroup()
        for i, (a, b) in enumerate(zip(self.p, self.q)):
            h = abs(a.height - b.height) * 0.9
            d = Rectangle(width=0.7, height=h, color=ORANGE, fill_opacity=0.65, stroke_width=2)
            d.move_to(RIGHT * 2.8 + UP * (h / 2 - 0.7))
            # stack them
            d.shift(RIGHT * (i - 1) * 0.85)
            diffs.add(d)
        cap = self.ja_text("差の絶対値", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d) for d in diffs], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("半分が距離", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(diffs, color=YELLOW), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\|P-Q\|_{\mathrm{TV}}=\tfrac12\sum|p-q|").scale(0.85)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
