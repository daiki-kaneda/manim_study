from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class StirlingSecond(PacedScene):
    """#389 スターリング第二種：漸化式 S(n,k)=k S(n-1,k)+S(n-1,k-1)（約45秒）"""

    def construct(self):
        self.show_heading("スターリング第二種")
        self.draw_table()
        self.recurrence()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_table(self):
        # small S(n,k) triangle values
        rows = [
            ["1"],
            ["1", "1"],
            ["1", "3", "1"],
            ["1", "7", "6", "1"],
        ]
        cells = VGroup()
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                t = MathTex(val, font_size=32)
                t.move_to(LEFT * 2.2 + RIGHT * j * 0.95 + UP * 1.5 + DOWN * i * 0.7)
                cells.add(t)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.05), run_time=1.6)
        note = self.ja_text("分割の数", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.cells = cells

    def recurrence(self):
        # indices: 0=1; 1=1,2=1; 3=1,4=3,5=1; 6=1,7=7,8=6,9=1
        box = SurroundingRectangle(self.cells[7], color=YELLOW, buff=0.12)
        arrows = VGroup(
            Arrow(self.cells[4].get_bottom(), self.cells[7].get_top(), buff=0.08, color=ORANGE, stroke_width=3),
            Arrow(self.cells[3].get_bottom(), self.cells[7].get_top(), buff=0.08, color=TEAL, stroke_width=3),
        )
        cap = self.ja_text("前の行から", font_size=24).move_to(self.note)
        self.play(Create(box), Transform(self.note, cap), run_time=1.0)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("漸化式", font_size=24).move_to(self.note)
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
        eq = MathTex(r"S(n,k)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"S(n,k)=k\,S(n-1,k)+S(n-1,k-1)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"S(n,k)=k\,S(n-1,k)+S(n-1,k-1)").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
