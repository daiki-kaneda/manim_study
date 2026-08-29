from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MatrixCompletion(PacedScene):
    """#479 行列補完：観測から低ランクを復元（約45秒）"""

    def construct(self):
        self.show_heading("行列補完")
        self.draw_mask()
        self.fill()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_mask(self):
        cells = VGroup()
        known = {(0, 0), (0, 2), (1, 1), (2, 0), (2, 3), (3, 2)}
        for i in range(4):
            for j in range(4):
                sq = Square(side_length=0.55, stroke_width=2, color=GREY)
                sq.shift(LEFT * 2.4 + RIGHT * j * 0.6 + UP * 1.2 + DOWN * i * 0.6)
                if (i, j) in known:
                    sq.set_fill(BLUE, opacity=0.55)
                    sq.set_stroke(BLUE, width=2)
                cells.add(sq)
        self.play(LaggedStart(*[FadeIn(c) for c in cells], lag_ratio=0.03), run_time=1.4)
        note = self.ja_text("一部だけ観測", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.cells = cells

    def fill(self):
        fills = VGroup(*[
            Square(side_length=0.55, fill_opacity=0.45, fill_color=ORANGE, stroke_width=0)
            .move_to(self.cells[i * 4 + j])
            for i in range(4) for j in range(4)
            if (i, j) not in {(0, 0), (0, 2), (1, 1), (2, 0), (2, 3), (3, 2)}
        ])
        cap = self.ja_text("低ランク復元", font_size=24).move_to(self.note)
        self.play(FadeIn(fills), Transform(self.note, cap), run_time=1.3)
        self.read(0.25)
        cap2 = self.ja_text("核ノルム最小化", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\min_X\|X\|_*\ \mathrm{s.t.}\ P_\Omega(X)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\min_X\|X\|_*\ \mathrm{s.t.}\ P_\Omega(X)=P_\Omega(M)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\min_X\|X\|_*\ \mathrm{s.t.}\ P_\Omega(X)=P_\Omega(M)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
