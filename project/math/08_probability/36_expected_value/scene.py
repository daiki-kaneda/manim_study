from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ExpectedValue(JapaneseScene):
    """#36 期待値は重心（約90秒）"""

    def construct(self):
        self.show_heading("期待値")
        self.draw_die()
        self.mark_mean()
        self.show_formula()
        self.hold(1.2)

    def draw_die(self):
        self.origin = LEFT * 4.0 + DOWN * 1.55
        self.w = 0.85
        self.gap = 1.15
        bars = VGroup()
        labels = VGroup()
        h = 2.15
        for i, face in enumerate(range(1, 7)):
            bar = Rectangle(width=self.w, height=h, color=BLUE, fill_opacity=0.8, stroke_width=1)
            x = self.origin + RIGHT * (i * self.gap + self.w / 2) + UP * (h / 2)
            bar.move_to(x)
            lab = MathTex(str(face), font_size=28).next_to(bar, DOWN, buff=0.12)
            bars.add(bar)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.15) for b in bars], lag_ratio=0.12), run_time=1.3)
        self.play(FadeIn(labels), run_time=0.4)
        note = self.ja_text("サイコロ（同じ高さ）", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.6)
        self.bars, self.origin_y = bars, self.origin[1]
        self.note = note

    def mark_mean(self):
        # 3.5 は 1 と 6 の真ん中。バー i の中心 x = origin.x + i*gap + w/2
        # 顔 k=1..6 の位置の平均は k=3.5 → index 2.5
        x_mean = self.origin[0] + 2.5 * self.gap + self.w / 2
        fulcrum = Triangle(color=YELLOW, fill_opacity=1).scale(0.18)
        fulcrum.rotate(PI)
        fulcrum.move_to([x_mean, self.origin_y - 0.55, 0])
        line = DashedLine(
            [x_mean, self.origin_y - 0.35, 0],
            [x_mean, self.origin_y + 2.4, 0],
            color=YELLOW,
            stroke_width=3,
        )
        mu = MathTex(r"3.5", color=YELLOW, font_size=34).next_to(line, UP, buff=0.1)
        self.play(Create(line), FadeIn(fulcrum), FadeIn(mu), run_time=0.8)
        cap = self.ja_text("重心の位置", font_size=26).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.8)

    def show_formula(self):
        formula = MathTex(r"E[X]=\sum x\,P(x)").scale(1.1)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
