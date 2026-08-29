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


class ModularClock(JapaneseScene):
    """#42 合同式は時計（約90秒）"""

    def construct(self):
        self.R = 2.15
        self.origin = LEFT * 2.3 + DOWN * 0.05
        self.show_heading("合同式")
        self.draw_clock()
        self.add_around()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, hour):
        # 12 が上。hour 0..11
        ang = PI / 2 - hour * TAU / 12
        return self.origin + np.array(polar(self.R, ang))

    def draw_clock(self):
        circle = Circle(radius=self.R, color=WHITE, stroke_width=2).move_to(self.origin)
        ticks = VGroup()
        labs = VGroup()
        for h in range(12):
            p = self._pt(h)
            ticks.add(Dot(p, radius=0.04, color=GREY))
            lab = MathTex(str(h if h != 0 else 12), font_size=22)
            lab.move_to(self.origin + np.array(polar(self.R + 0.32, PI / 2 - h * TAU / 12)))
            labs.add(lab)
        self.play(Create(circle), FadeIn(ticks), FadeIn(labs), run_time=0.9)
        self.hold(0.4)

    def add_around(self):
        # 7 + 8 = 15 ≡ 3 (mod 12)
        hand7 = Line(self.origin, self._pt(7), color=BLUE, stroke_width=4)
        self.play(Create(hand7), run_time=0.5)
        n7 = MathTex("7", color=BLUE, font_size=34).to_edge(RIGHT, buff=0.55).shift(UP * 1.6)
        self.play(FadeIn(n7), run_time=0.3)
        self.hold(0.4)
        # 8 時間進む: 7→8→...→3 の弧
        start = PI / 2 - 7 * TAU / 12
        arc = Arc(radius=0.7, start_angle=start, angle=-8 * TAU / 12, color=ORANGE, arc_center=self.origin)
        self.play(Create(arc), run_time=0.9)
        hand3 = Line(self.origin, self._pt(3), color=YELLOW, stroke_width=5)
        self.play(Transform(hand7, hand3), run_time=0.7)
        n15 = MathTex(r"7+8=15", font_size=32).next_to(n7, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(FadeIn(n15), run_time=0.4)
        self.hold(0.7)
        self.n15 = n15

    def show_formula(self):
        formula = MathTex(r"15\equiv 3\pmod{12}").scale(1.15)
        formula.to_edge(DOWN, buff=0.38)
        note = self.ja_text("12 で割った余り", font_size=24)
        note.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(note), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
