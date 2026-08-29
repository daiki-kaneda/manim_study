from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Sophia(PacedScene):
    """#741 Sophia：クリッピング付き2次モーメント最適化（約45秒）"""

    def construct(self):
        self.show_heading("Sophia")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 4, 1], y_range=[0, 2, 1], x_length=5.0, y_length=2.3, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.15)
        clip = DashedLine(axes.c2p(0, 1.2), axes.c2p(4, 1.2), color=GREY)
        path = axes.plot(lambda t: min(1.2, 0.3 + 0.5 * t), x_range=[0.1, 3.8], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(clip), Create(path), run_time=1.4)
        note = self.ja_text("h をクリップ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("凸でも非凸でも", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("理論付き更新", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"h_t=\max\{\beta h_{t-1}+(1-\beta)g_t^2,\gamma\}").scale(0.58)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
