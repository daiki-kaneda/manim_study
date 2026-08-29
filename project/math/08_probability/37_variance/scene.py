from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Variance(JapaneseScene):
    """#37 分散はばらつき（約90秒）"""

    def construct(self):
        self.show_heading("分散")
        self.draw_two_spreads()
        self.show_formula()
        self.hold(1.2)

    def _bars(self, heights, color, origin):
        group = VGroup()
        w, gap = 0.55, 0.72
        for i, h in enumerate(heights):
            bar = Rectangle(width=w, height=h, color=color, fill_opacity=0.85, stroke_width=1)
            bar.move_to(origin + RIGHT * (i * gap + w / 2) + UP * (h / 2))
            group.add(bar)
        return group

    def draw_two_spreads(self):
        left_o = LEFT * 5.5 + DOWN * 1.3
        right_o = RIGHT * 0.15 + DOWN * 1.3
        # 同じ平均、左は中央に集中、右は端に厚い
        tight = self._bars([0.35, 0.7, 2.3, 2.3, 0.7, 0.35], BLUE, left_o)
        wide = self._bars([2.1, 0.55, 0.35, 0.35, 0.55, 2.1], ORANGE, right_o)
        self.play(FadeIn(tight), run_time=0.7)
        tlab = self.ja_text("ばらつき小", font_size=26).next_to(tight, UP, buff=0.35)
        self.play(FadeIn(tlab), run_time=0.35)
        self.hold(0.55)
        self.play(FadeIn(wide), run_time=0.7)
        wlab = self.ja_text("ばらつき大", font_size=26).next_to(wide, UP, buff=0.35)
        self.play(FadeIn(wlab), run_time=0.35)
        same = self.ja_text("平均はどちらも同じ", font_size=24)
        same.to_edge(DOWN, buff=1.15)
        self.play(FadeIn(same), run_time=0.4)
        self.hold(0.8)
        self.same = same

    def show_formula(self):
        formula = MathTex(r"V(X)=E[(X-\mu)^2]").scale(1.1)
        formula.to_edge(DOWN, buff=0.32)
        self.play(FadeOut(self.same), run_time=0.25)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=ORANGE), run_time=0.7)
        self.hold(1.2)
