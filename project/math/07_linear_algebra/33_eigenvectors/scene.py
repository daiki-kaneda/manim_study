from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

import numpy as np
from manim import *
from manim_math import JapaneseScene
from manim_math.geometry import apply_2d


class Eigenvectors(JapaneseScene):
    """#33 固有ベクトル（約90秒）"""

    def construct(self):
        self.origin = LEFT * 2.4 + DOWN * 0.35
        self.unit = 1.35
        self.M = [[2.0, 1.0], [0.0, 1.0]]
        self.show_heading("固有ベクトル")
        self.draw_arrows()
        self.apply_map()
        self.show_formula()
        self.hold(1.2)

    def _pt(self, xy):
        return self.origin + np.array([xy[0] * self.unit, xy[1] * self.unit, 0.0])

    def _arrow(self, xy, color):
        return Arrow(self.origin, self._pt(xy), buff=0, color=color, stroke_width=4)

    def draw_arrows(self):
        axes_x = Line(self.origin + LEFT * 0.4, self.origin + RIGHT * 4.2, color=GREY, stroke_width=2)
        axes_y = Line(self.origin + DOWN * 2.0, self.origin + UP * 2.2, color=GREY, stroke_width=2)
        self.play(Create(axes_x), Create(axes_y), run_time=0.5)
        # (1,0) λ=2; (1,-1) λ=1; その他は向きが変わる
        specs = [
            ((1.0, 0.0), YELLOW, True),
            ((1.0, -1.0), ORANGE, True),
            ((0.2, 1.15), BLUE, False),
            ((0.85, 0.55), TEAL, False),
        ]
        self.arrows = []
        self.eigen = []
        for xy, color, is_eig in specs:
            arr = self._arrow(xy, color)
            self.arrows.append((arr, xy, color, is_eig))
            self.play(GrowArrow(arr), run_time=0.35)
        note = self.ja_text("いろいろな向きのベクトル", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.7)
        self.play(FadeIn(note), run_time=0.4)
        self.hold(0.6)
        self.note = note

    def apply_map(self):
        anims = []
        highlights = []
        for arr, xy, color, is_eig in self.arrows:
            img = apply_2d(self.M, xy)[:2]
            nxt = self._arrow(img, color)
            anims.append(Transform(arr, nxt))
            if is_eig:
                highlights.append(arr)
        self.play(*anims, run_time=1.15)
        stay = self.ja_text("黄と橙は向きが同じ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, stay), run_time=0.4)
        for arr in highlights:
            self.play(Indicate(arr, color=WHITE), run_time=0.45)
        self.hold(0.6)

    def show_formula(self):
        formula = MathTex(r"Av=\lambda v").scale(1.2)
        formula.to_edge(DOWN, buff=0.4)
        cap = self.ja_text("固有ベクトル", font_size=26)
        cap.next_to(formula, UP, buff=0.18)
        self.play(Write(formula), FadeIn(cap), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
