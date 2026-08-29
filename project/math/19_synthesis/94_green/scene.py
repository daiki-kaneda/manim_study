from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class GreenTheorem(JapaneseScene):
    """#94 グリーンの定理（約90秒）"""

    def construct(self):
        self.show_heading("グリーンの定理")
        self.draw_region()
        self.circulate()
        self.show_formula()
        self.hold(1.2)

    def draw_region(self):
        self.center = LEFT * 1.8 + DOWN * 0.1
        self.region = RoundedRectangle(
            width=4.4, height=2.8, corner_radius=0.35, color=BLUE, fill_opacity=0.25, stroke_width=3
        ).move_to(self.center)
        self.play(FadeIn(self.region), run_time=0.7)
        note = self.ja_text("領域 D", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.4)
        self.note = note

    def circulate(self):
        arrows = VGroup()
        w, h = 2.0, 1.2
        c = self.center
        specs = [
            (c + LEFT * w + DOWN * h, c + RIGHT * w + DOWN * h),
            (c + RIGHT * w + DOWN * h, c + RIGHT * w + UP * h),
            (c + RIGHT * w + UP * h, c + LEFT * w + UP * h),
            (c + LEFT * w + UP * h, c + LEFT * w + DOWN * h),
        ]
        for a, b in specs:
            arrows.add(Arrow(a, b, buff=0.05, color=YELLOW, stroke_width=4, max_tip_length_to_length_ratio=0.12))
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.18), run_time=1.2)
        curl = MathTex(r"\partial_x Q-\partial_y P", font_size=28, color=ORANGE)
        curl.move_to(self.center)
        self.play(FadeIn(curl), run_time=0.45)
        cap = self.ja_text("境界＝回転", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\oint P\,dx+Q\,dy=\iint(Q_x-P_y)\,dA").scale(0.85)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.2)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
