from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class SubspaceIteration(PacedScene):
    """#502 部分空間反復：ブロックで固有空間を追う（約45秒）"""

    def construct(self):
        self.show_heading("部分空間反復")
        self.draw_block()
        self.qr_step()
        self.show_formula()
        self.read(1.4)

    def draw_block(self):
        cols = VGroup(*[
            Rectangle(width=0.55, height=2.2, color=BLUE, stroke_width=2, fill_opacity=0.2)
            .shift(LEFT * 2.5 + RIGHT * i * 0.7 + UP * 0.2)
            for i in range(3)
        ])
        self.play(LaggedStart(*[FadeIn(c) for c in cols], lag_ratio=0.1), run_time=1.2)
        note = self.ja_text("複数ベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def qr_step(self):
        box = RoundedRectangle(width=2.8, height=1.5, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(RIGHT * 2.0 + UP * 0.2)
        lab = MathTex(r"QR", font_size=36).move_to(box)
        arrow = Arrow(LEFT * 0.8, RIGHT * 0.4, buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("直交化して反復", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Create(box), FadeIn(lab), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("上位固有空間", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"Y_{k+1}=AQ_k,\quad Y_{k+1}=Q_{k+1}R_{k+1}").scale(0.78)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
