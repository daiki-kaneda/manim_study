from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class EntropyRate(PacedScene):
    """#220 エントロピー率は 1 ステップの平均情報（約45秒）"""

    def construct(self):
        self.show_heading("エントロピー率")
        self.draw_chain()
        self.show_rate()
        self.show_formula()
        self.read(1.4)

    def draw_chain(self):
        self.A = LEFT * 2.5 + UP * 0.6
        self.B = RIGHT * 2.5 + UP * 0.6
        da = Dot(self.A, radius=0.18, color=BLUE)
        db = Dot(self.B, radius=0.18, color=TEAL)
        la = MathTex("A", font_size=30).next_to(da, DOWN, buff=0.15)
        lb = MathTex("B", font_size=30).next_to(db, DOWN, buff=0.15)
        # two arrows both ways
        ab = ArcBetweenPoints(self.A + UP * 0.25 + RIGHT * 0.2, self.B + UP * 0.25 + LEFT * 0.2, angle=-0.6, color=YELLOW)
        ba = ArcBetweenPoints(self.B + DOWN * 0.25 + LEFT * 0.2, self.A + DOWN * 0.25 + RIGHT * 0.2, angle=-0.6, color=ORANGE)
        self.play(FadeIn(da), FadeIn(db), FadeIn(la), FadeIn(lb), run_time=1.1)
        self.play(Create(ab), Create(ba), run_time=1.3)
        note = self.ja_text("マルコフ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.35)
        self.note = note

    def show_rate(self):
        # stationary weights
        bars = VGroup(
            Rectangle(width=0.7, height=1.6, color=BLUE, fill_opacity=0.5, stroke_width=2).move_to(LEFT * 1.2 + DOWN * 1.3),
            Rectangle(width=0.7, height=1.0, color=TEAL, fill_opacity=0.5, stroke_width=2).move_to(RIGHT * 0.3 + DOWN * 1.0),
        )
        # align bottoms
        for b, h in zip(bars, (1.6, 1.0)):
            b.move_to(b.get_center())
            b.align_to(DOWN * 2.0, DOWN)
            b.shift(UP * h / 2)
        bars[0].move_to(LEFT * 1.0 + DOWN * 1.2)
        bars[1].move_to(RIGHT * 0.5 + DOWN * 1.5)
        bars[0] = Rectangle(width=0.75, height=1.5, color=BLUE, fill_opacity=0.55, stroke_width=2)
        bars[1] = Rectangle(width=0.75, height=0.95, color=TEAL, fill_opacity=0.55, stroke_width=2)
        bars[0].move_to(LEFT * 1.0 + DOWN * 1.35)
        bars[1].move_to(RIGHT * 0.6 + DOWN * 1.62)
        cap = self.ja_text("定常分布", font_size=24).move_to(self.note)
        self.play(FadeIn(bars[0]), FadeIn(bars[1]), Transform(self.note, cap), run_time=1.4)
        self.read(0.3)
        cap2 = self.ja_text("1 歩の情報", font_size=24).move_to(self.note)
        flash = SurroundingRectangle(VGroup(bars[0], bars[1]), color=ORANGE, buff=0.2)
        self.play(Create(flash), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"H=\sum_i\pi_i H(\cdot\mid i)").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
