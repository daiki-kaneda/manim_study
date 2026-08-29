from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Pseudodifferential(PacedScene):
    """#583 擬微分作用素：記号で定義する作用素（約45秒）"""

    def construct(self):
        self.show_heading("擬微分作用素")
        self.draw_symbol()
        self.quantize()
        self.show_formula()
        self.read(1.4)

    def draw_symbol(self):
        box = RoundedRectangle(width=3.2, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 1.8 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"a(x,\xi)", font_size=34).move_to(box)), run_time=1.3)
        note = self.ja_text("記号", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def quantize(self):
        arrow = Arrow(LEFT * 0.1, RIGHT * 2.0, buff=0.05, color=ORANGE, stroke_width=4).shift(UP * 0.2)
        cap = self.ja_text("量子化", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("微分の一般化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Op(a)f=(2\pi)^{-n}\int e^{ix\cdot\xi}a(x,\xi)\hat f(\xi)\,d\xi").scale(0.55)
        formula.to_edge(DOWN, buff=0.18)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
