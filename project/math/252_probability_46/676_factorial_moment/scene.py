from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FactorialMoment(PacedScene):
    """#676 階乗モーメント測度：点過程の高次統計（約45秒）"""

    def construct(self):
        self.show_heading("階乗モーメント測度")
        self.draw()
        self.moment()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.8, height=1.0, corner_radius=0.08, color=c, stroke_width=3).shift(pos)
            for c, pos in [(BLUE, LEFT * 2.5 + UP * 0.3), (ORANGE, ORIGIN + UP * 0.3), (TEAL, RIGHT * 2.5 + UP * 0.3)]
        ])
        labs = VGroup(*[MathTex(s, font_size=26).move_to(b) for s, b in zip([r"\alpha_1", r"\alpha_2", r"\alpha_n"], boxes)])
        self.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.1), FadeIn(labs), run_time=1.4)
        note = self.ja_text("高次強度", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def moment(self):
        cap = self.ja_text("重複なし計数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("積密度の積分", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\alpha^{(n)}(dx)=\rho^{(n)}(x)\,dx").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
