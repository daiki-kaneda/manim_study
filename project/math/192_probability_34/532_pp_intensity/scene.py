from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class PointProcessIntensity(PacedScene):
    """#532 点過程強度：履歴に依存する発生率（約45秒）"""

    def construct(self):
        self.show_heading("点過程強度")
        self.draw_points()
        self.history()
        self.show_formula()
        self.read(1.4)

    def draw_points(self):
        line = NumberLine(x_range=[0, 6, 1], length=7, include_numbers=False).shift(UP * 0.5)
        xs = [0.7, 1.5, 2.8, 3.1, 4.4, 5.2]
        dots = VGroup(*[Dot(line.n2p(x), color=YELLOW, radius=0.1) for x in xs])
        self.play(Create(line), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.1), run_time=1.4)
        note = self.ja_text("イベント列", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def history(self):
        brace = BraceBetweenPoints(LEFT * 2.5 + DOWN * 0.3, RIGHT * 0.5 + DOWN * 0.3, color=ORANGE)
        cap = self.ja_text("履歴で強度が変わる", font_size=24).move_to(self.note)
        self.play(GrowFromCenter(brace), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("自己励起も可", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    def show_formula(self):
        formula = MathTex(r"\lambda(t\mid\mathcal{H}_{t-})=\lim_{h\downarrow0}\frac{P(\Delta N=1\mid\mathcal{H}_{t-})}{h}").scale(0.62)
        formula.to_edge(DOWN, buff=0.2)
        self.play(Write(formula), run_time=1.9)
        self.play(Indicate(formula, color=YELLOW), run_time=0.85)
