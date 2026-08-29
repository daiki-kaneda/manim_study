from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class BlockCoordinate(PacedScene):
    """#503 ブロック座標：変数ブロックを順に最適化（約45秒）"""

    def construct(self):
        self.show_heading("ブロック座標")
        self.draw_blocks()
        self.cycle()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_blocks(self):
        blocks = VGroup(*[
            RoundedRectangle(width=1.6, height=1.1, corner_radius=0.1, color=c, stroke_width=3)
            .shift(LEFT * 2.6 + RIGHT * i * 2.0 + UP * 0.4)
            for i, c in enumerate([BLUE, TEAL, ORANGE])
        ])
        labs = VGroup(*[MathTex(rf"x_{{{i+1}}}", font_size=30).move_to(blocks[i]) for i in range(3)])
        self.play(LaggedStart(*[Create(b) for b in blocks], lag_ratio=0.12), FadeIn(labs), run_time=1.4)
        note = self.ja_text("ブロック分割", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.blocks = blocks

    def cycle(self):
        hl = SurroundingRectangle(self.blocks[0], color=YELLOW, buff=0.08)
        cap = self.ja_text("一つずつ最小化", font_size=24).move_to(self.note)
        self.play(Create(hl), Transform(self.note, cap), run_time=1.0)
        self.play(hl.animate.move_to(self.blocks[1]), run_time=0.6)
        self.play(hl.animate.move_to(self.blocks[2]), run_time=0.6)
        self.read(0.25)
        cap2 = self.ja_text("座標降下の拡張", font_size=24).move_to(self.note)
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
        eq = MathTex(r"x_i\leftarrow\arg\min_{x_i}f(x_1,\ldots,x_i,\ldots,x_m)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"x_i\leftarrow\arg\min_{x_i}f(x_1,\ldots,x_i,\ldots,x_m)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"x_i\leftarrow\arg\min_{x_i}f(x_1,\ldots,x_i,\ldots,x_m)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
