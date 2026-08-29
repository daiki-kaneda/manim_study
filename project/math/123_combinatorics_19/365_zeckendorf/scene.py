from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Zeckendorf(PacedScene):
    """#365 ゼッケンドルフ：隣り合わないフィボナッチ和（約45秒）"""

    def construct(self):
        self.show_heading("ゼッケンドルフの定理")
        self.draw_fibs()
        self.select()
        self.show_formula()
        self.read(1.4)

    def draw_fibs(self):
        vals = ["1", "2", "3", "5", "8", "13"]
        self.boxes = VGroup()
        for i, v in enumerate(vals):
            b = RoundedRectangle(width=1.0, height=0.85, corner_radius=0.08, color=BLUE, stroke_width=3)
            b.shift(LEFT * 3.0 + RIGHT * i * 1.15 + UP * 0.5)
            t = MathTex(v, font_size=32).move_to(b)
            self.boxes.add(VGroup(b, t))
        self.play(LaggedStart(*[FadeIn(b) for b in self.boxes], lag_ratio=0.1), run_time=1.5)
        note = self.ja_text("フィボナッチ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def select(self):
        # select non-adjacent: 13+5+2 = indices 5,3,1
        chosen = [1, 3, 5]
        rects = VGroup(*[SurroundingRectangle(self.boxes[i], color=ORANGE, buff=0.06) for i in chosen])
        # cross out adjacent idea
        cap = self.ja_text("隣を避ける", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[Create(r) for r in rects], lag_ratio=0.12), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("一意に表せる", font_size=24).move_to(self.note)
        total = MathTex(r"n=13+5+2", color=YELLOW, font_size=36).shift(DOWN * 0.6)
        self.play(Write(total), Transform(self.note, cap2), run_time=1.3)
        self.read(0.4)

    def show_formula(self):
        formula = self.ja_text("隣り合わないフィボナッチ和", font_size=28)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
