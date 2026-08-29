from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CouponCollector(PacedScene):
    """#243 クーポン：全部揃う待ち時間（約45秒）"""

    def construct(self):
        self.show_heading("クーポンコレクター")
        self.draw_types()
        self.fill_in()
        self.show_formula()
        self.read(1.4)

    def draw_types(self):
        self.slots = VGroup()
        for i in range(6):
            sq = RoundedRectangle(width=0.85, height=0.85, corner_radius=0.08, color=GREY, stroke_width=2)
            sq.shift(LEFT * 2.7 + RIGHT * i * 1.0 + UP * 0.8)
            self.slots.add(sq)
        self.play(LaggedStart(*[FadeIn(s, scale=0.8) for s in self.slots], lag_ratio=0.08), run_time=1.4)
        note = self.ja_text("n 種類", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def fill_in(self):
        cols = [BLUE, TEAL, YELLOW, ORANGE, GREEN, RED]
        # fill quickly first few, slower feel for last
        for i, col in enumerate(cols):
            fill = self.slots[i].copy().set_fill(col, opacity=0.7).set_stroke(col, width=2)
            self.play(Transform(self.slots[i], fill), run_time=0.55 if i < 4 else 0.95)
            if i == 2:
                cap = self.ja_text("だんだん遅い", font_size=24).move_to(self.note)
                self.play(Transform(self.note, cap), run_time=0.4)
        cap2 = self.ja_text("全部揃う", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.6)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\mathbb{E}[T]=n H_n\sim n\log n").scale(0.9)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
