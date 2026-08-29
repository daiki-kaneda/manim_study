from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class Laplacian(PacedScene):
    """#163 ラプラシアンは平均との差（約45秒）"""

    def construct(self):
        self.origin = LEFT * 0.4 + DOWN * 0.15
        self.show_heading("ラプラシアン")
        self.draw_grid()
        self.compare_neighbors()
        self.show_formula()
        self.read(1.4)

    def draw_grid(self):
        cells = VGroup()
        vals = [
            [1, 2, 1],
            [2, 4, 2],
            [1, 2, 1],
        ]
        self.rects = {}
        self.labels = {}
        for i in range(3):
            for j in range(3):
                r = Square(side_length=1.15, color=GREY, stroke_width=2, fill_opacity=0.12)
                r.move_to(self.origin + RIGHT * (j - 1) * 1.2 + UP * (1 - i) * 1.2)
                lab = MathTex(str(vals[i][j]), font_size=32).move_to(r.get_center())
                cells.add(r, lab)
                self.rects[(i, j)] = r
                self.labels[(i, j)] = lab
        self.play(LaggedStart(*[FadeIn(m) for m in cells], lag_ratio=0.05), run_time=2.0)
        self.read(0.35)

    def compare_neighbors(self):
        center = self.rects[(1, 1)]
        note = self.ja_text("中央", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(center.animate.set_fill(YELLOW, opacity=0.35), FadeIn(note), run_time=1.0)
        self.read(0.35)
        neigh = [(0, 1), (1, 0), (1, 2), (2, 1)]
        self.play(*[self.rects[p].animate.set_fill(BLUE, opacity=0.35) for p in neigh], run_time=1.1)
        cap = self.ja_text("まわり平均", font_size=24).move_to(note)
        self.play(Transform(note, cap), run_time=0.7)
        self.read(0.35)
        avg = MathTex(r"2", color=BLUE, font_size=36)
        avg.next_to(center, DOWN, buff=1.55)
        # place to the right instead
        avg.move_to(self.origin + RIGHT * 3.4)
        cap2 = self.ja_text("差", font_size=24).move_to(note)
        self.play(FadeIn(avg), Transform(note, cap2), run_time=1.0)
        self.read(0.4)
        self.note = note

    def show_formula(self):
        formula = MathTex(r"\Delta u=u_{xx}+u_{yy}").scale(1.0)
        formula.to_edge(DOWN, buff=0.28)
        self.play(Write(formula), run_time=1.7)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
