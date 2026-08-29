from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class LaxMilgram(PacedScene):
    """#356 ラックス・ミルグラム：強圧双線形なら一意解（約45秒）"""

    def construct(self):
        self.show_heading("ラックス・ミルグラム")
        self.draw_form()
        self.solve()
        self.show_formula()
        self.read(1.4)

    def draw_form(self):
        a = MathTex(r"a(u,v)", font_size=48).shift(UP * 1.0 + LEFT * 1.5)
        ell = MathTex(r"\ell(v)", font_size=48).shift(UP * 1.0 + RIGHT * 1.8)
        self.play(FadeIn(a), FadeIn(ell), run_time=1.3)
        note = self.ja_text("双線形形式", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def solve(self):
        eq = MathTex(r"a(u,v)=\ell(v)\ \forall v", font_size=40).shift(DOWN * 0.2)
        cap = self.ja_text("弱形式", font_size=24).move_to(self.note)
        self.play(Write(eq), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("強圧なら一意", font_size=24).move_to(self.note)
        box = SurroundingRectangle(eq, color=YELLOW, buff=0.15)
        self.play(Create(box), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"a(u,u)\ge \alpha\|u\|^{2}\Rightarrow\exists!u").scale(0.82)
        formula.to_edge(DOWN, buff=0.24)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
