from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import polar


class ExpMap(JapaneseScene):
    """#72 e^z は帯を扇形へ（約90秒）"""

    def construct(self):
        self.show_heading("e の複素")
        self.draw_strip()
        self.map_it()
        self.show_formula()
        self.hold(1.2)

    def draw_strip(self):
        # 左：縦の帯（実部が定数に近い矩形）
        rect = Rectangle(width=1.1, height=2.6, color=BLUE, fill_opacity=0.45, stroke_width=2)
        rect.shift(LEFT * 3.4 + DOWN * 0.1)
        lab = MathTex(r"z=x+iy", font_size=30).next_to(rect, UP, buff=0.2)
        self.play(FadeIn(rect), FadeIn(lab), run_time=0.7)
        note = self.ja_text("縦の帯", font_size=24)
        note.next_to(rect, DOWN, buff=0.25)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.5)
        self.rect, self.note = rect, note

    def map_it(self):
        # 右：原点中心の扇（偏角の区間、半径 e^x）
        origin = RIGHT * 1.8 + DOWN * 0.1
        r = 2.0
        sector = AnnularSector(
            inner_radius=0,
            outer_radius=r,
            angle=80 * DEGREES,
            start_angle=20 * DEGREES,
            color=YELLOW,
            fill_opacity=0.5,
            stroke_width=2,
            arc_center=origin,
        )
        arrow = Arrow(self.rect.get_right(), sector.get_left() + LEFT * 0.15, buff=0.1, color=WHITE, stroke_width=3)
        self.play(GrowArrow(arrow), run_time=0.45)
        self.play(FadeIn(sector), run_time=0.7)
        cap = self.ja_text("扇形へ", font_size=24)
        cap.next_to(sector, DOWN, buff=0.2)
        self.play(FadeIn(cap), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"e^{x+iy}=e^x(\cos y+i\sin y)").scale(0.95)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
