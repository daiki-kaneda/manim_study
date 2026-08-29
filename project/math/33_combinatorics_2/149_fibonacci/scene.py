from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Fibonacci(PacedScene):
    """#149 フィボナッチ数列は正方形が隣に付く（約55秒）"""

    def construct(self):
        self.show_heading("フィボナッチ")
        self.draw_squares()
        self.mark_sum()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_squares(self):
        origin = LEFT * 4.85 + DOWN * 2.05
        u = 0.52
        # (size, bl_x, bl_y, color)
        specs = [
            (1, 0, 0, BLUE),
            (1, 1, 0, TEAL),
            (2, 0, 1, GREEN),
            (3, 2, 0, YELLOW),
            (5, 0, 3, ORANGE),
            (8, 5, 0, RED),
        ]
        self.squares = VGroup()
        labels = VGroup()
        for size, x, y, color in specs:
            bl = origin + RIGHT * (x * u) + UP * (y * u)
            sq = Square(side_length=size * u, color=color, stroke_width=3, fill_opacity=0.35)
            sq.move_to(bl + RIGHT * (size * u / 2) + UP * (size * u / 2))
            lab = MathTex(str(size), font_size=22 + 2 * min(size, 5))
            lab.move_to(sq.get_center())
            self.squares.add(sq)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(s, scale=0.85) for s in self.squares], lag_ratio=0.22), run_time=3.4)
        self.play(LaggedStart(*[FadeIn(lab) for lab in labels], lag_ratio=0.12), run_time=1.2)
        note = self.ja_text("隣に足す", font_size=24)
        note.to_edge(RIGHT, buff=0.28).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.5)
        self.read(0.4)
        self.note = note
        self.labels = labels

    def mark_sum(self):
        cap = self.ja_text("3+5=8", font_size=24).move_to(self.note)
        self.play(
            Indicate(self.squares[3], color=WHITE),
            Indicate(self.squares[4], color=WHITE),
            Transform(self.note, cap),
            run_time=1.4,
        )
        self.read(0.4)
        self.play(Indicate(self.squares[5], color=WHITE), run_time=1.0)
        cap2 = self.ja_text("前の二つ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
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
        eq = MathTex(r"F_n").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"F_n=F_{n-1}+F_{n-2}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"F_n=F_{n-1}+F_{n-2}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
