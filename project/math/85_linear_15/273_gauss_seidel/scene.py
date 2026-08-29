from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class GaussSeidel(PacedScene):
    """#273 ガウス・ザイデル：最新成分をすぐ使う（約45秒）"""

    def construct(self):
        self.show_heading("ガウス・ザイデル法")
        self.draw_grid()
        self.update_flow()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        self.cells = VGroup()
        vals = ["x_1", "x_2", "x_3"]
        for i, v in enumerate(vals):
            box = RoundedRectangle(width=1.5, height=0.9, corner_radius=0.08, color=BLUE, stroke_width=3)
            box.shift(LEFT * 2.2 + RIGHT * i * 1.9 + UP * 0.6)
            lab = MathTex(v, font_size=36).move_to(box)
            self.cells.add(VGroup(box, lab))
        self.play(LaggedStart(*[FadeIn(c) for c in self.cells], lag_ratio=0.15), run_time=1.4)
        note = self.ja_text("未知数", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def update_flow(self):
        arrows = VGroup()
        for i in range(2):
            a = Arrow(
                self.cells[i].get_right(),
                self.cells[i + 1].get_left(),
                buff=0.08,
                color=ORANGE,
                stroke_width=4,
            )
            arrows.add(a)
        cap = self.ja_text("すぐ次へ渡す", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.2), Transform(self.note, cap), run_time=1.5)
        self.read(0.3)
        # highlight first cell as updated
        new1 = MathTex(r"x_1^{(k+1)}", font_size=32, color=YELLOW).move_to(self.cells[0][1])
        cap2 = self.ja_text("最新を使う", font_size=24).move_to(self.note)
        self.play(Transform(self.cells[0][1], new1), Transform(self.note, cap2), run_time=1.2)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"(D+L)x^{(k+1)}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"(D+L)x^{(k+1)}=b-Ux^{(k)}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"(D+L)x^{(k+1)}=b-Ux^{(k)}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
