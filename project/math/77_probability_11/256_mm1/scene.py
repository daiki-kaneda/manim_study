from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class MM1Queue(PacedScene):
    """#256 M/M/1：到着とサービスのバランス（約45秒）"""

    def construct(self):
        self.show_heading("M/M/1 待ち行列")
        self.draw_server()
        self.flow()
        self.show_formula()
        self.read(1.4)

    def draw_server(self):
        self.server = RoundedRectangle(width=1.4, height=1.0, corner_radius=0.1, color=YELLOW, stroke_width=3)
        self.server.shift(RIGHT * 2.5 + UP * 0.3)
        slab = self.ja_text("窓口", font_size=22).move_to(self.server)
        self.play(Create(self.server), FadeIn(slab), run_time=1.1)
        note = self.ja_text("サービス", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def flow(self):
        # queue dots arriving from left
        queue = VGroup()
        for i in range(4):
            d = Dot(LEFT * 3.2 + RIGHT * i * 0.7 + UP * 0.3, radius=0.14, color=BLUE)
            queue.add(d)
        self.play(LaggedStart(*[FadeIn(d, shift=RIGHT * 0.3) for d in queue], lag_ratio=0.15), run_time=1.5)
        cap = self.ja_text("到着 λ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.5)
        self.read(0.25)
        # one serves
        self.play(queue[0].animate.move_to(self.server.get_center()), run_time=1.0)
        self.play(FadeOut(queue[0]), run_time=0.5)
        cap2 = self.ja_text("処理 μ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.5)
        # remaining compact
        self.play(queue[1].animate.shift(RIGHT * 0.7), queue[2].animate.shift(RIGHT * 0.7), queue[3].animate.shift(RIGHT * 0.7), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"L=\frac{\rho}{1-\rho},\ \rho=\frac{\lambda}{\mu}").scale(0.9)
        formula.to_edge(DOWN, buff=0.26)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
