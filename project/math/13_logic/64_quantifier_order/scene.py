from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class QuantifierOrder(JapaneseScene):
    """#64 量化子の順番（約90秒）"""

    def construct(self):
        self.show_heading("量化子の順")
        self.show_forall_exists()
        self.show_exists_forall()
        self.show_formula()
        self.hold(1.2)

    def show_forall_exists(self):
        xs = VGroup(*[Dot(LEFT * 3.6 + UP * (0.9 - i * 0.75), radius=0.09, color=BLUE) for i in range(3)])
        ys = VGroup(*[Dot(LEFT * 1.3 + UP * (0.9 - i * 0.75), radius=0.09, color=GREEN) for i in range(3)])
        arrows = VGroup(
            *[Arrow(xs[i].get_center(), ys[i].get_center(), buff=0.15, stroke_width=3) for i in range(3)]
        )
        cap = MathTex(r"\forall x\,\exists y", font_size=32)
        cap.next_to(VGroup(xs, ys), UP, buff=0.25)
        lab = self.ja_text("それぞれ相手がいる", font_size=22).next_to(cap, DOWN, buff=0.12)
        self.play(FadeIn(xs), FadeIn(ys), run_time=0.45)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.12), FadeIn(cap), FadeIn(lab), run_time=0.75)
        self.hold(0.7)
        self.left = VGroup(xs, ys, arrows, cap, lab)

    def show_exists_forall(self):
        xs = VGroup(*[Dot(RIGHT * 1.2 + UP * (0.9 - i * 0.75), radius=0.09, color=BLUE) for i in range(3)])
        y = Dot(RIGHT * 3.6 + UP * 0.15, radius=0.11, color=YELLOW)
        arrows = VGroup(*[Arrow(xs[i].get_center(), y.get_center(), buff=0.15, stroke_width=3, color=YELLOW) for i in range(3)])
        cap = MathTex(r"\exists y\,\forall x", font_size=32)
        cap.next_to(VGroup(xs, y), UP, buff=0.25)
        lab = self.ja_text("一人が全員の相手", font_size=22).next_to(cap, DOWN, buff=0.12)
        self.play(FadeIn(xs), FadeIn(y), run_time=0.45)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.12), FadeIn(cap), FadeIn(lab), run_time=0.75)
        self.hold(0.8)

    def show_formula(self):
        note = self.ja_text("順番を変えると意味が変わる", font_size=28)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note), run_time=0.6)
        self.play(Indicate(note, color=YELLOW), run_time=0.7)
        self.hold(1.2)
