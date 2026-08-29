from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class DiniTheorem(PacedScene):
    """#319 ディニ：単調な点収束は一様（コンパクト上）（約45秒）"""

    def construct(self):
        self.show_heading("ディニの定理")
        self.draw_mono()
        self.uniform()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_mono(self):
        self.axes = Axes(x_range=[0, 4, 1], y_range=[0, 2.2, 1], x_length=6.2, y_length=2.7,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.5 + UP * 0.25)
        import math
        curves = []
        for n, col in [(1, GREY), (2, TEAL), (4, BLUE)]:
            curves.append(self.axes.plot(lambda x, n=n: (1 - math.exp(-n * x * 0.4)) * 1.5, x_range=[0.1, 3.8], color=col, stroke_width=3))
        self.play(Create(self.axes), run_time=0.7)
        self.play(LaggedStart(*[Create(c) for c in curves], lag_ratio=0.15), run_time=1.5)
        note = self.ja_text("単調増加", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def uniform(self):
        import math
        lim = self.axes.plot(lambda x: 1.5, x_range=[0.1, 3.8], color=ORANGE, stroke_width=4)
        cap = self.ja_text("点ごとに収束", font_size=24).move_to(self.note)
        self.play(Create(lim), Transform(self.note, cap), run_time=1.3)
        self.read(0.3)
        cap2 = self.ja_text("実は一様", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(lim, color=YELLOW), run_time=1.1)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("単調点収束 ⇒ 一様収束", font_size=28)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.7)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
