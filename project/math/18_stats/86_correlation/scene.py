from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Correlation(JapaneseScene):
    """#86 相関（約90秒）"""

    def construct(self):
        self.show_heading("相関")
        self.draw_scatters()
        self.show_formula()
        self.hold(1.2)

    def _frame(self, origin):
        x = Line(origin, origin + RIGHT * 3.3, color=GREY, stroke_width=2)
        y = Line(origin, origin + UP * 3.0, color=GREY, stroke_width=2)
        return VGroup(x, y)

    def _pts(self, origin, pairs, color):
        return VGroup(*[
            Dot(origin + RIGHT * p[0] + UP * p[1], radius=0.07, color=color) for p in pairs
        ])

    def draw_scatters(self):
        left = LEFT * 5.6 + DOWN * 1.55
        right = RIGHT * 0.15 + DOWN * 1.55
        pos_pairs = [(0.4, 0.5), (0.8, 0.85), (1.2, 1.15), (1.6, 1.7), (2.0, 1.9), (2.4, 2.35), (2.8, 2.55)]
        neg_pairs = [(0.4, 2.55), (0.8, 2.2), (1.2, 1.85), (1.6, 1.45), (2.0, 1.1), (2.4, 0.7), (2.8, 0.45)]
        fl, fr = self._frame(left), self._frame(right)
        pl = self._pts(left, pos_pairs, BLUE)
        pr = self._pts(right, neg_pairs, ORANGE)
        self.play(Create(fl), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(d) for d in pl], lag_ratio=0.08), run_time=0.8)
        lp = self.ja_text("正の相関", font_size=24).next_to(fl, UP, buff=0.25)
        self.play(FadeIn(lp), run_time=0.3)
        self.hold(0.4)
        self.play(Create(fr), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(d) for d in pr], lag_ratio=0.08), run_time=0.8)
        ln = self.ja_text("負の相関", font_size=24).next_to(fr, UP, buff=0.25)
        self.play(FadeIn(ln), run_time=0.3)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"\mathrm{Corr}(X,Y)=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}").scale(0.9)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
