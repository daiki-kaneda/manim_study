from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class MarkedPointProcess(PacedScene):
    """#568 マーク付き点過程：点に属性を載せる（約45秒）"""

    def construct(self):
        self.show_heading("マーク付き点過程")
        self.draw_marks()
        self.space()
        self.show_formula()
        self.read(1.4)

    def draw_marks(self):
        line = NumberLine(x_range=[0, 6, 1], length=7, include_numbers=False).shift(UP * 0.3)
        xs = [0.8, 1.7, 2.9, 4.1, 5.3]
        marks = ["a", "b", "a", "c", "b"]
        dots = VGroup(*[Dot(line.n2p(x), color=YELLOW, radius=0.1) for x in xs])
        labs = VGroup(*[MathTex(m, font_size=26).next_to(dots[i], UP, buff=0.15) for i, m in enumerate(marks)])
        self.play(Create(line), FadeIn(dots), FadeIn(labs), run_time=1.4)
        note = self.ja_text("時刻＋印", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def space(self):
        cap = self.ja_text("印空間付き", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("種別に分解可", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\{(T_i,M_i)\}\subset\mathbb{R}_+\times\mathbb{M}").scale(0.82)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
