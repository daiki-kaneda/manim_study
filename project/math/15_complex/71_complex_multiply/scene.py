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


class ComplexMultiply(JapaneseScene):
    """#71 複素数の積＝回転と拡大（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.5 + DOWN * 0.1
        self.show_heading("複素数の積")
        self.draw_z()
        self.multiply()
        self.show_formula()
        self.hold(1.2)

    def draw_z(self):
        axes_x = Line(self.origin + LEFT * 0.4, self.origin + RIGHT * 4.0, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 1.8, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        self.play(Create(axes_x), Create(axes_y), run_time=0.5)
        z = np.array(polar(1.7, 25 * DEGREES))
        self.arrow_z = Arrow(self.origin, self.origin + z, buff=0, color=BLUE, stroke_width=4)
        lab = MathTex("z", color=BLUE, font_size=32).next_to(self.arrow_z.get_end(), DOWN, buff=0.1)
        self.play(GrowArrow(self.arrow_z), FadeIn(lab), run_time=0.6)
        self.hold(0.4)
        self.z = z

    def multiply(self):
        # w = 1.35 cis 50°
        w = np.array(polar(1.35, 50 * DEGREES))
        aw = Arrow(self.origin, self.origin + w, buff=0, color=GREEN, stroke_width=3)
        lw = MathTex("w", color=GREEN, font_size=30).next_to(aw.get_end(), UR, buff=0.08)
        self.play(GrowArrow(aw), FadeIn(lw), run_time=0.55)
        self.hold(0.4)
        prod = np.array(polar(1.7 * 1.35, 75 * DEGREES))
        ap = Arrow(self.origin, self.origin + prod, buff=0, color=YELLOW, stroke_width=5)
        lp = MathTex(r"zw", color=YELLOW, font_size=32).next_to(ap.get_end(), UR, buff=0.1)
        self.play(GrowArrow(ap), FadeIn(lp), run_time=0.7)
        note = self.ja_text("偏角は足し、長さは掛け", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"|zw|=|z||w|,\quad \arg(zw)=\arg z+\arg w").scale(0.78)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
