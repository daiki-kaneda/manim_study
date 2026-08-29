from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene



class Directrix(PacedScene):
    """#590 準線：焦点との比が離心率（約45秒）"""

    def construct(self):
        self.show_heading("準線")
        self.draw_parabola()
        self.ratio()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_parabola(self):
        axes = Axes(x_range=[-0.5, 3, 1], y_range=[-2, 2, 1], x_length=5.0, y_length=3.0, tips=False,
                    axis_config={"stroke_width": 2, "include_ticks": False}).shift(LEFT * 0.8 + UP * 0.1)
        para = axes.plot(lambda x: 1.1 * (x ** 0.5) if x > 0 else 0, x_range=[0.02, 2.6], color=BLUE, stroke_width=4)
        para2 = axes.plot(lambda x: -1.1 * (x ** 0.5) if x > 0 else 0, x_range=[0.02, 2.6], color=BLUE, stroke_width=4)
        focus = Dot(axes.c2p(0.45, 0), color=YELLOW, radius=0.1)
        dline = DashedLine(axes.c2p(-0.45, -2), axes.c2p(-0.45, 2), color=ORANGE, stroke_width=3)
        self.play(Create(axes), Create(para), Create(para2), FadeIn(focus), Create(dline), run_time=1.5)
        note = self.ja_text("焦点と準線", font_size=24)
        note.to_edge(RIGHT, buff=0.45).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note

    def ratio(self):
        cap = self.ja_text("距離の比が一定", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap), run_time=0.9)
        self.read(0.25)
        cap2 = self.ja_text("離心率 e", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\frac{|PF|}{d(P,\ell)}").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\frac{|PF|}{d(P,\ell)}=e").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\frac{|PF|}{d(P,\ell)}=e").scale(0.9)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
