from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class RenewalProcess(PacedScene):
    """#388 再生過程：待ち時間の和で点が並ぶ（約45秒）"""

    def construct(self):
        self.show_heading("再生過程")
        self.draw_timeline()
        self.renewals()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_timeline(self):
        self.axis = NumberLine(
            x_range=[0, 10, 1], length=8.5, include_numbers=False,
            stroke_width=3, color=GREY,
        ).shift(UP * 0.4)
        self.play(Create(self.axis), run_time=1.0)
        note = self.ja_text("時間軸", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def renewals(self):
        times = [0, 1.4, 2.9, 4.1, 5.8, 7.2, 8.6]
        dots = VGroup(*[Dot(self.axis.n2p(t), color=ORANGE, radius=0.1) for t in times])
        gaps = VGroup(*[
            BraceBetweenPoints(self.axis.n2p(times[i]), self.axis.n2p(times[i + 1]), direction=DOWN, color=TEAL)
            for i in range(len(times) - 1)
        ])
        cap = self.ja_text("再生時刻", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.1), Transform(self.note, cap), run_time=1.6)
        self.read(0.2)
        cap2 = self.ja_text("独立な間隔", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[FadeIn(g) for g in gaps], lag_ratio=0.08), Transform(self.note, cap2), run_time=1.4)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"N(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"N(t)=\sup\{n:S_n\le t\}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"N(t)=\sup\{n:S_n\le t\}").scale(0.95)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.8)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
