from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AdaBound(PacedScene):
    """#718 AdaBound：Adamの学習率に動的上下限（約45秒）"""

    def construct(self):
        self.show_heading("AdaBound")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        lo = DashedLine(axes.c2p(0, 0.4), axes.c2p(4, 0.4), color=GREY)
        hi = DashedLine(axes.c2p(0, 1.6), axes.c2p(4, 1.6), color=GREY)
        mid = axes.plot(lambda t: 1.0 + 0.4 * (2.0 ** (-t)), x_range=[0.1, 3.8], color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(lo), Create(hi), Create(mid), run_time=1.4)

        note = self.ja_text("上下で挟む", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("SGDへ収束", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("汎化改善", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\eta_l(t)\le\eta/\sqrt{V_t}\le\eta_u(t)").scale(0.68)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
