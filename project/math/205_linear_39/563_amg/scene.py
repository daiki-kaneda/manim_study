from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class AlgebraicMultigrid(PacedScene):
    """#563 代数的多重グリッド：行列から粗い空間を作る（約45秒）"""

    def construct(self):
        self.show_heading("代数的多重グリッド")
        self.draw_graph()
        self.coarsen()
        self.show_formula()
        self.read(1.4)

    def draw_graph(self):
        dots = VGroup(*[Dot(LEFT * 2 + RIGHT * (i % 3) * 1.1 + UP * (0.8 - (i // 3) * 1.0), color=BLUE, radius=0.1) for i in range(6)])
        edges = VGroup(*[
            Line(dots[i].get_center(), dots[j].get_center(), color=GREY, stroke_width=2)
            for i, j in [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 5)]
        ])
        self.play(Create(edges), FadeIn(dots), run_time=1.4)
        note = self.ja_text("強接続グラフ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def coarsen(self):
        cap = self.ja_text("粗い変数を選ぶ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("格子不要", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"A_c=RAP").scale(0.95)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
