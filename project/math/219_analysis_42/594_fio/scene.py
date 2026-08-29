from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class FourierIntegralOp(PacedScene):
    """#594 フーリエ積分作用素：位相で振動する積分核（約45秒）"""

    def construct(self):
        self.show_heading("フーリエ積分作用素")
        self.draw_phase()
        self.canonical()
        self.show_formula()
        self.read(1.4)

    def draw_phase(self):
        box = RoundedRectangle(width=3.4, height=1.5, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 1.5 + UP * 0.2)
        self.play(Create(box), FadeIn(MathTex(r"e^{i\phi(x,\xi)}", font_size=34).move_to(box)), run_time=1.3)
        note = self.ja_text("位相関数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def canonical(self):
        cap = self.ja_text("正準関係を運ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("波動の伝播", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Af(x)=\int e^{i\phi(x,\xi)}a(x,\xi)\hat f(\xi)\,d\xi").scale(0.65)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
