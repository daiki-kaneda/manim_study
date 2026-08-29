from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import math
from manim import *
from manim_math import PacedScene


class Poisson(PacedScene):
    """#135 ポアソン分布（約45秒）"""

    def construct(self):
        self.show_heading("ポアソン")
        self.draw_bars()
        self.show_formula()
        self.read(1.4)

    def draw_bars(self):
        lam = 3.0
        ks = list(range(0, 9))
        raw = [math.exp(-lam) * lam ** k / math.factorial(k) for k in ks]
        heights = [h / max(raw) * 3.0 for h in raw]
        origin = LEFT * 5.0 + DOWN * 1.55
        w, gap = 0.55, 0.85
        bars = VGroup()
        labels = VGroup()
        for i, h in enumerate(heights):
            color = YELLOW if ks[i] == 3 else BLUE
            bar = Rectangle(width=w, height=max(h, 0.1), color=color, fill_opacity=0.85, stroke_width=1)
            bar.move_to(origin + RIGHT * (i * gap + w / 2) + UP * (max(h, 0.1) / 2))
            lab = MathTex(str(ks[i]), font_size=22).next_to(bar, DOWN, buff=0.1)
            bars.add(bar)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(b, shift=UP * 0.2) for b in bars], lag_ratio=0.12), run_time=2.6)
        self.play(FadeIn(labels), run_time=0.45)
        note = self.ja_text("平均の近く", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), Indicate(bars[3], color=WHITE), run_time=0.9)
        self.read(0.5)

    def show_formula(self):
        formula = MathTex(r"P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}").scale(0.92)
        formula.to_edge(DOWN, buff=0.32)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.8)
