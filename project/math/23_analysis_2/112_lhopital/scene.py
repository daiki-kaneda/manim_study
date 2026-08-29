from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class LHopital(JapaneseScene):
    """#112 ロピタルの定理（約90秒）"""

    def construct(self):
        self.show_heading("ロピタル")
        self.draw_curves()
        self.zoom_slopes()
        self.show_formula()
        self.hold(1.2)

    def draw_curves(self):
        self.axes = Axes(
            x_range=[-0.2, 2.6, 1],
            y_range=[-0.2, 3.2, 1],
            x_length=7.0,
            y_length=3.6,
            tips=False,
            axis_config={"stroke_width": 2, "include_ticks": False},
        ).shift(DOWN * 0.15 + LEFT * 0.55)
        f = self.axes.plot(lambda x: 0.85 * x, x_range=[0, 2.4], color=BLUE, stroke_width=5)
        g = self.axes.plot(lambda x: 0.45 * x, x_range=[0, 2.4], color=GREEN, stroke_width=5)
        lf = MathTex("f", color=BLUE, font_size=30).next_to(f, UR, buff=0.08)
        lg = MathTex("g", color=GREEN, font_size=30).next_to(g, DR, buff=0.08)
        self.play(Create(self.axes), run_time=0.4)
        self.play(Create(f), Create(g), FadeIn(lf), FadeIn(lg), run_time=0.85)
        note = self.ja_text("どちらも 0 へ", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.3)
        self.hold(0.5)
        self.note = note

    def zoom_slopes(self):
        cap = self.ja_text("比は傾きへ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.4)
        self.hold(0.65)

    def show_formula(self):
        formula = MathTex(r"\lim\frac{f}{g}=\lim\frac{f'}{g'}").scale(1.05)
        formula.to_edge(DOWN, buff=0.35)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
