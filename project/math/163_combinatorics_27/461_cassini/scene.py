from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class CassiniIdentity(PacedScene):
    """#461 カッシーニ：F_{n+1}F_{n-1}-F_n^2=(-1)^n（約45秒）"""

    def construct(self):
        self.show_heading("カッシーニの恒等式")
        self.draw_fib()
        self.identity()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_fib(self):
        vals = ["1", "1", "2", "3", "5", "8", "13"]
        cells = VGroup(*[MathTex(v, font_size=34) for v in vals]).arrange(RIGHT, buff=0.55).shift(UP * 0.9)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.08), run_time=1.4)
        note = self.ja_text("フィボナッチ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.cells = cells

    def identity(self):
        box = SurroundingRectangle(VGroup(self.cells[3], self.cells[4], self.cells[5]), color=YELLOW, buff=0.15)
        cap = self.ja_text("隣どうしの積", font_size=24).move_to(self.note)
        self.play(Create(box), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("差は ±1", font_size=24).move_to(self.note)
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
        eq = MathTex(r"F_{n+1}F_{n-1}-F_n^{2}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"F_{n+1}F_{n-1}-F_n^{2}=(-1)^{n}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"F_{n+1}F_{n-1}-F_n^{2}=(-1)^{n}").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
