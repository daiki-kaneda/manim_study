from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class UltraweakTopology(PacedScene):
    """#486 超弱作用素位相：トレース双対で決まる位相（約45秒）"""

    def construct(self):
        self.show_heading("超弱作用素位相")
        self.draw_dual()
        self.nets()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_dual(self):
        box = RoundedRectangle(width=3.2, height=1.6, corner_radius=0.12, color=BLUE, stroke_width=3).shift(LEFT * 2.0 + UP * 0.2)
        lab = MathTex(r"B(H)_*", font_size=36).move_to(box)
        self.play(Create(box), FadeIn(lab), run_time=1.3)
        note = self.ja_text("トレースクラス双対", font_size=24)
        note.to_edge(RIGHT, buff=0.35).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def nets(self):
        arrows = VGroup(*[
            Arrow(LEFT * 0.2 + UP * (0.8 - i * 0.7), RIGHT * 2.6 + UP * (0.8 - i * 0.7),
                  buff=0.05, color=c, stroke_width=3)
            for i, c in enumerate([ORANGE, TEAL, YELLOW])
        ])
        cap = self.ja_text("汎関数で収束", font_size=24).move_to(self.note)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), Transform(self.note, cap), run_time=1.5)
        self.read(0.25)
        cap2 = self.ja_text("WOTより細かい", font_size=24).move_to(self.note)
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
        eq = MathTex(r"T_\alpha\to T\ \Leftrightarrow\ \mathrm{tr}(\rho T_\alpha)\to\mathrm{tr}(\rho T)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"T_\alpha\to T\ \Leftrightarrow\ \mathrm{tr}(\rho T_\alpha)\to\mathrm{tr}(\rho T)").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"T_\alpha\to T\ \Leftrightarrow\ \mathrm{tr}(\rho T_\alpha)\to\mathrm{tr}(\rho T)").scale(0.72)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
