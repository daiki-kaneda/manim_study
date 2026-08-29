from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class AdaiClip(PacedScene):
    """#1031 AdaiClip（約45秒）"""

    def construct(self):
        self.show_heading("AdaiClip")
        self.draw()
        self.mid()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw(self):
        axes = Axes(x_range=[-0.2, 3.2, 1], y_range=[-0.2, 2.2, 1], x_length=5.2, y_length=3.0).shift(LEFT * 0.4 + DOWN * 0.1)
        curve = axes.plot(lambda x: 0.35 * (x - 1.4) ** 2 + 0.45, x_range=[0.1, 2.9], color=BLUE)
        dot = Dot(axes.c2p(2.2, 0.35 * (2.2 - 1.4) ** 2 + 0.45), color=YELLOW)
        self.play(Create(axes), Create(curve), run_time=1.1)
        self.play(FadeIn(dot), run_time=0.35)
        note = self.ja_text("クリップつきAdai", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def mid(self):
        cap = self.ja_text("適応慣性制限", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("発散防止", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.8)
        self.read(0.35)

    
    def derive(self):
        if getattr(self, "note", None) is not None:
            cap = self.ja_text("途中式", font_size=24).move_to(self.note)
            self.play(Transform(self.note, cap), run_time=0.75)
        else:
            self.note = self.ja_text("途中式", font_size=24)
            self.note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
            self.play(FadeIn(self.note), run_time=0.5)
        self.read(0.2)
        eq = MathTex(r"\Rightarrow").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.35)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(chr(92)+"beta"+"="+chr(92)+"mathrm"+"{clip}("+chr(92)+"hat"+chr(92)+"beta"+")").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.25)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(chr(92)+"beta"+"="+chr(92)+"mathrm"+"{clip}("+chr(92)+"hat"+chr(92)+"beta"+")").scale(0.68)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
