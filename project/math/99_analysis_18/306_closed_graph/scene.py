from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ClosedGraph(PacedScene):
    """#306 閉グラフ：閉なら有界線形（約45秒）"""

    def construct(self):
        self.show_heading("閉グラフ定理")
        self.draw_graph()
        self.closed()
        self.show_formula()
        self.read(1.4)

    def draw_graph(self):
        self.axes = Axes(x_range=[0, 4, 1], y_range=[0, 3.5, 1], x_length=5.5, y_length=3.2,
                         tips=False, axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.6 + UP * 0.15)
        g = self.axes.plot(lambda x: 0.6 * x + 0.5, x_range=[0.3, 3.5], color=BLUE, stroke_width=4)
        self.play(Create(self.axes), Create(g), run_time=1.4)
        note = self.ja_text("グラフ", font_size=24)
        note.to_edge(RIGHT, buff=0.55).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def closed(self):
        # sequence approaching a point on the graph
        pts = VGroup(*[Dot(self.axes.c2p(1.0 + 0.4 * i, 0.6 * (1.0 + 0.4 * i) + 0.5), color=ORANGE, radius=0.08) for i in range(4)])
        lim = Dot(self.axes.c2p(2.6, 0.6 * 2.6 + 0.5), color=YELLOW, radius=0.11)
        cap = self.ja_text("点列の極限", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in pts], lag_ratio=0.12), Transform(self.note, cap), run_time=1.3)
        self.play(FadeIn(lim, scale=0.5), run_time=0.7)
        self.read(0.25)
        cap2 = self.ja_text("閉なら連続", font_size=24).move_to(self.note)
        box = SurroundingRectangle(lim, color=TEAL, buff=0.15)
        self.play(Create(box), Transform(self.note, cap2), run_time=1.1)
        self.read(0.4)

    def show_formula(self):
        formula = MathTex(r"\mathrm{graph}(T)\ \text{closed}\Rightarrow T\ \text{bounded}").scale(0.75)
        formula.to_edge(DOWN, buff=0.22)
        self.play(Write(formula), run_time=2.0)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
