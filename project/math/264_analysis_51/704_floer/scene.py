from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class FloerHomology(PacedScene):
    """#704 フローアホモロジー：無限次元モース理論（約45秒）"""

    def construct(self):
        self.show_heading("フローアホモロジー")
        self.draw()
        self.mid()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[-2, 2, 1], y_range=[-1, 2, 1], x_length=5.0, y_length=2.4, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.3 + UP * 0.1)
        crit = VGroup(*[Dot(axes.c2p(x, y), color=YELLOW, radius=0.09) for x, y in [(-1.2, 1.2), (0, 0.2), (1.2, 1.0)]])
        self.play(Create(axes), FadeIn(crit), run_time=1.3)

        note = self.ja_text("臨界点を数える", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("勾配流の軌道", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("3次元トポロジーへ", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"HF_*(Y)=\mathrm{Morse}_\infty(\mathcal{A})").scale(0.62)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
