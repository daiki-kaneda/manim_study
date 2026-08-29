from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class UniqueContinuation(PacedScene):
    """#608 一意接続性：局所ゼロが全域ゼロを強制（約45秒）"""

    def construct(self):
        self.show_heading("一意接続性")
        self.draw_domain()
        self.extend()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_domain(self):
        domain = Circle(radius=2.0, color=BLUE, stroke_width=3).shift(LEFT * 0.3 + UP * 0.1)
        hole = Circle(radius=0.55, color=ORANGE, stroke_width=3, fill_opacity=0.25).shift(LEFT * 0.8 + UP * 0.4)
        self.play(Create(domain), FadeIn(hole),
                  FadeIn(MathTex(r"u=0", font_size=28).move_to(hole)), run_time=1.4)
        note = self.ja_text("開集合でゼロ", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.domain = domain

    def extend(self):
        fill = Circle(radius=2.0, color=TEAL, stroke_width=0, fill_opacity=0.2).move_to(self.domain)
        cap = self.ja_text("全域へ伝播", font_size=24).move_to(self.note)
        self.play(FadeIn(fill), Transform(self.note, cap), run_time=1.2)
        self.read(0.25)
        cap2 = self.ja_text("解析性・Carleman", font_size=22).move_to(self.note)
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
        eq = MathTex(r"u|_{\omega}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"u|_{\omega}=0\ \Rightarrow\ u\equiv 0").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"u|_{\omega}=0\ \Rightarrow\ u\equiv 0").scale(0.85)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
