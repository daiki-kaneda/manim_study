from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class StringProcess(PacedScene):
    """#592 ストリング過程：区間のランダムな並び（約45秒）"""

    def construct(self):
        self.show_heading("ストリング過程")
        self.draw_intervals()
        self.overlap()
        self.show_formula()
        self.read(1.4)

    def draw_intervals(self):
        segs = VGroup(*[
            Line(LEFT * 3 + RIGHT * i * 0.3 + UP * (0.8 - j * 0.7),
                 LEFT * 1.5 + RIGHT * i * 0.3 + UP * (0.8 - j * 0.7),
                 color=c, stroke_width=8)
            for j, (i, c) in enumerate([(0, BLUE), (2, ORANGE), (1, TEAL), (3, YELLOW)])
        ])
        # simpler horizontal segments on a line
        line = NumberLine(x_range=[0, 6, 1], length=7, include_numbers=False).shift(UP * 0.2)
        bars = VGroup(
            Line(line.n2p(0.5), line.n2p(2.0), color=BLUE, stroke_width=10).shift(UP * 0.35),
            Line(line.n2p(1.5), line.n2p(3.5), color=ORANGE, stroke_width=10).shift(UP * 0.55),
            Line(line.n2p(3.0), line.n2p(5.2), color=TEAL, stroke_width=10).shift(UP * 0.35),
        )
        self.play(Create(line), LaggedStart(*[Create(b) for b in bars], lag_ratio=0.15), run_time=1.5)
        note = self.ja_text("区間の集まり", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def overlap(self):
        cap = self.ja_text("重なりを許す模型", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("線分過程の一種", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("ストリング：ランダムな区間の点過程", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
