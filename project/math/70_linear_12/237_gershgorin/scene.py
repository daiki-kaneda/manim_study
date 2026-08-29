from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Gershgorin(PacedScene):
    """#237 ゲルシュゴリン：固有値は行円盤の中（約45秒）"""

    def construct(self):
        self.origin = LEFT * 1.2 + DOWN * 0.3
        self.show_heading("ゲルシュゴリン")
        self.draw_disks()
        self.mark_eigen()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_disks(self):
        # centers at diagonal entries 2, -1, 0.5 with radii 1.2, 0.9, 0.7
        disks = [
            (2.0, 0.0, 1.15, BLUE),
            (-1.1, 0.0, 0.95, TEAL),
            (0.4, 0.0, 0.7, YELLOW),
        ]
        self.circles = VGroup()
        for cx, cy, r, col in disks:
            c = Circle(radius=r * 0.85, color=col, stroke_width=3)
            c.move_to(self.origin + RIGHT * cx * 0.85 + UP * cy)
            self.circles.add(c)
            self.play(Create(c), run_time=0.7)
        note = self.ja_text("行の円盤", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mark_eigen(self):
        # place dots inside disks as "eigenvalues"
        pts = [
            self.origin + RIGHT * 1.7,
            self.origin + LEFT * 0.7 + UP * 0.35,
            self.origin + RIGHT * 0.55 + DOWN * 0.25,
        ]
        dots = VGroup(*[Dot(p, color=ORANGE, radius=0.1) for p in pts])
        cap = self.ja_text("固有値は中", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.15), Transform(self.note, cap), run_time=1.5)
        self.read(0.45)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"D_i").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"D_i=\{z:|z-a_{ii}|\le R_i\}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"D_i=\{z:|z-a_{ii}|\le R_i\}").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
