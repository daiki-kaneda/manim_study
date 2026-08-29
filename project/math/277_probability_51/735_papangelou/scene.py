from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class PapangelouIntensity(PacedScene):
    """#735 パパンゲルー強度：条件付きで点を置く強さ（約45秒）"""

    def construct(self):
        self.show_heading("パパンゲルー強度")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        import random
        random.seed(4)
        pts = VGroup(*[Dot([random.uniform(-2.8, 2.8), random.uniform(-1.1, 1.1), 0], radius=0.07, color=BLUE) for _ in range(14)])
        new = Dot(ORIGIN + UP * 0.3, radius=0.12, color=YELLOW)
        self.play(FadeIn(pts), FadeIn(new), run_time=1.3)

        note = self.ja_text("条件付き強度", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("既存配置に依存", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ギブス過程へ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\lambda(x|\Phi)=\lim\frac{P(N(dx)=1|\Phi)}{dx}").scale(0.58)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
