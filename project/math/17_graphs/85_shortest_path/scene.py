from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import JapaneseScene


class ShortestPath(JapaneseScene):
    """#85 最短路は波のように広がる（約90秒）"""

    def construct(self):
        self.show_heading("最短路")
        self.draw_grid()
        self.wave()
        self.show_formula()
        self.hold(1.2)

    def draw_grid(self):
        self.origin = LEFT * 3.6 + DOWN * 1.55
        self.step = 1.35
        self.n = 4
        dots = VGroup()
        edges = VGroup()
        self.pos = {}
        for i in range(self.n):
            for j in range(self.n):
                p = self.origin + RIGHT * (i * self.step) + UP * (j * self.step)
                self.pos[(i, j)] = p
                dots.add(Dot(p, radius=0.08, color=GREY))
                if i + 1 < self.n:
                    edges.add(Line(p, p + RIGHT * self.step, color=GREY, stroke_width=2))
                if j + 1 < self.n:
                    edges.add(Line(p, p + UP * self.step, color=GREY, stroke_width=2))
        self.play(Create(edges), FadeIn(dots), run_time=0.8)
        start = Dot(self.pos[(0, 0)], radius=0.14, color=YELLOW)
        goal = Dot(self.pos[(3, 2)], radius=0.14, color=GREEN)
        sl = self.ja_text("始", font_size=22).next_to(start, DL, buff=0.08)
        gl = self.ja_text("終", font_size=22).next_to(goal, UR, buff=0.08)
        self.play(FadeIn(start), FadeIn(goal), FadeIn(sl), FadeIn(gl), run_time=0.45)
        self.hold(0.35)

    def wave(self):
        layers = [
            [(1, 0), (0, 1)],
            [(2, 0), (1, 1), (0, 2)],
            [(3, 0), (2, 1), (1, 2), (0, 3)],
            [(3, 1), (2, 2), (1, 3)],
            [(3, 2), (2, 3)],
        ]
        colors = [BLUE, TEAL, ORANGE, PINK, YELLOW]
        note = self.ja_text("距離 0", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.25)
        for k, layer in enumerate(layers, start=1):
            marks = VGroup(*[
                Dot(self.pos[cell], radius=0.12, color=colors[k - 1]) for cell in layer
            ])
            cap = self.ja_text(f"距離 {k}", font_size=24).move_to(note)
            self.play(FadeIn(marks), Transform(note, cap), run_time=0.45)
            self.hold(0.22)
        path = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]
        line = VMobject(color=YELLOW, stroke_width=6)
        line.set_points_as_corners([self.pos[p] for p in path])
        self.play(Create(line), run_time=0.8)
        self.hold(0.55)

    def show_formula(self):
        formula = self.ja_text("近い順が最短", font_size=28)
        formula.to_edge(DOWN, buff=0.35)
        self.play(FadeIn(formula), run_time=0.8)
        self.play(Indicate(formula, color=YELLOW), run_time=0.7)
        self.hold(1.2)
