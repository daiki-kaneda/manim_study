from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class BFGS(PacedScene):
    """#609 BFGS：準ニュートン更新でヘッセ近似（約45秒）"""

    def construct(self):
        self.show_heading("BFGS")
        self.draw_update()
        self.rank2()
        self.show_formula()
        self.read(1.4)

    def draw_update(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.6, height=1.2, corner_radius=0.1, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT * 2.5 + UP * 0.3), (ORANGE, ORIGIN + UP * 0.3), (TEAL, RIGHT * 2.5 + UP * 0.3)]
        ])
        labs = VGroup(
            MathTex(r"B_k", font_size=32).move_to(boxes[0]),
            MathTex(r"s,y", font_size=28).move_to(boxes[1]),
            MathTex(r"B_{k+1}", font_size=30).move_to(boxes[2]),
        )
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), buff=0.08, stroke_width=3),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), buff=0.08, stroke_width=3),
        )
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), GrowArrow(arrows[0]), GrowArrow(arrows[1]), run_time=1.5)
        note = self.ja_text("ヘッセ近似", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def rank2(self):
        cap = self.ja_text("ランク2更新", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("正定値を保つ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"B_{+}=B-\frac{Bss^\top B}{s^\top Bs}+\frac{yy^\top}{y^\top s}").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
