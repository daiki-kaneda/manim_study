from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class EulerCircuit(JapaneseScene):
    """#81 オイラー閉路（約90秒）"""

    def construct(self):
        self.show_heading("一筆書き")
        self.draw_graph()
        self.trace()
        self.show_formula()
        self.hold(1.2)

    def draw_graph(self):
        c = DOWN * 0.15
        self.pts = {
            "A": c + LEFT * 2.4 + UP * 1.35,
            "B": c + RIGHT * 2.4 + UP * 1.35,
            "C": c + RIGHT * 2.4 + DOWN * 1.35,
            "D": c + LEFT * 2.4 + DOWN * 1.35,
        }
        order = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")]
        self.edges = VGroup()
        for u, v in order:
            self.edges.add(Line(self.pts[u], self.pts[v], color=WHITE, stroke_width=4))
        dots = VGroup(*[Dot(p, radius=0.09, color=BLUE) for p in self.pts.values()])
        self.play(LaggedStart(*[Create(e) for e in self.edges], lag_ratio=0.12), run_time=0.9)
        self.play(FadeIn(dots), run_time=0.35)
        note = self.ja_text("次数はすべて 2", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.35)
        self.hold(0.5)
        self.note = note

    def trace(self):
        path = ["A", "B", "C", "D", "A"]
        walker = Dot(self.pts["A"], radius=0.13, color=YELLOW)
        self.play(FadeIn(walker), run_time=0.25)
        for i in range(len(path) - 1):
            self.play(walker.animate.move_to(self.pts[path[i + 1]]), run_time=0.45)
            self.edges[i].set_color(YELLOW)
        cap = self.ja_text("戻ってこれる", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.35)
        self.hold(0.7)

    def show_formula(self):
        formula = self.ja_text("偶数次数なら閉じる", font_size=28)
        formula.to_edge(DOWN, buff=0.38)
        self.play(FadeIn(formula), run_time=0.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
