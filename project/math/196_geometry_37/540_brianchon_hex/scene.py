from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class BrianchonHexagon(PacedScene):
    """#540 ブリアンション六角形：外接六角形の対角線共点（約45秒）"""

    def construct(self):
        self.show_heading("ブリアンション六角形")
        self.draw_hex()
        self.concurrence()
        self.show_formula()
        self.read(1.4)

    def draw_hex(self):
        circ = Circle(radius=1.7, color=BLUE, stroke_width=3).shift(UP * 0.15)
        pts = [circ.point_from_proportion(t) for t in [0.0, 0.15, 0.35, 0.5, 0.68, 0.85]]
        # tangential hex approx as polygon outside
        hexagon = Polygon(*[p * 1.35 for p in pts], color=ORANGE, stroke_width=3)
        self.play(Create(circ), Create(hexagon), run_time=1.4)
        note = self.ja_text("外接六角形", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.pts = [p * 1.35 for p in pts]

    def concurrence(self):
        lines = VGroup(
            Line(self.pts[0], self.pts[3], color=YELLOW, stroke_width=3),
            Line(self.pts[1], self.pts[4], color=YELLOW, stroke_width=3),
            Line(self.pts[2], self.pts[5], color=YELLOW, stroke_width=3),
        )
        p = Dot(UP * 0.15, color=RED, radius=0.1)
        cap = self.ja_text("主対角線が共点", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.15), FadeIn(p), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("パスカルの双対", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("外接六角形の対角線は一点で交わる", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
