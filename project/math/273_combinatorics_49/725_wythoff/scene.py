from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class WythoffArray(PacedScene):
    """#725 ウィソフ配列：ビートティ数列の三角形配列（約45秒）"""

    def construct(self):
        self.show_heading("ウィソフ配列")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        grid = VGroup(*[
            MathTex(str((i + 1) * (j + 2)), font_size=22).shift(LEFT * 2.2 + RIGHT * j * 0.85 + UP * (1.0 - i * 0.55))
            for i in range(4) for j in range(5)
        ])
        self.play(LaggedStart(*[FadeIn(g) for g in grid], lag_ratio=0.02), run_time=1.4)

        note = self.ja_text("黄金比で分割", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("低・高ビートティ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("ワイソフゲーム", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"a_n=\lfloor n\phi\rfloor,\ b_n=\lfloor n\phi^2\rfloor").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
