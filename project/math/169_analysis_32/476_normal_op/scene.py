from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class NormalOperator(PacedScene):
    """#476 正規作用素：T*T=TT* で同時対角化（約45秒）"""

    def construct(self):
        self.show_heading("正規作用素")
        self.draw_commute()
        self.unitary()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_commute(self):
        T = RoundedRectangle(width=1.8, height=1.2, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.4 + UP * 0.4)
        Ts = RoundedRectangle(width=1.8, height=1.2, corner_radius=0.1, color=TEAL, stroke_width=3).shift(LEFT * 2.4 + DOWN * 1.1)
        self.play(
            Create(T), FadeIn(MathTex("T", font_size=34).move_to(T)),
            Create(Ts), FadeIn(MathTex(r"T^*", font_size=34).move_to(Ts)),
            run_time=1.3,
        )
        note = self.ja_text("交換する", font_size=24)
        note.to_edge(RIGHT, buff=0.5).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def unitary(self):
        U = RoundedRectangle(width=2.4, height=1.5, corner_radius=0.12, color=ORANGE, stroke_width=3).shift(RIGHT * 2.0 + UP * 0.1)
        lab = MathTex(r"U^*TU=\Lambda", font_size=30).move_to(U)
        arrow = Arrow(LEFT * 0.9, RIGHT * 0.4, buff=0.05, color=YELLOW, stroke_width=4)
        cap = self.ja_text("ユニタリ対角", font_size=24).move_to(self.note)
        self.play(GrowArrow(arrow), Create(U), FadeIn(lab), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("スペクトル定理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
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
        eq = MathTex(r"T^*T").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"T^*T=TT^*\quad\Rightarrow\quad T=U\Lambda U^*").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"T^*T=TT^*\quad\Rightarrow\quad T=U\Lambda U^*").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
