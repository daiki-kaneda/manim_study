from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MarkCorrelation(PacedScene):
    """#664 マーク相関：距離に応じたマークの共変動（約45秒）"""

    def construct(self):
        self.show_heading("マーク相関")
        self.draw()
        self.corr()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        import random
        random.seed(5)
        dots = VGroup()
        for _ in range(16):
            x, y = random.uniform(-3, 3), random.uniform(-1.2, 1.2)
            r = random.uniform(0.06, 0.18)
            dots.add(Dot([x, y, 0], radius=r, color=interpolate_color(BLUE, ORANGE, (r - 0.06) / 0.12)))
        self.play(FadeIn(dots), run_time=1.2)
        note = self.ja_text("点にマーク", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def corr(self):
        cap = self.ja_text("距離 r の相関", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("k_mm(r)", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"k_{mm}(r)=\frac{\mathbb{E}^0[m(0)m(r)]}{\mu^2}").scale(0.7)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
