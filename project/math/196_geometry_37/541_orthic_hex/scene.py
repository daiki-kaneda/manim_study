from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class OrthicHexagon(PacedScene):
    """#541 垂心六角形：垂線と辺が作る六角形（約45秒）"""

    def construct(self):
        self.show_heading("垂心六角形")
        self.draw_triangle()
        self.hex()
        self.show_formula()
        self.read(1.4)

    def draw_triangle(self):
        self.A = UP * 2.1
        self.B = LEFT * 2.6 + DOWN * 1.4
        self.C = RIGHT * 2.8 + DOWN * 1.35
        self.tri = Polygon(self.A, self.B, self.C, color=BLUE, stroke_width=3)
        self.play(Create(self.tri), run_time=1.2)
        note = self.ja_text("鋭角三角形", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def hex(self):
        pts = [
            self.A * 0.55 + self.B * 0.45,
            self.A * 0.55 + self.C * 0.45,
            self.B * 0.35 + self.C * 0.65,
            self.B * 0.55 + self.C * 0.45,
            self.A * 0.25 + self.B * 0.75,
            self.A * 0.25 + self.C * 0.75,
        ]
        hexagon = Polygon(*pts, color=ORANGE, stroke_width=3)
        cap = self.ja_text("垂線が作る六角形", font_size=24).move_to(self.note)
        self.play(Create(hexagon), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("垂心が中心的", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = self.ja_text("垂心六角形：垂足と垂線の交点", font_size=26)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
