from pathlib import Path
import sys

for _parent in Path(__file__).resolve().parents:
    if (_parent / "manim_math" / "__init__.py").is_file():
        sys.path.insert(0, str(_parent))
        break

from manim import *
from manim_math import PacedScene


class ResolventSet(PacedScene):
    """#474 リゾルベント集合：スペクトルの外側（約45秒）"""

    def construct(self):
        self.show_heading("リゾルベント集合")
        self.draw_plane()
        self.outside()
        self.derive()
        self.show_formula()
        self.read(1.4)

    def draw_plane(self):
        axes = ComplexPlane(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.0, 2.0, 1],
            x_length=6.0,
            y_length=4.0,
        ).shift(UP * 0.15)
        axes.add_coordinates()
        self.play(Create(axes), run_time=1.2)
        note = self.ja_text("複素平面", font_size=24)
        note.to_edge(RIGHT, buff=0.4).shift(UP * 1.65)
        self.play(FadeIn(note), run_time=0.4)
        self.read(0.3)
        self.note = note
        self.axes = axes

    def outside(self):
        # spectrum blob near origin
        blob = Ellipse(width=1.6, height=1.1, color=RED, fill_opacity=0.35, stroke_width=2)
        blob.move_to(self.axes.n2p(0.2 + 0.1j))
        dots = VGroup(*[
            Dot(self.axes.n2p(z), color=YELLOW, radius=0.08)
            for z in [1.8, -1.6 + 0.9j, 0.5 - 1.5j]
        ])
        cap = self.ja_text("外がリゾルベント", font_size=24).move_to(self.note)
        self.play(FadeIn(blob), Transform(self.note, cap), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.15), run_time=1.0)
        self.read(0.25)
        cap2 = self.ja_text("逆が有界", font_size=24).move_to(self.note)
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
        eq = MathTex(r"\rho(T)").scale(0.62)
        eq.to_edge(DOWN, buff=0.2)
        self.play(Write(eq), run_time=1.05)
        self.read(0.3)
        cap2 = self.ja_text("整理", font_size=24).move_to(self.note)
        self.play(Transform(self.note, cap2), run_time=0.75)
        self.read(0.2)
        eq2 = MathTex(r"\rho(T)=\{\lambda:(T-\lambda)^{-1}\in B(H)\}").scale(0.62)
        eq2.move_to(eq)
        self.play(Transform(eq, eq2), run_time=1.0)
        self.read(0.35)
        self.proof_eq = eq

    def show_formula(self):
        formula = MathTex(r"\rho(T)=\{\lambda:(T-\lambda)^{-1}\in B(H)\}").scale(0.78)
        formula.move_to(self.proof_eq)
        self.play(Transform(self.proof_eq, formula), run_time=1.9)
        self.play(Indicate(self.proof_eq, color=YELLOW), run_time=0.85)
