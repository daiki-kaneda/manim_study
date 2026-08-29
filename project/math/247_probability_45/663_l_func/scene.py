from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LFunction(PacedScene):
    """#663 L関数：リプリーKの安定化変換（約45秒）"""

    def construct(self):
        self.show_heading("L関数")
        self.draw()
        self.stab()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[0, 3, 1], y_range=[0, 3, 1], x_length=5.0, y_length=2.5,
                    tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.1)
        diag = axes.plot(lambda r: r, x_range=[0.05, 2.9], color=GREY, stroke_width=2)
        L = axes.plot(lambda r: r + 0.25 * (1.5 ** (-r)) * (r ** 0.5), x_range=[0.05, 2.9], color=BLUE, stroke_width=3)
        self.play(Create(axes), Create(diag), Create(L), run_time=1.4)
        note = self.ja_text("L(r)-r を見る", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def stab(self):
        cap = self.ja_text("分散を安定化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("CSR なら L=r", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"L(r)=\sqrt{K(r)/\pi}").scale(0.85)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
