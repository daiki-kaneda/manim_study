from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class KroneckerProduct(PacedScene):
    """#225 クロネッカー積はブロックの複製（約45秒）"""

    def construct(self):
        self.show_heading("クロネッカー積")
        self.draw_factors()
        self.expand_blocks()
        self.show_formula()
        self.read(1.4)

    def draw_factors(self):
        a = Matrix([["a", "b"], ["c", "d"]], h_buff=0.7, v_buff=0.55).scale(0.7)
        b = Matrix([["1", "0"], ["0", "1"]], h_buff=0.7, v_buff=0.55).scale(0.7)
        a.shift(LEFT * 3.0 + UP * 0.4)
        b.shift(LEFT * 0.6 + UP * 0.4)
        times = MathTex(r"\otimes").scale(1.1).move_to((a.get_right() + b.get_left()) / 2)
        self.play(FadeIn(a), FadeIn(times), FadeIn(b), run_time=1.4)
        note = self.ja_text("二つの行列", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.a, self.b = a, b

    def expand_blocks(self):
        # 4x4 visual blocks of scaled I
        blocks = VGroup()
        labels = [["aI", "bI"], ["cI", "dI"]]
        colors = [[BLUE, TEAL], [YELLOW, ORANGE]]
        for i in range(2):
            for j in range(2):
                sq = RoundedRectangle(width=1.35, height=1.0, corner_radius=0.08, color=colors[i][j], stroke_width=3)
                lab = MathTex(labels[i][j], font_size=28, color=colors[i][j])
                g = VGroup(sq, lab)
                g.move_to(RIGHT * 2.0 + RIGHT * (j * 1.55) + DOWN * (i * 1.15) + UP * 0.5)
                blocks.add(g)
        cap = self.ja_text("ブロックに複製", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(b, scale=0.8) for b in blocks], lag_ratio=0.12), Transform(self.note, cap), run_time=1.8)
        self.read(0.45)

    def show_formula(self):
        formula = MathTex(r"(A\otimes B)_{ij}=a_{ij}B").scale(0.95)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
