from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class GraphColoring(JapaneseScene):
    """#84 グラフの彩色（約90秒）"""

    def construct(self):
        self.show_heading("彩色")
        self.draw_triangle()
        self.draw_square()
        self.show_formula()
        self.hold(1.2)

    def _dots(self, pts, colors):
        return VGroup(*[Dot(p, radius=0.16, color=c) for p, c in zip(pts, colors)])

    def draw_triangle(self):
        origin = LEFT * 3.1 + DOWN * 0.15
        pts = [
            origin + UP * 1.45,
            origin + LEFT * 1.35 + DOWN * 1.15,
            origin + RIGHT * 1.35 + DOWN * 1.15,
        ]
        edges = VGroup(*[
            Line(pts[i], pts[(i + 1) % 3], color=WHITE, stroke_width=3) for i in range(3)
        ])
        grey = self._dots(pts, [GREY, GREY, GREY])
        lab = self.ja_text("三角形", font_size=24).next_to(edges, UP, buff=0.35)
        self.play(Create(edges), FadeIn(grey), FadeIn(lab), run_time=0.7)
        colored = self._dots(pts, [BLUE, ORANGE, GREEN])
        self.play(Transform(grey, colored), run_time=0.7)
        self.hold(0.45)
        self.tri = VGroup(edges, grey, lab)

    def draw_square(self):
        origin = RIGHT * 2.5 + DOWN * 0.15
        pts = [
            origin + LEFT * 1.2 + UP * 1.2,
            origin + RIGHT * 1.2 + UP * 1.2,
            origin + RIGHT * 1.2 + DOWN * 1.2,
            origin + LEFT * 1.2 + DOWN * 1.2,
        ]
        edges = VGroup(*[
            Line(pts[i], pts[(i + 1) % 4], color=WHITE, stroke_width=3) for i in range(4)
        ])
        grey = self._dots(pts, [GREY] * 4)
        lab = self.ja_text("四角形", font_size=24).next_to(edges, UP, buff=0.35)
        self.play(Create(edges), FadeIn(grey), FadeIn(lab), run_time=0.7)
        colored = self._dots(pts, [BLUE, ORANGE, BLUE, ORANGE])
        self.play(Transform(grey, colored), run_time=0.7)
        note = self.ja_text("2 色で足りる", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.65)

    def show_formula(self):
        formula = self.ja_text("隣り合う頂点は違う色", font_size=28)
        formula.to_edge(DOWN, buff=0.38)
        self.play(FadeIn(formula), run_time=0.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
