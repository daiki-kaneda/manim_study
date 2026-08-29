from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class RankNullity(JapaneseScene):
    """#108 階数・核の定理（約90秒）"""

    def construct(self):
        self.show_heading("階数と核")
        self.show_dims()
        self.show_formula()
        self.hold(1.2)

    def show_dims(self):
        domain = Square(side_length=2.2, color=BLUE, fill_opacity=0.35, stroke_width=2)
        domain.shift(LEFT * 3.1 + DOWN * 0.1)
        dlab = self.ja_text("2 次元", font_size=24).next_to(domain, DOWN, buff=0.2)
        image = Line(RIGHT * 1.3 + LEFT * 1.4, RIGHT * 1.3 + RIGHT * 1.4, color=YELLOW, stroke_width=8)
        image.shift(DOWN * 0.1)
        ilab = self.ja_text("像 1 次元", font_size=24).next_to(image, DOWN, buff=0.35)
        arrow = Arrow(domain.get_right(), image.get_left(), buff=0.25, color=WHITE)
        self.play(FadeIn(domain), FadeIn(dlab), run_time=0.6)
        self.play(GrowArrow(arrow), FadeIn(image), FadeIn(ilab), run_time=0.7)
        note = self.ja_text("核も 1 次元", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = MathTex(r"\dim\ker A+\dim\mathrm{Im}\,A=n").scale(0.95)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.05)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
