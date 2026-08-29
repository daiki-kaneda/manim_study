from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CatalanTriangle(PacedScene):
    """#473 カタラン三角：B_n,k でカタランを細分（約45秒）"""

    def construct(self):
        self.show_heading("カタラン三角")
        self.draw_table()
        self.meaning()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_table(self):
        rows = [
            ["1"],
            ["1", "1"],
            ["2", "3", "2"],
            ["5", "9", "9", "5"],
        ]
        cells = VGroup()
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                t = MathTex(val, font_size=30)
                t.move_to(LEFT * 2.0 + RIGHT * j * 0.9 + UP * 1.4 + DOWN * i * 0.65)
                cells.add(t)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.04), run_time=1.5)
        note = self.ja_text("数表", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.cells = cells

    def meaning(self):
        box = SurroundingRectangle(self.cells[0], color=YELLOW, buff=0.12)
        # highlight last of a row roughly
        box = SurroundingRectangle(VGroup(self.cells[6], self.cells[7], self.cells[8], self.cells[9]), color=YELLOW, buff=0.12)
        cap = self.ja_text("行の端がカタラン", font_size=24).move_to(self.note)
        self.play(Create(box), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("道の細分", font_size=24).move_to(self.note)
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
        eq = MathTex(r"B(n,k)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"B(n,k)=\frac{k+1}{n+1}\binom{2n-k}{n}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"B(n,k)=\frac{k+1}{n+1}\binom{2n-k}{n}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
