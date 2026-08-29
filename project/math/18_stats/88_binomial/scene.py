from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Binomial(JapaneseScene):
    """#88 二項分布（約90秒）"""

    def construct(self):
        self.show_heading("二項分布")
        self.draw_bars()
        self.show_formula()
        self.hold(1.2)

    def draw_bars(self):
        # C(6,k) / 64, scaled for height
        coeffs = [1, 6, 15, 20, 15, 6, 1]
        heights = [c / 20 * 3.1 for c in coeffs]
        origin = LEFT * 4.6 + DOWN * 1.55
        w, gap = 0.7, 1.05
        bars = VGroup()
        labels = VGroup()
        for i, h in enumerate(heights):
            bar = Rectangle(width=w, height=max(h, 0.12), color=BLUE, fill_opacity=0.85, stroke_width=1)
            bar.move_to(origin + RIGHT * (i * gap + w / 2) + UP * (max(h, 0.12) / 2))
            lab = MathTex(str(i), font_size=24).next_to(bar, DOWN, buff=0.12)
            bars.add(bar)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in bars], lag_ratio=0.1), run_time=1.2)
        self.play(FadeIn(labels), run_time=0.35)
        note = self.ja_text("表が k 回", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}").scale(0.9)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.1)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
