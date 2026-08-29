from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class KrylovRecycling(PacedScene):
    """#586 クレイロフ再利用：部分空間を持ち越す（約45秒）"""

    def construct(self):
        self.show_heading("クレイロフ再利用")
        self.draw_space()
        self.recycle()
        self.show_formula()
        self.read(1.4)

    def draw_space(self):
        boxes = VGroup(*[
            RoundedRectangle(width=1.5, height=1.0, corner_radius=0.08, color=BLUE, stroke_width=2)
            .shift(LEFT * 2.6 + RIGHT * i * 1.8 + UP * 0.5)
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.12), run_time=1.3)
        note = self.ja_text("部分空間", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def recycle(self):
        arrow = CurvedArrow(LEFT * 1.0 + DOWN * 0.3, RIGHT * 2.0 + DOWN * 0.3, color=ORANGE)
        cap = self.ja_text("次の系へ再利用", font_size=24).move_to(self.note)
        self.play(Create(arrow), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("系列問題向き", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\mathcal{K}\leftarrow\mathrm{recycle}(\mathcal{K}_{\mathrm{old}})").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
