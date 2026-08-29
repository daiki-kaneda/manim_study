from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CampbellMecke(PacedScene):
    """#699 キャンベル・メッケ：マーク付きへの拡張（約45秒）"""

    def construct(self):
        self.show_heading("キャンベル・メッケ")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        line = NumberLine(x_range=[0, 5, 1], length=6.0, include_numbers=False).shift(UP*0.5)
        dots = VGroup(*[Dot(line.n2p(x), color=YELLOW, radius=0.09) for x in [0.8, 2.0, 3.2, 4.3]])
        self.play(Create(line), FadeIn(dots), run_time=1.2)

        note = self.ja_text("点とマーク", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("期待値を積分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("パームと結ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathbb{E}\sum f(x,\Phi)=\int\mathbb{E}^0 f(x,\Phi)\,dx").scale(0.58)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
