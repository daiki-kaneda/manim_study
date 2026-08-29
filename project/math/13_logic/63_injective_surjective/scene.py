from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class InjectiveSurjective(JapaneseScene):
    """#63 単射と全射（約90秒）"""

    def construct(self):
        self.show_heading("単射と全射")
        self.show_injective()
        self.show_surjective()
        self.show_formula()
        self.hold(1.2)

    def _dots(self, n, origin, color):
        g = VGroup()
        for i in range(n):
            g.add(Dot(origin + DOWN * i * 0.7, radius=0.1, color=color))
        return g

    def show_injective(self):
        left = self._dots(3, LEFT * 4.2 + UP * 1.1, BLUE)
        right = self._dots(3, LEFT * 1.6 + UP * 1.1, GREEN)
        arrows = VGroup(
            Arrow(left[0].get_center(), right[0].get_center(), buff=0.16, stroke_width=3),
            Arrow(left[1].get_center(), right[1].get_center(), buff=0.16, stroke_width=3),
            Arrow(left[2].get_center(), right[2].get_center(), buff=0.16, stroke_width=3),
        )
        cap = self.ja_text("単射：ぶつからない", font_size=24)
        cap.next_to(VGroup(left, right), UP, buff=0.25)
        self.play(FadeIn(left), FadeIn(right), run_time=0.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=0.7)
        self.play(FadeIn(cap), run_time=0.3)
        self.hold(0.7)
        self.keep = VGroup(left, right, arrows, cap)

    def show_surjective(self):
        left = self._dots(3, RIGHT * 1.3 + UP * 1.1, BLUE)
        right = self._dots(3, RIGHT * 3.9 + UP * 1.1, GREEN)
        arrows = VGroup(
            Arrow(left[0].get_center(), right[0].get_center(), buff=0.16, stroke_width=3),
            Arrow(left[1].get_center(), right[1].get_center(), buff=0.16, stroke_width=3),
            Arrow(left[2].get_center(), right[2].get_center(), buff=0.16, stroke_width=3),
        )
        cap = self.ja_text("全射：すきまなし", font_size=24)
        cap.next_to(VGroup(left, right), UP, buff=0.25)
        self.play(FadeIn(left), FadeIn(right), run_time=0.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=0.7)
        self.play(FadeIn(cap), run_time=0.3)
        self.hold(0.7)

    def show_formula(self):
        formula = self.ja_text("両方満たせば一対一対応", font_size=28)
        formula.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(formula), run_time=0.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
