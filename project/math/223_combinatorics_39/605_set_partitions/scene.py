from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class SetPartitions(PacedScene):
    """#605 セット分割：集合を空でないブロックへ（約45秒）"""

    def construct(self):
        self.show_heading("セット分割")
        self.draw_blocks()
        self.bell()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        blocks = VGroup(*[
            RoundedRectangle(width=w, height=1.0, corner_radius=0.1, color=c, stroke_width=3)
            .shift(pos)
            for w, c, pos in [
                (1.8, BLUE, LEFT * 2.8 + UP * 0.4),
                (2.2, ORANGE, ORIGIN + UP * 0.4),
                (1.6, TEAL, RIGHT * 2.6 + UP * 0.4),
            ]
        ])
        labs = VGroup(
            MathTex(r"\{1,4\}", font_size=26).move_to(blocks[0]),
            MathTex(r"\{2,3,6\}", font_size=26).move_to(blocks[1]),
            MathTex(r"\{5\}", font_size=26).move_to(blocks[2]),
        )
        self.play(LaggedStart(*[Create(b) for b in blocks], lag_ratio=0.12), FadeIn(labs), run_time=1.4)
        note = self.ja_text("ブロック分割", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def bell(self):
        cap = self.ja_text("ベル数が総数", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("スターリング第二種の和", font_size=24).move_to(self.note)
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
        eq = MathTex(r"B_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"B_n=\sum_k S(n,k)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"B_n=\sum_k S(n,k)").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
