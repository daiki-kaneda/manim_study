from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GeometricDist(PacedScene):
    """#134 幾何分布（約45秒）"""

    def construct(self):
        self.show_heading("幾何分布")
        self.draw_bars()
        self.show_formula()
        self.read(1.4)

    def draw_bars(self):
        p = 0.35
        heights = [4.2 * p * ((1 - p) ** (k - 1)) for k in range(1, 8)]
        origin = LEFT * 4.8 + DOWN * 1.55
        w, gap = 0.62, 0.95
        bars = VGroup()
        labels = VGroup()
        for i, h in enumerate(heights):
            bar = Rectangle(width=w, height=max(h, 0.12), color=BLUE, fill_opacity=0.85, stroke_width=1)
            bar.move_to(origin + RIGHT * (i * gap + w / 2) + UP * (max(h, 0.12) / 2))
            lab = MathTex(str(i + 1), font_size=24).next_to(bar, DOWN, buff=0.12)
            bars.add(bar)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.25) for b in bars], lag_ratio=0.14), run_time=2.8)
        self.play(FadeIn(labels), run_time=0.5)
        note = self.ja_text("初めての成功", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.45)
        self.read(0.55)

    def show_formula(self):
        formula = MathTex(r"P(X=k)=p(1-p)^{k-1}").scale(0.95)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
