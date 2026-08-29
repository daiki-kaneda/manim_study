from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class UnitaryGroup(PacedScene):
    """#367 ユニタリ群：U(t)=e^{itH} はノルム保存（約45秒）"""

    def construct(self):
        self.show_heading("ユニタリ群")
        self.draw_circle()
        self.flow()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_circle(self):
        self.O = LEFT * 0.5 + DOWN * 0.1
        self.circ = Circle(radius=2.0, color=GREY, stroke_width=3).move_to(self.O)
        self.v0 = Arrow(self.O, self.O + RIGHT * 1.6 + UP * 1.0, buff=0, color=BLUE, stroke_width=5)
        self.play(Create(self.circ), GrowArrow(self.v0), run_time=1.4)
        note = self.ja_text("単位ノルム", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def flow(self):
        tips = [
            self.O + RIGHT * 0.4 + UP * 1.85,
            self.O + LEFT * 1.2 + UP * 1.4,
            self.O + LEFT * 1.8 + UP * 0.2,
        ]
        arrows = VGroup(*[
            Arrow(self.O, tip, buff=0, color=ORANGE, stroke_width=4)
            for tip in tips
        ])
        cap = self.ja_text("時間発展", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("長さ不変", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), Indicate(self.circ, color=YELLOW), run_time=1.1)
        self.read(0.4)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.6)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"U(t)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"U(t)=e^{itH},\ \|U(t)x\|=\|x\|").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"U(t)=e^{itH},\ \|U(t)x\|=\|x\|").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
