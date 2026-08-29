from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class FrankWolfe(PacedScene):
    """#489 フランク・ウォルフェ：線形オラクルで凸集合を進む（約45秒）"""

    def construct(self):
        self.show_heading("フランク・ウォルフェ")
        self.draw_set()
        self.linear_oracle()
        self.show_formula()
        self.read(1.4)

    def draw_set(self):
        poly = Polygon(
            LEFT * 2.5 + DOWN * 1.2,
            LEFT * 0.5 + UP * 1.6,
            RIGHT * 2.2 + UP * 0.8,
            RIGHT * 2.0 + DOWN * 1.4,
            color=BLUE, stroke_width=3, fill_opacity=0.15,
        )
        x = Dot(ORIGIN + LEFT * 0.3 + DOWN * 0.2, color=YELLOW, radius=0.1)
        self.play(Create(poly), FadeIn(x), run_time=1.3)
        note = self.ja_text("凸集合上", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.x = x

    def linear_oracle(self):
        s = Dot(RIGHT * 2.0 + UP * 0.8, color=ORANGE, radius=0.1)
        line = DashedLine(self.x.get_center(), s.get_center(), color=ORANGE, stroke_width=3)
        cap = self.ja_text("線形最小化", font_size=24).move_to(self.note)
        self.play(FadeIn(s), Create(line), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        mid = Dot(self.x.get_center() * 0.6 + s.get_center() * 0.4, color=RED, radius=0.1)
        cap2 = self.ja_text("凸結合で更新", font_size=24).move_to(self.note)
        self.play(FadeIn(mid), Transform(self.note, cap2), run_time=0.9)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"s_k=\arg\min_{s\in C}\langle\nabla f(x_k),s\rangle").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
