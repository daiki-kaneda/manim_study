from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Microlocal(PacedScene):
    """#596 ミクロローカル：位置と周波数を同時に見る（約45秒）"""

    def construct(self):
        self.show_heading("ミクロローカル")
        self.draw_bundle()
        self.localize()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_bundle(self):
        base = Line(LEFT * 3, RIGHT * 2.5, color=BLUE, stroke_width=4).shift(DOWN * 0.8)
        fibers = VGroup(*[
            Arrow(base.point_from_proportion(t), base.point_from_proportion(t) + UP * 1.6, buff=0, color=TEAL, stroke_width=3)
            for t in [0.15, 0.35, 0.55, 0.75]
        ])
        self.play(Create(base), LaggedStart(*[GrowArrow(f) for f in fibers], lag_ratio=0.1), run_time=1.5)
        note = self.ja_text("余接束", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def localize(self):
        cap = self.ja_text("点と方向で局所化", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("作用素の特異性解析", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\cdots").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\Rightarrow").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = self.ja_text("ミクロローカル：位置×周波数の解析", font_size=26)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
