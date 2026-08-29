from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class Handshake(JapaneseScene):
    """#82 握手補題（約90秒）"""

    def construct(self):
        self.show_heading("握手補題")
        self.draw_graph()
        self.count()
        self.show_formula()
        self.hold(1.2)

    def draw_graph(self):
        c = DOWN * 0.1 + LEFT * 0.4
        self.pts = [
            c + LEFT * 2.2 + UP * 1.4,
            c + RIGHT * 2.0 + UP * 1.2,
            c + RIGHT * 1.5 + DOWN * 1.45,
            c + LEFT * 2.0 + DOWN * 1.25,
            c + LEFT * 0.2 + UP * 0.15,
        ]
        pairs = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 4), (2, 4)]
        self.edges = VGroup(*[Line(self.pts[i], self.pts[j], color=WHITE, stroke_width=3) for i, j in pairs])
        self.dots = VGroup(*[Dot(p, radius=0.1, color=BLUE) for p in self.pts])
        self.play(Create(self.edges), run_time=0.8)
        self.play(FadeIn(self.dots), run_time=0.35)
        self.hold(0.4)

    def count(self):
        degs = [3, 3, 3, 2, 3]
        labels = VGroup()
        for p, d in zip(self.pts, degs):
            lab = MathTex(str(d), color=YELLOW, font_size=30)
            lab.move_to(p + UP * 0.38)
            labels.add(lab)
        self.play(LaggedStart(*[FadeIn(lab) for lab in labels], lag_ratio=0.12), run_time=0.9)
        note = self.ja_text("次数の和は 14", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.45)
        cap = self.ja_text("辺は 7 本", font_size=24).move_to(note)
        self.play(Transform(note, cap), run_time=0.4)
        self.hold(0.6)

    def show_formula(self):
        formula = MathTex(r"\sum_v \deg v = 2|E|").scale(1.1)
        formula.to_edge(DOWN, buff=0.38)
        self.play(Write(formula), run_time=1.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
