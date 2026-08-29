from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class CalderonCommutator(PacedScene):
    """#582 カルデロン交換子：[H,a] の有界性（約45秒）"""

    def construct(self):
        self.show_heading("カルデロン交換子")
        self.draw_ops()
        self.comm()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_ops(self):
        H = RoundedRectangle(width=2.0, height=1.3, corner_radius=0.1, color=BLUE, stroke_width=3).shift(LEFT * 2.6 + UP * 0.2)
        a = RoundedRectangle(width=2.0, height=1.3, corner_radius=0.1, color=TEAL, stroke_width=3).shift(RIGHT * 2.6 + UP * 0.2)
        self.play(Create(H), FadeIn(MathTex(r"H", font_size=36).move_to(H)),
                  Create(a), FadeIn(MathTex(r"a", font_size=36).move_to(a)), run_time=1.3)
        note = self.ja_text("ヒルベルト変換", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def comm(self):
        box = RoundedRectangle(width=2.8, height=1.2, corner_radius=0.1, color=ORANGE, stroke_width=3).shift(DOWN * 0.9)
        cap = self.ja_text("交換子が有界", font_size=24).move_to(self.note)
        self.play(Create(box), FadeIn(MathTex(r"[H,a]", font_size=34).move_to(box)), Transform(self.note, cap), run_time=1.4)
        self.read(0.25)
        cap2 = self.ja_text("リプシッツで十分", font_size=24).move_to(self.note)
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
        eq = MathTex(r"[H,a]f").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"[H,a]f=H(af)-a\,Hf").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"[H,a]f=H(af)-a\,Hf").scale(0.88)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
