from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class WaldEquation(PacedScene):
    """#231 ワルド：停止時刻でも期待値は積（約45秒）"""

    def construct(self):
        self.show_heading("ワルドの等式")
        self.draw_sum()
        self.factor()
        self.show_formula()
        self.read(1.4)

    def draw_sum(self):
        boxes = VGroup()
        for i in range(5):
            sq = RoundedRectangle(width=0.85, height=0.7, corner_radius=0.08, color=BLUE, stroke_width=3)
            lab = MathTex(f"X_{{{i+1}}}", font_size=26)
            g = VGroup(sq, lab)
            g.shift(LEFT * 2.8 + RIGHT * i * 1.05 + UP * 0.6)
            boxes.add(g)
        self.play(LaggedStart(*[FadeIn(b, scale=0.8) for b in boxes], lag_ratio=0.1), run_time=1.5)
        brace = Brace(boxes[:3], DOWN, color=ORANGE)
        nlab = MathTex("N=3", color=ORANGE, font_size=30).next_to(brace, DOWN, buff=0.12)
        note = self.ja_text("止まる回数", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(GrowFromCenter(brace), FadeIn(nlab), FadeIn(note), run_time=1.2)
        self.read(0.35)
        self.note = note
        self.boxes = boxes

    def factor(self):
        # highlight first N, fade rest
        self.play(
            *[b.animate.set_opacity(0.25) for b in self.boxes[3:]],
            run_time=0.8,
        )
        cap = self.ja_text("合計の期待値", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.25)
        prod = MathTex(r"\mathbb{E}[N]\,\mathbb{E}[X]", color=YELLOW).scale(1.0)
        prod.shift(DOWN * 0.85)
        cap2 = self.ja_text("積に分解", font_size=24).move_to(self.note)
        self.play(Write(prod), Transform(self.note, cap2), run_time=1.4)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\mathbb{E}[S_N]=\mathbb{E}[N]\mathbb{E}[X]").scale(0.95)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
